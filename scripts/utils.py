from django.contrib.auth import get_user_model

from people.models import Person, Person_Natural, Person_Legal, Person_E_Mail, Person_Address, Person_Phone
from references.models import Address, PUC, E_Mail, Phone, Transaction_Type, Charge_Factor, Factor_Data
from properties.models import Estate, Estate_Person, Realty, Realty_Estate, Estate_Appraisal
from accounting.models import Account, Ledger, Ledger_Type, Ledger_Template, Charge, Charge_Concept, Charge_Template
from accountables.models import Accountable, Lease_Realty, Lease_Realty_Realty, Lease_Realty_Person, Date_Value

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
