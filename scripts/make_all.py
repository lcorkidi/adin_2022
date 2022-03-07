import pandas as pd
from datetime import datetime
from scripts.utils import address2code, df2objs, personcompletename

_raw_data_info = pd.read_json('_files/_raw_data_info.json')

def run():
    dt1 = datetime.now()

    # create addresses
    objs = df2objs(pd.read_csv('_files/addresses_raw.csv'), _raw_data_info)
    for obj in objs:
        obj.code = address2code(obj)
        obj.save()
    dt2 = datetime.now()
    print('Addresses: {}'.format(dt2-dt1))

    # create puc
    df2objs(pd.read_csv('_files/puc_raw.csv'), _raw_data_info, True)
    dt3 = datetime.now()
    print('PUC: {}'.format(dt3-dt2))

    # create people
    objs = df2objs(pd.read_csv('_files/people_raw.csv'), _raw_data_info)
    for obj in objs:
        obj.code = personcompletename(obj)
        obj.save()
    dt4 = datetime.now()
    print('People: {}'.format(dt4-dt3))

    # create estates
    df2objs(pd.read_csv('_files/estates_raw.csv'), _raw_data_info, True)
    dt5 = datetime.now()
    print('Estates: {}'.format(dt5-dt4))

    # create estates_people
    df2objs(pd.read_csv('_files/estates_people_raw.csv'), _raw_data_info, True)
    dt6 = datetime.now()
    print('Estates_People: {}'.format(dt6-dt5))

    # create appraisals
    df2objs(pd.read_csv('_files/appraisals_raw.csv'), _raw_data_info, True)
    dt7 = datetime.now()
    print('Appraisals: {}'.format(dt7-dt6))

    # create realties
    df2objs(pd.read_csv('_files/realties_raw.csv'), _raw_data_info, True)
    dt8 = datetime.now()
    print('Realties: {}'.format(dt8-dt7))

    # create realties_estates
    df2objs(pd.read_csv('_files/realties_estates_raw.csv'), _raw_data_info, True)
    dt9 = datetime.now()
    print('Realties_Estates: {}'.format(dt9-dt8))
    print('Total: {}'.format(dt9-dt1))
