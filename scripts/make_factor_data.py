import pandas as pd
from scripts.utils import df2objs

_raw_data_info = pd.read_json('_files/_raw_data_info.json')

def run():
    df2objs(pd.read_csv('_files/factor_data.csv'), _raw_data_info, True)
