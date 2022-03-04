import pandas as pd
from scripts.utils import address2code, df2objs

_raw_data_info = pd.read_json('_files/_raw_data_info.json')

def run():
    # create people
    df2objs(pd.read_csv('_files/people_raw.csv'), _raw_data_info, True)

    # create addresses
    objs = df2objs(pd.read_csv('_files/addresses_raw.csv'), _raw_data_info)
    for obj in objs:
        obj.code = address2code(obj)
        obj.save()

    # create estates
    df2objs(pd.read_csv('_files/estates_raw.csv'), _raw_data_info, True)

    # create estates_people
    df2objs(pd.read_csv('_files/estates_people_raw.csv'), _raw_data_info, True)

    # create appraisals
    df2objs(pd.read_csv('_files/appraisals_raw.csv'), _raw_data_info, True)

    # create realties
    df2objs(pd.read_csv('_files/realties_raw.csv'), _raw_data_info, True)

    # create realties_estates
    df2objs(pd.read_csv('_files/realties_estates_raw.csv'), _raw_data_info, True)
