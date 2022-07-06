import pandas as pd
from os.path import join
from adin.settings import BASE_DIR
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from people.models import Person, Person_Natural, Person_Legal, Person_E_Mail, Person_Address, Person_Phone
from people.models.person import Person_Legal_Person_Natural
from references.models import Address, PUC, E_Mail, Phone, Charge_Factor, Factor_Data, Calendar_Date
from properties.models import Estate, Estate_Person, Realty, Realty_Estate, Estate_Appraisal
from accountables.models import Accountable, Accountable_Transaction_Type, Accountable_Concept, Lease_Realty, Lease_Realty_Realty, Lease_Realty_Person, Date_Value
from accounting.models import Account, Ledger, Ledger_Type, Ledger_Template, Charge, Charge_Template
    
load_lists = {
        'all': [
            'puc',
            'calendar_date', 
            'charge_factor', 
            'factor_data', 
            'address', 
            'phone', 
            'e_mail',
            'person_natural', 
            'person_legal', 
            'person_address', 
            'person_phone', 
            'person_e_mail',
            'estate', 
            'estate_person', 
            'estate_appraisal', 
            'realty', 
            'realty_estate',
            'lease_realty', 
            'lease_realty_realty', 
            'lease_realty_person', 
            'date_value',
            'accountable_transaction_type'
        ],
        'references': [
            'puc', 
            'calendar_date', 
            'charge_factor', 
            'factor_data', 
            'address', 
            'phone', 
            'e_mail'
        ],
        'people': [
            'person_natural', 
            'person_legal', 
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
            'account', 
            'ledger_type', 
            'ledger_template', 
            'charge_template', 
            'ledger', 
            'charge'
        ],
        'no-registers': [
            'puc', 
            'calendar_date', 
            'charge_factor', 
            'factor_data', 
            'address', 
            'phone', 
            'e_mail', 
            'person_natural', 
            'person_legal', 
            'person_address', 
            'person_phone', 
            'person_e_mail', 
            'estate', 
            'estate_person', 
            'estate_appraisal', 
            'realty', 
            'realty_estate', 
            'lease_realty', 
            'lease_realty_realty', 
            'lease_realty_person', 
            'date_value', 
            'accountable_transaction_type',
            'account', 
            'ledger_type', 
            'ledger_template', 
            'charge_template'
        ],
        'registers': [
            'charge_concept', 
            'ledger', 
            'charge'
        ],
        'temp': [
            'puc', 
            'calendar_date', 
            'charge_factor', 
            'factor_data', 
            'address', 
            'phone', 
            'e_mail'
            'person_address', 
            'person_phone', 
            'person_e_mail', 
            'estate', 
            'estate_person', 
            'estate_appraisal', 
            'realty', 
            'realty_estate', 
            'lease_realty', 
            'lease_realty_realty', 
            'lease_realty_person', 
            'date_value', 
            'accountable_transaction_type',
        ]
    }

