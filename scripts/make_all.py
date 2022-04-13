import pandas as pd
from datetime import datetime
from scripts.utils import df2objs

_raw_data_info = pd.read_json('_files/_raw_data_info.json')

def run():
    dt1 = datetime.now()

    # create addresses
    df2objs(pd.read_csv('_files/addresses_raw.csv'), _raw_data_info, True)
    dt2 = datetime.now()
    print('Addresses: {}'.format(dt2-dt1))

    # create puc
    df2objs(pd.read_csv('_files/puc_raw.csv'), _raw_data_info, True)
    dt3 = datetime.now()
    print('PUC: {}'.format(dt3-dt2))

    # create phones
    df2objs(pd.read_csv('_files/phones_raw.csv'), _raw_data_info, True)
    dt4 = datetime.now()
    print('Phones: {}'.format(dt4-dt3))

    # create emails
    df2objs(pd.read_csv('_files/emails_raw.csv'), _raw_data_info, True)
    dt5 = datetime.now()
    print('Emails: {}'.format(dt5-dt4))

    # create people
    df2objs(pd.read_csv('_files/people_raw.csv'), _raw_data_info, True)
    dt6 = datetime.now()
    print('People: {}'.format(dt6-dt5))

    # create people_phones
    df2objs(pd.read_csv('_files/people_phones_raw.csv'), _raw_data_info, True)
    dt7 = datetime.now()
    print('People_Phones: {}'.format(dt7-dt6))

    # create people_addresses
    df2objs(pd.read_csv('_files/people_addresses_raw.csv'), _raw_data_info, True)
    dt8 = datetime.now()
    print('People_Addresses: {}'.format(dt8-dt7))

    # create people_emails
    df2objs(pd.read_csv('_files/people_emails_raw.csv'), _raw_data_info, True)
    dt9 = datetime.now()
    print('People_Emails: {}'.format(dt9-dt8))

    # create estates
    df2objs(pd.read_csv('_files/estates_raw.csv'), _raw_data_info, True)
    dt10 = datetime.now()
    print('Estates: {}'.format(dt10-dt9))

    # create estates_people
    df2objs(pd.read_csv('_files/estates_people_raw.csv'), _raw_data_info, True)
    dt11 = datetime.now()
    print('Estates_People: {}'.format(dt11-dt10))

    # create estates_appraisals
    df2objs(pd.read_csv('_files/estates_appraisals_raw.csv'), _raw_data_info, True)
    dt12 = datetime.now()
    print('Appraisals: {}'.format(dt12-dt11))

    # create realties
    df2objs(pd.read_csv('_files/realties_raw.csv'), _raw_data_info, True)
    dt13 = datetime.now()
    print('Realties: {}'.format(dt13-dt12))

    # create realties_estates
    df2objs(pd.read_csv('_files/realties_estates_raw.csv'), _raw_data_info, True)
    dt14 = datetime.now()
    print('Realties_Estates: {}'.format(dt14-dt13))

    # create accounts
    df2objs(pd.read_csv('_files/accounts_raw.csv'), _raw_data_info, True)
    dt15 = datetime.now()
    print('Accounts: {}'.format(dt15-dt14))

    # create leases_realties
    df2objs(pd.read_csv('_files/leases_realties_raw.csv'), _raw_data_info, True)
    dt16 = datetime.now()
    print('Leases_Realties: {}'.format(dt16-dt15))

    # create leases_realties_realties
    df2objs(pd.read_csv('_files/leases_realties_realties_raw.csv'), _raw_data_info, True)
    dt17 = datetime.now()
    print('Leases_Realties_Realties: {}'.format(dt17-dt16))

    # create leases_realties_people
    df2objs(pd.read_csv('_files/leases_realties_people_raw.csv'), _raw_data_info, True)
    dt18 = datetime.now()
    print('Leases_Realties_People: {}'.format(dt18-dt17))

    # create dates_values
    df2objs(pd.read_csv('_files/dates_values_raw.csv'), _raw_data_info, True)
    dt19 = datetime.now()
    print('Dates_Values: {}'.format(dt19-dt18))

    # create transaction_types
    df2objs(pd.read_csv('_files/transaction_types_raw.csv'), _raw_data_info, True)
    dt20 = datetime.now()
    print('Transaction_Type: {}'.format(dt20-dt19))

    # create charges_concepts
    df2objs(pd.read_csv('_files/charges_concepts_raw.csv'), _raw_data_info, True)
    dt21 = datetime.now()
    print('Charge_Concept: {}'.format(dt21-dt20))

    # create ledger_types
    df2objs(pd.read_csv('_files/ledger_types_raw.csv'), _raw_data_info, True)
    dt22 = datetime.now()
    print('Ledger_Type: {}'.format(dt22-dt21))

    # create ledgers
    df2objs(pd.read_csv('_files/ledgers_raw.csv'), _raw_data_info, True)
    dt23 = datetime.now()
    print('Ledger: {}'.format(dt23-dt22))

    # create charges
    df2objs(pd.read_csv('_files/charges_raw.csv'), _raw_data_info, True)
    dt24 = datetime.now()
    print('Charge: {}'.format(dt24-dt23))

    # create charges factors
    df2objs(pd.read_csv('_files/charges_factors_raw.csv'), _raw_data_info, True)
    dt25 = datetime.now()
    print('Charge_Factor: {}'.format(dt25-dt24))

    # create factors data
    df2objs(pd.read_csv('_files/factors_data_raw.csv'), _raw_data_info, True)
    dt26 = datetime.now()
    print('Factor_Data: {}'.format(dt26-dt25))

    # create ledgers templates
    df2objs(pd.read_csv('_files/ledgers_templates_raw.csv'), _raw_data_info, True)
    dt27 = datetime.now()
    print('Ledger_Template: {}'.format(dt27-dt26))

    # create charges templates
    df2objs(pd.read_csv('_files/charges_templates_raw.csv'), _raw_data_info, True)
    dt28 = datetime.now()
    print('Charges_Templates: {}'.format(dt28-dt27))
    print('Total: {}'.format(dt28-dt1))
