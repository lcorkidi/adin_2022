import pandas as pd

from people.models import Person_Natural, Person_Legal, Person_E_Mail, Person_Address, Person_Phone, Person_Legal_Person_Natural
from references.models import Address, E_Mail, Phone, Transaction_Type
from properties.models import Estate, Estate_Person, Realty, Realty_Estate, Estate_Appraisal
from accounting.models import Account, Ledger, Ledger_Type, Charge, Charge_Concept
from accountables.models import Lease_Realty, Lease_Realty_Realty, Lease_Realty_Person, Date_Value

def run():
    pd.DataFrame(Address.objects.all().values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)\
        .to_csv('_files/exports/address_export.csv')

    pd.DataFrame(E_Mail.objects.all().values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)\
        .to_csv('_files/exports/e_mail_export.csv')

    pd.DataFrame(Phone.objects.all().values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)\
        .to_csv('_files/exports/phone_export.csv')

    pd.DataFrame(Transaction_Type.objects.all().values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)\
        .to_csv('_files/exports/transaction_type_export.csv')

    pd.DataFrame(Person_Natural.objects.all().values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)\
        .to_csv('_files/exports/person_natural_export.csv')

    pd.DataFrame(Person_Legal.objects.all().values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)\
        .to_csv('_files/exports/person_legal_export.csv')

    pd.DataFrame(Person_E_Mail.objects.all().values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)\
        .to_csv('_files/exports/person_e_mail_export.csv')

    pd.DataFrame(Person_Address.objects.all().values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)\
        .to_csv('_files/exports/person_address_export.csv')

    pd.DataFrame(Person_Phone.objects.all().values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)\
        .to_csv('_files/exports/person_phone_export.csv')

    # pd.DataFrame(Person_Legal_Person_Natural.objects.all().values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)\
    #     .to_csv('_files/exports/person_legal_person_natural_export.csv')

    pd.DataFrame(Estate.objects.all().values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)\
        .to_csv('_files/exports/estate_export.csv')

    pd.DataFrame(Estate_Person.objects.all().values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)\
        .to_csv('_files/exports/estate_person_export.csv')

    pd.DataFrame(Estate_Appraisal.objects.all().values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)\
        .to_csv('_files/exports/estaet_appraisal_export.csv')

    pd.DataFrame(Realty.objects.all().values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)\
        .to_csv('_files/exports/realty_export.csv')

    pd.DataFrame(Realty_Estate.objects.all().values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)\
        .to_csv('_files/exports/realty_estate_export.csv')

    pd.DataFrame(Account.objects.all().values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)\
        .to_csv('_files/exports/account_export.csv')

    pd.DataFrame(Ledger.objects.all().values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)\
        .to_csv('_files/exports/ledger_export.csv')

    pd.DataFrame(Ledger_Type.objects.all().values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)\
        .to_csv('_files/exports/ledger_type_export.csv')

    pd.DataFrame(Charge.objects.all().values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)\
        .to_csv('_files/exports/charge_export.csv')

    pd.DataFrame(Charge_Concept.objects.all().values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)\
        .to_csv('_files/exports/charge_concept_export.csv')

    pd.DataFrame(Lease_Realty.objects.all().values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)\
        .to_csv('_files/exports/lease_realty_export.csv')

    pd.DataFrame(Lease_Realty_Realty.objects.all().values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)\
        .to_csv('_files/exports/lease_realty_realty_export.csv')

    pd.DataFrame(Lease_Realty_Person.objects.all().values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)\
        .to_csv('_files/exports/lease_realty_person_export.csv')

    pd.DataFrame(Date_Value.objects.all().values()).drop(['state_change_user_id', 'state_change_date', 'state'], axis=1)\
        .to_csv('_files/exports/date_value_export.csv')
