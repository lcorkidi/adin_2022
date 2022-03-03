import pandas as pd
from properties.models import Estate, Estate_Person
from people.models import Person

data_df = pd.read_csv('_files/estate_person_raw.csv')

def run():
    for index, row in data_df.iterrows():
        est_per = Estate_Person()
        for attr in data_df:
            if row[attr] not in [-9999, 'ZZZZZ']:
                if attr == 'estate':
                    setattr(est_per, attr, Estate.objects.get(pk=row[attr]))
                elif attr == 'person':
                    setattr(est_per, attr, Person.objects.get(pk=row[attr]))
                else:
                    setattr(est_per, attr, row[attr])
        est_per.save()
