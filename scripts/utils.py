import pandas as pd
from os.path import join
from adin.settings import BASE_DIR
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from people.models import Person, Person_Natural, Person_Legal, Person_E_Mail, Person_Address, Person_Phone
from people.models.person import Person_Legal_Person_Natural
from references.models import Address, PUC, E_Mail, Phone, Charge_Factor, Factor_Data
from properties.models import Estate, Estate_Person, Realty, Realty_Estate, Estate_Appraisal
from accounting.models import Account, Ledger, Ledger_Type, Ledger_Template, Charge, Charge_Template
from accountables.models import Accountable, Accountable_Transaction_Type, Accountable_Concept, Lease_Realty, Lease_Realty_Realty, Lease_Realty_Person, Date_Value
    
load_lists = {
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
            'lease_realty', 
            'lease_realty_realty', 
            'lease_realty_person', 
            'date_value',
            'accountable_transaction_type'
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
            'accountable_transaction_type',
            'ledger_template', 
            'charge_template'
        ],
        'registers': [
            'charge_concept', 
            'ledger', 
            'charge'
        ]
    }

load_info = { 
        'puc' : {
            'csv_name' : '0_puc.csv',
            'fk_dict' : {'state_change_user': User},
            'model' : PUC,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user'},
            'bulk' : True
            },
        'charge_factor' : {
            'csv_name' : '1_charge_factor.csv',
            'fk_dict' : {'state_change_user':User},
            'model' : Charge_Factor,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user'},
            'bulk' : True
            },
        'factor_data' : {
            'csv_name' : '2_factor_data.csv',
            'fk_dict' : {'state_change_user':User, 'factor':Charge_Factor},
            'model' : Factor_Data,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user'},
            'bulk' : True
            },
        'address' : {
            'csv_name' : '3_address.csv',
            'fk_dict' : {'state_change_user':User},
            'model' : Address,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user'},
            'bulk' : True
            },
        'phone' : {
            'csv_name' : '4_phone.csv',
            'fk_dict' : {'state_change_user':User},
            'model' : Phone,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user'},
            'bulk' : True
            },
        'e_mail' : {
            'csv_name' : '5_e_mail.csv',
            'fk_dict' : {'state_change_user':User},
            'model' : E_Mail,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user'},
            'bulk' : True
            },
        'person_natural' : {
            'csv_name' : '6_person_natural.csv',
            'fk_dict' : {'state_change_user':User},
            'model' : Person_Natural,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user'},
            'bulk' : False
            },
        'person_legal' : {
            'csv_name' : '7_person_legal.csv',
            'fk_dict' : {'state_change_user':User},
            'model' : Person_Legal,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user'},
            'bulk' : False
            },
        'person_address' : {
            'csv_name' : '8_person_address.csv',
            'fk_dict' : {'state_change_user':User, 'person':Person, 'address':Address},
            'model' : Person_Address,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'person_id':'person', 'address_id':'address'},
            'bulk' : True
            },
        'person_phone' : {
            'csv_name' : '9_person_phone.csv',
            'fk_dict' : {'state_change_user':User, 'person':Person, 'phone':Phone},
            'model' : Person_Phone,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'person_id':'person', 'phone_id':'phone'},
            'bulk' : True
            },
        'person_e_mail' : {
            'csv_name' : '10_person_e_mail.csv',
            'fk_dict' : {'state_change_user':User, 'person':Person, 'e_mail':E_Mail},
            'model' : Person_E_Mail,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'person_id':'person', 'e_mail_id':'e_mail'},
            'bulk' : True
            },
        'person_legal_person_natural' : {
            'csv_name' : '11_person_legal_person_natural.csv',
            'fk_dict' : {'state_change_user':User, 'person_legal':Person_Legal, 'person_natural':Person_Natural},
            'model' : Person_Legal_Person_Natural,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'person_legal_id':'person_legal', 'person_natural_id':'person_natural'},
            'bulk' : False
            },
        'estate' : {
            'csv_name' : '12_estate.csv',
            'fk_dict' : {'state_change_user':User, 'address':Address},
            'model' : Estate,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'address_id':'address'},
            'bulk' : True
            },
        'estate_person' : {
            'csv_name' : '13_estate_person.csv',
            'fk_dict' : {'state_change_user':User, 'estate':Estate, 'person':Person},
            'model' : Estate_Person,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'estate_id':'estate', 'person_id':'person'},
            'bulk' : True
            },
        'estate_appraisal' : {
            'csv_name' : '14_estate_appraisal.csv',
            'fk_dict' : {'state_change_user':User, 'estate':Estate},
            'model' : Estate_Appraisal,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'estate_id':'estate'},
            'bulk' : True
            },
        'realty' : {
            'csv_name' : '15_realty.csv',
            'fk_dict' : {'state_change_user':User, 'address':Address},
            'model' : Realty,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'address_id':'address'},
            'bulk' : True
            },
        'realty_estate' : {
            'csv_name' : '16_realty_estate.csv',
            'fk_dict' : {'state_change_user':User, 'realty':Realty, 'estate':Estate},
            'model' : Realty_Estate,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'realty_id':'realty', 'estate_id':'estate'},
            'bulk' : True
            },
        'lease_realty' : {
            'csv_name' : '17_lease_realty.csv',
            'fk_dict' : {'state_change_user':User, 'subclass':ContentType},
            'model' : Lease_Realty,
            'to_drop' : ['Unnamed: 0', 'state_change_date', 'accountable_ptr_id'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'subclass_id':'subclass'},
            'bulk' : False
            },
        'lease_realty_realty' : {
            'csv_name' : '18_lease_realty_realty.csv',
            'fk_dict' : {'state_change_user':User, 'lease':Lease_Realty, 'realty':Realty},
            'model' : Lease_Realty_Realty,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'lease_id':'lease', 'realty_id':'realty'},
            'bulk' : True
            },
        'lease_realty_person' : {
            'csv_name' : '19_lease_realty_person.csv',
            'fk_dict' : {'state_change_user':User, 'lease':Lease_Realty, 'person':Person, 'phone':Phone, 'e_mail':E_Mail, 'address':Address},
            'model' : Lease_Realty_Person,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'lease_id':'lease', 'person_id':'person', 'phone_id':'phone', 'e_mail_id':'e_mail', 'address_id':'address'},
            'bulk' : True
            },
        'date_value' : {
            'csv_name' : '20_date_value.csv',
            'fk_dict' : {'state_change_user':User, 'accountable':Accountable},
            'model' : Date_Value,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'accountable_id':'accountable'},
            'bulk' : True
            }
        }

