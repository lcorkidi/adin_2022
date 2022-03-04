import pandas as pd
from properties.models import Realty, Realty_Estate, Estate

data_df = pd.read_csv('_files/realties_estates_raw.csv')

def run():
    for index, row in data_df.iterrows():
        rea_est = Realty_Estate()
        for attr in data_df:
            if row[attr] not in [-9999, 'ZZZZZ']:
                if attr == 'realty':
                    setattr(rea_est, attr, Realty.objects.get(pk=row[attr]))                
                elif attr == 'estate':
                    setattr(rea_est, attr, Estate.objects.get(pk=row[attr]))                
                else:
                    setattr(rea_est, attr, row[attr])
        rea_est.save()