import pandas as pd
from scripts.utils import df2objs

info_df = pd.read_json('_files/_raw_data_info.json')

def run():
    df2objs(pd.read_csv('_files/ledger_types_raw.csv'), info_df, True)