def data_load(load_info, load_list=None):
    counter = 0
    timers = { counter:datetime.now() }
    if load_list:
        for element in load_list:
            model_load(load_info[element])
            counter = counter + 1
            timers[counter] = datetime.now()
            print(f"{element} : {timers[counter] - timers[counter - 1]}")
    else:
        for value in load_info.values():
            model_load(value)
            counter = counter + 1
            timers[counter] = datetime.now()
            print(f"{element} : {timers[counter] - timers[counter - 1]}")
    
def model_load(load_dict):
    df_from_csv = pd.read_csv(join(BASE_DIR, f"_files/exports/{load_dict['csv_name']}"), keep_default_na=False)\
        .drop(load_dict['to_drop'], axis=1)\
        .rename(columns=load_dict['to_rename'])
    data_dict = df_from_csv\
        .assign(**{column: df_from_csv[column].apply(lambda x: None if x == '' else x) for column in df_from_csv.columns})\
        .assign(**{column: df_from_csv[column].apply(lambda x: None if x == '' else model.objects.get(pk=x)) for column, model in load_dict['fk_dict'].items()})\
        .assign(state=df_from_csv.state.apply(lambda x: 2))\
        .to_dict('index')
    if load_dict['bulk']:
        load_dict['model'].objects.bulk_create([load_dict['model'](**data) for data in data_dict.values()])
    else:
        for data in data_dict.values():
            load_dict['model'](**data).save()