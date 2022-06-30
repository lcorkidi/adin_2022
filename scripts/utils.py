import pandas as pd
from os.path import join
from adin.settings import BASE_DIR
from datetime import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from people.models import Person, Person_Natural, Person_Legal, Person_E_Mail, Person_Address, Person_Phone
from references.models import Address, PUC, E_Mail, Phone, Charge_Factor, Factor_Data
from properties.models import Estate, Estate_Person, Realty, Realty_Estate, Estate_Appraisal
from accounting.models import Account, Ledger, Ledger_Type, Ledger_Template, Charge, Charge_Template
from accountables.models import Accountable, Accountable_Transaction_Type, Accountable_Concept, Lease_Realty, Lease_Realty_Realty, Lease_Realty_Person, Date_Value
    
classes_list = {
        'references': [
            'puc', 
            'charge_factor', 
            'factor_data', 
            'address', 
            'phone', 
            'e_mail'
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
            'accountable_transaction_type',
            'lease_realty', 
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

def data_load(load_info, load_list=None):
    counter = 0
    timers = { counter : datetime.now() }
    if load_list:
        for element in load_list:
            model_load(load_info[element])
            counter = counter + 1
            timers[counter] = datetime.now()
            print(f"{element}: {timers[counter] - timers[counter - 1]}")
    else:
        for value in load_info.values():
            model_load(value)
            counter = counter + 1
            timers[counter] = datetime.now()
            print(f"{element}: {timers[counter] - timers[counter - 1]}")
    
def model_load(load_dict):
    df_from_csv = pd.read_csv(join(BASE_DIR, f"_files/exports/{load_dict['csv_name']}"), keep_default_na=False)\
        .drop(load_dict['to_drop'], axis=1)\
        .rename(columns=load_dict['to_rename'])
    data_dict = df_from_csv\
        .assign(**{column: df_from_csv[column].apply(lambda x: None if x == '' else x) for column in df_from_csv.columns})\
        .assign(**{column: df_from_csv[column].apply(lambda x: model.objects.get(pk=x)) for column, model in load_dict['fk_dict'].items()})\
        .assign(state=df_from_csv.state.apply(lambda x: 2))\
        .to_dict('index')
    load_dict['model'].objects.bulk_create([load_dict['model'](**data) for key, data in data_dict.items()])