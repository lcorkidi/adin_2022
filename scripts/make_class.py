import pandas as pd
from datetime import datetime
from scripts.utils import df2objs

info_df = pd.read_json('_files/_raw_data_info.json')

def run(class_name):
    dt0 = datetime.now()
    df2objs(pd.read_csv(f'_files/{class_name}.csv'), info_df, True)
    dt1 = datetime.now()

    print(f'time: {dt1 - dt0}')
