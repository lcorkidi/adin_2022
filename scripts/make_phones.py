import pandas as pd
from scripts.utils import phone2code, df2objs

data_df = pd.read_csv('_files/phones_raw.csv')
info_df = pd.read_json('_files/_raw_data_info.json')

def run():
    objs = df2objs(data_df, info_df)
    for obj in objs:
        obj.code = phone2code(obj)
        obj.save()
