import pandas as pd
from django.contrib.auth import get_user_model
from scripts.utils import df2objs

data_df = pd.read_csv('_files/people_addresses_raw.csv')
info_df = pd.read_json('_files/_raw_data_info.json')

def run():
    df2objs(data_df, info_df, True)
