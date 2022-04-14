import pandas as pd
from scripts.utils import df2objs

data_df = pd.read_csv('_files/estates_raw.csv')
info_df = pd.read_json('_files/_raw_data_info.json')

def run():
    df2objs(data_df, info_df, True)
