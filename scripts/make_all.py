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

    # create realties_estates
    df2objs(pd.read_csv('_files/accounts_raw.csv'), _raw_data_info, True)
    dt15 = datetime.now()
    print('Realties_Estates: {}'.format(dt15-dt14))

    # create realties_estates
    df2objs(pd.read_csv('_files/leases_realties_raw.csv'), _raw_data_info, True)
    dt16 = datetime.now()
    print('Realties_Estates: {}'.format(dt16-dt15))

    # create realties_estates
    df2objs(pd.read_csv('_files/leases_realties_realties_raw.csv'), _raw_data_info, True)
    dt17 = datetime.now()
    print('Realties_Estates: {}'.format(dt17-dt16))

    # create realties_estates
    df2objs(pd.read_csv('_files/leases_realties_people_raw.csv'), _raw_data_info, True)
    dt18 = datetime.now()
    print('Realties_Estates: {}'.format(dt18-dt17))
    print('Total: {}'.format(dt18-dt1))
