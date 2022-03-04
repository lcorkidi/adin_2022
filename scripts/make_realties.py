import pandas as pd
from properties.models import Realty
from references.models import Address

data_df = pd.read_csv('_files/realties_raw.csv')

def run():
    for index, row in data_df.iterrows():
        rea = Realty()
        for attr in data_df:
            if row[attr] not in [-9999, 'ZZZZZ']:
                if attr == 'address':
                    setattr(rea, attr, Address.objects.get(pk=row[attr]))                
                else:
                    setattr(rea, attr, row[attr])
        rea.save()