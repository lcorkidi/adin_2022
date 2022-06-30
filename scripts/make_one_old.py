import pandas as pd
from datetime import datetime
from django.contrib.auth import get_user_model

from people.models import Person, Person_Natural, Person_Legal, Person_E_Mail, Person_Address, Person_Phone
from people.models.person import Person_Legal_Person_Natural
from references.models import Address, PUC, E_Mail, Phone, Charge_Factor, Factor_Data
from properties.models import Estate, Estate_Person, Realty, Realty_Estate, Estate_Appraisal
from accounting.models import Account, Ledger, Ledger_Type, Ledger_Template, Charge, Charge_Template
from accountables.models import Accountable, Accountable_Transaction_Type, Accountable_Concept, Lease_Realty, Lease_Realty_Realty, Lease_Realty_Person, Date_Value

info_df = pd.read_json('_files/_raw_data_info.json')

def run(class_name):
    dt0 = datetime.now()
    df2objs(pd.read_csv(f'_files/{class_name}.csv'), info_df, True)
    dt1 = datetime.now()

    print(f'time: {dt1 - dt0}')

def df2objs(dr, rdi, save=False):
    user = get_user_model().objects.all()[0]
    objs = []
    for index, row in dr.iterrows():
        obj = eval(f"{row['class']}()")
        for attr in rdi.loc['value_attrs', row['class']]:
            if row[attr] not in [-9999, 'ZZZZZ', '1900-01-01']:
                setattr(obj, attr, row[attr])
        for attr, model in rdi.loc['fk_attrs', row['class']].items():
            if row[attr] not in [-9999, 'ZZZZZ', '1900-01-01']:
                setattr(obj, attr, eval(f"{model}.objects.get(pk='{row[attr]}')"))
        obj.state_change_user = user
        if save: obj.save()
        objs.append(obj)
    return objs
