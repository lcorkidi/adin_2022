import pandas as pd
from datetime import date as dt, timedelta as td
from django.contrib.auth import get_user_model

from people.models import Person, Person_Natural, Person_Legal, Person_E_Mail, Person_Address, Person_Phone
from references.models import Address, PUC, E_Mail, Phone, Transaction_Type, Charge_Factor, Factor_Data
from properties.models import Estate, Estate_Person, Realty, Realty_Estate, Estate_Appraisal
from accounting.models import Account, Ledger, Ledger_Type, Ledger_Template, Charge, Charge_Concept, Charge_Template
from accountables.models import Accountable, Lease_Realty, Lease_Realty_Realty, Lease_Realty_Person, Date_Value
    
# load = lambda x: pd.read_csv(f'_files/copy/{x.lower()}.csv')
# dump = lambda x,n: x.to_csv(f'_files/copy/{n.lower()}.csv', index=False)
load = lambda x: pd.read_csv(f'../_files/copy/{x.lower()}.csv')
dump = lambda x,n: x.to_csv(f'../_files/copy/{n.lower()}.csv', index=False)

def df2objs(dr, rdi, save=False):
    user = get_user_model().objects.all()[0]
    objs = []
    for index, row in dr.iterrows():
        obj = eval(f"{row['class']}()")
        for attr in rdi.loc['value_attrs', row['class']]:
            if row[attr] not in [-9999, 'ZZZZZ']:
                setattr(obj, attr, row[attr])
        for attr, model in rdi.loc['fk_attrs', row['class']].items():
            if row[attr] not in [-9999, 'ZZZZZ']:
                setattr(obj, attr, eval(f"{model}.objects.get(pk='{row[attr]}')"))
        obj.state_change_user = user
        if save: obj.save()
        objs.append(obj)
    return objs

def get_ledger_csv():
    charges = load('Charge')
    concepts = load('Charge_Concept')
    ledgers = load('Ledger')    
    return charges\
            .join(concepts.set_index('code'), on='concept')\
            .join(ledgers.set_index('code'), on='ledger', lsuffix='_concept')\
            .sort_values(by=['account','date','ledger'])\
            .reset_index(drop=True)

def filter_ledger_by_date(ledger, exact_date=None, start_date=None, end_date=None, period=None):
    # these dates must conform all across the api. Forcing column types can be a way to go or having a constant expression for the datetime (iso)format.
    # assumes only column 'date' carries the true date info. Other referenced 'dates' are treated as attributes of other kind by the ledger
    if exact_date is not None:
        data = ledger.query(f'ledger__date=={exact_date}')
    else:
        end_date = end_date or dt.today()
        period = period or td(days=365)
        start_date = start_date or end_date - period 
        data = ledger.query(f'ledger__date>="{start_date}" & ledger__date<="{end_date}"') 
    return data

def filter_ledger_by_parts(ledger, parts=None):
    # and we can agree on which columns are considered 'parts'
    data = ledger.copy()
    if isinstance(parts,dict):
        for part,val in parts.items():
            data = data.query(f'{part}=={val}')
    return data

def total_balance(ledger, group=['concept__accountable','account']):
    data = ledger\
        .groupby(group)['value']\
        .sum()\
        .to_frame()\
        .rename(columns={'value':'total'})
    return data

def pending_balance_annotation(ledger, group=['concept__accountable','account'], last=True):
    data = ledger[group+['ledger__date','value']]\
        .sort_values(by=group+['ledger__date'])\
        .assign(pending=lambda df:df.groupby(group)['value'].cumsum())
    if last: data = data.groupby(group)[['ledger__date','pending']].last()
    return data
