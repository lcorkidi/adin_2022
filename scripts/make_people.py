import pandas as pd
from scripts.utils import df2objs, personcompletename

data_df = pd.read_csv('_files/people_raw.csv')
info_df = pd.read_json('_files/_raw_data_info.json')

def run():
    objs = df2objs(data_df, info_df)
    for obj in objs:
        obj.complete_name = personcompletename(obj)
        obj.save()