load_info = { 
        'puc' : {
            'csv_name' : 'puc.csv',
            'fk_dict' : {'state_change_user': User},
            'model' : PUC,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user'},
            'bulk' : True,
            'pending_relations' : None
            },
        'calendar_date' : {
            'csv_name' : 'calendar_date.csv',
            'fk_dict' : {'state_change_user':User},
            'model' : Calendar_Date,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user'},
            'bulk' : True,
            'pending_relations' : None
            },
        'charge_factor' : {
            'csv_name' : 'charge_factor.csv',
            'fk_dict' : {'state_change_user':User},
            'model' : Charge_Factor,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user'},
            'bulk' : True,
            'pending_relations' : None
            },
        'factor_data' : {
            'csv_name' : 'factor_data.csv',
            'fk_dict' : {'state_change_user':User, 'factor':Charge_Factor},
            'model' : Factor_Data,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user'},
            'bulk' : True,
            'pending_relations' : None
            },
        'address' : {
            'csv_name' : 'address.csv',
            'fk_dict' : {'state_change_user':User},
            'model' : Address,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user'},
            'bulk' : True,
            'pending_relations' : None
            },
        'phone' : {
            'csv_name' : 'phone.csv',
            'fk_dict' : {'state_change_user':User},
            'model' : Phone,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user'},
            'bulk' : True,
            'pending_relations' : None
            },
        'e_mail' : {
            'csv_name' : 'e_mail.csv',
            'fk_dict' : {'state_change_user':User},
            'model' : E_Mail,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user'},
            'bulk' : True,
            'pending_relations' : None
            },
        'person_natural' : {
            'csv_name' : 'person_natural.csv',
            'fk_dict' : {'state_change_user':User},
            'model' : Person_Natural,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user'},
            'bulk' : False,
            'pending_relations' : None
            },
        'person_legal' : {
            'csv_name' : 'person_legal.csv',
            'fk_dict' : {'state_change_user':User},
            'model' : Person_Legal,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user'},
            'bulk' : False,
            'pending_relations' : None
            },
        'person_address' : {
            'csv_name' : 'person_address.csv',
            'fk_dict' : {'state_change_user':User, 'person':Person, 'address':Address},
            'model' : Person_Address,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'person_id':'person', 'address_id':'address'},
            'bulk' : True,
            'pending_relations' : None
            },
        'person_phone' : {
            'csv_name' : 'person_phone.csv',
            'fk_dict' : {'state_change_user':User, 'person':Person, 'phone':Phone},
            'model' : Person_Phone,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'person_id':'person', 'phone_id':'phone'},
            'bulk' : True,
            'pending_relations' : None
            },
        'person_e_mail' : {
            'csv_name' : 'person_e_mail.csv',
            'fk_dict' : {'state_change_user':User, 'person':Person, 'e_mail':E_Mail},
            'model' : Person_E_Mail,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'person_id':'person', 'e_mail_id':'e_mail'},
            'bulk' : True,
            'pending_relations' : None
            },
        'person_legal_person_natural' : {
            'csv_name' : 'person_legal_person_natural.csv',
            'fk_dict' : {'state_change_user':User, 'person_legal':Person_Legal, 'person_natural':Person_Natural},
            'model' : Person_Legal_Person_Natural,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'person_legal_id':'person_legal', 'person_natural_id':'person_natural'},
            'bulk' : False,
            'pending_relations' : None
            },
        'estate' : {
            'csv_name' : 'estate.csv',
            'fk_dict' : {'state_change_user':User, 'address':Address},
            'model' : Estate,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'address_id':'address'},
            'bulk' : True,
            'pending_relations' : None
            },
        'estate_person' : {
            'csv_name' : 'estate_person.csv',
            'fk_dict' : {'state_change_user':User, 'estate':Estate, 'person':Person},
            'model' : Estate_Person,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'estate_id':'estate', 'person_id':'person'},
            'bulk' : True,
            'pending_relations' : None
            },
        'estate_appraisal' : {
            'csv_name' : 'estate_appraisal.csv',
            'fk_dict' : {'state_change_user':User, 'estate':Estate},
            'model' : Estate_Appraisal,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'estate_id':'estate'},
            'bulk' : True,
            'pending_relations' : None
            },
        'realty' : {
            'csv_name' : 'realty.csv',
            'fk_dict' : {'state_change_user':User, 'address':Address},
            'model' : Realty,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'address_id':'address'},
            'bulk' : True,
            'pending_relations' : None
            },
        'realty_estate' : {
            'csv_name' : 'realty_estate.csv',
            'fk_dict' : {'state_change_user':User, 'realty':Realty, 'estate':Estate},
            'model' : Realty_Estate,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'realty_id':'realty', 'estate_id':'estate'},
            'bulk' : True,
            'pending_relations' : None
            },
        'lease_realty' : {
            'csv_name' : 'lease_realty.csv',
            'fk_dict' : {'state_change_user':User, 'subclass':ContentType},
            'model' : Lease_Realty,
            'to_drop' : ['Unnamed: 0', 'state_change_date', 'accountable_ptr_id'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'subclass_id':'subclass'},
            'bulk' : False,
            'pending_relations' : None
            },
        'lease_realty_realty' : {
            'csv_name' : 'lease_realty_realty.csv',
            'fk_dict' : {'state_change_user':User, 'lease':Lease_Realty, 'realty':Realty},
            'model' : Lease_Realty_Realty,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'lease_id':'lease', 'realty_id':'realty'},
            'bulk' : True,
            'pending_relations' : None
            },
        'lease_realty_person' : {
            'csv_name' : 'lease_realty_person.csv',
            'fk_dict' : {'state_change_user':User, 'lease':Lease_Realty, 'person':Person, 'phone':Phone, 'e_mail':E_Mail, 'address':Address},
            'model' : Lease_Realty_Person,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'lease_id':'lease', 'person_id':'person', 'phone_id':'phone', 'e_mail_id':'e_mail', 'address_id':'address'},
            'bulk' : True,
            'pending_relations' : None
            },
        'date_value' : {
            'csv_name' : 'date_value.csv',
            'fk_dict' : {'state_change_user':User, 'accountable':Accountable},
            'model' : Date_Value,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user', 'accountable_id':'accountable'},
            'bulk' : True,
            'pending_relations' : None
            },
        'accountable_transaction_type' : {
            'csv_name' : 'accountable_transaction_type.csv',
            'fk_dict' : {'state_change_user':User},
            'model' : Accountable_Transaction_Type,
            'to_drop' : ['Unnamed: 0', 'state_change_date'],
            'to_rename' : {'state_change_user_id':'state_change_user'},
            'bulk' : True,
            'pending_relations' : ['accountable_transaction_type']
            }
        }

