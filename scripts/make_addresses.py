import pandas as pd
from references.models import Address
from scripts.utils import AddressToCode

data_df = pd.read_csv('_files/address_raw.csv')

def run():
    for index, row in data_df.iterrows():
        add = Address()
        for attr in data_df:
            if row[attr] not in [-9999, 'ZZZZZ']:
                setattr(add, attr, row[attr])
        add.code = AddressToCode(add)
        add.save()
