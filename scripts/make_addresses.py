import pandas as pd
from references.models import Address

data_df = pd.read_csv('_files/address_raw.csv')


def run():
    for index, row in data_df.iterrows():
        add = Address()
        for attr in data_df:
            if pd.notna(row[attr]):
                setattr(add, attr, row[attr])
        add.save()
