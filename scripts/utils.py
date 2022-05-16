from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

from people.models import Person, Person_Natural, Person_Legal, Person_E_Mail, Person_Address, Person_Phone
from references.models import Address, PUC, E_Mail, Phone, Charge_Factor, Factor_Data
from properties.models import Estate, Estate_Person, Realty, Realty_Estate, Estate_Appraisal
from accounting.models import Account, Ledger, Ledger_Type, Ledger_Template, Charge, Charge_Template
from accountables.models import Accountable, Accountable_Transaction_Type, Accountable_Concept, Lease_Realty, Lease_Realty_Realty, Lease_Realty_Person, Date_Value
    
classes_list = {
    'all': [
        'puc', 
        'charge_factor', 
        'factor_data', 
        'account', 
        'address', 
        'phone', 
        'e_mail', 
        'person', 
        'person_address', 
        'person_phone', 
        'person_e_mail', 
        'estate', 
        'estate_person', 
        'estate_appraisal', 
        'realty', 
        'realty_estate', 
        'ledger_type', 
        'lease_realty', 
        'transaction_type', 
        'lease_realty_realty', 
        'lease_realty_person', 
        'date_value', 
        'ledger_template', 
        'charge_template', 
        'charge_concept', 
        'ledger', 
        'charge'
    ],
    'references': [
        'puc', 
        'charge_factor', 
        'factor_data', 
        'address', 
        'phone', 
        'e_mail', 
        'transaction_type'
    ],
    'people': [
        'person', 
        'person_address', 
        'person_phone', 
        'person_e_mail'
    ],
    'properties': [
        'estate', 
        'estate_person', 
        'estate_appraisal', 
        'realty', 
        'realty_estate'
    ],
    'accountables': [
        'lease_realty', 
        'transaction_type', 
        'lease_realty_realty', 
        'lease_realty_person', 
        'date_value'
        ],
    'accounting': [
        'ledger_type', 
        'ledger_template', 
        'charge_template', 
        'ledger', 
        'charge'
    ],
    'no-registers': [
        'puc', 
        'charge_factor', 
        'factor_data', 
        'account', 
        'address', 
        'phone', 
        'e_mail', 
        'person', 
        'person_address', 
        'person_phone', 
        'person_e_mail', 
        'estate', 
        'estate_person', 
        'estate_appraisal', 
        'realty', 
        'realty_estate', 
        'ledger_type', 
        'lease_realty', 
        'transaction_type', 
        'lease_realty_realty', 
        'lease_realty_person', 
        'date_value', 
        'ledger_template', 
        'charge_template'
    ],
    'registers': [
        'charge_concept', 
        'ledger', 
        'charge'
    ]
}

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