m2m_info = {
    'accountable_transaction_type' : {
            'csv_name' : 'm2m_accountable_transaction_type.csv',
            'm2m_field' : 'transaction_types',
            'field_obj_column' : 'accountable',
            'field_obj_model' : Accountable,
            'non_field_obj_column' : 'accountable_transaction_type',
            'non_field_obj_model' : Accountable_Transaction_Type
    }
}

def data_load(load_info, load_list=None):
    counter = 0
    timers = { counter:datetime.now() }
    if not load_list:
        load_list = load_lists['all']
    for element in load_list:
        model_load(load_info[element])
        counter = counter + 1
        timers[counter] = datetime.now()
        print(f"{element} : {timers[counter] - timers[counter - 1]}")
    
def model_load(load_dict, csv_file=None):
    df_from_csv = pd.read_csv(csv_file if csv_file else join(BASE_DIR, f"_files/{load_dict['csv_name']}"), keep_default_na=False)\
        .drop(load_dict['to_drop'], axis=1)\
        .rename(columns=load_dict['to_rename'])
    data_dict = df_from_csv\
        .assign(**{column: df_from_csv[column].apply(lambda x: None if x == '' else x) for column in df_from_csv.columns})\
        .assign(**{column: df_from_csv[column].apply(lambda x: None if x == '' else model.objects.get(pk=x)) for column, model in load_dict['fk_dict'].items()})\
        .to_dict('index')
    if load_dict['bulk']:
        load_dict['model'].objects.bulk_create([load_dict['model'](**data) for data in data_dict.values()])
    else:
        for data in data_dict.values():
            load_dict['model'](**data).save()
    if load_dict['pending_relations']:
        for relation in load_dict['pending_relations']:
            m2m_load(m2m_info[relation])

def m2m_load(load_dict):
    df_from_csv = pd.read_csv(join(BASE_DIR, f"_files/{load_dict['csv_name']}"), keep_default_na=False)
    df_from_csv.assign(**{load_dict['field_obj_column']:df_from_csv[load_dict['field_obj_column']].apply(lambda x: load_dict['field_obj_model'].objects.get(pk=x))})\
        .apply(lambda x: eval(f"x[load_dict['field_obj_column']].{load_dict['m2m_field']}.add(load_dict['non_field_obj_model'].objects.get(pk=x[load_dict['non_field_obj_column']]))"), axis=1)

