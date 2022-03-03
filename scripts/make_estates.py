import pandas as pd
from properties.models import Estate
from references.models import Address

data_df = pd.read_csv('_files/estate_raw.csv')

def run():
    for index, row in data_df.iterrows():
        est = Estate()
        for attr in data_df:
            if row[attr] not in [-9999, 'ZZZZZ']:
                if attr == 'address':
                    setattr(est, attr, Address.objects.get(pk=row[attr]))                
                else:
                    setattr(est, attr, row[attr])
        est.save()