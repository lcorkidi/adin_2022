import pandas as pd
from references.models import Appraisal
from properties.models import Estate

data_df = pd.read_csv('_files/appraisal_raw.csv')

def run():
    for index, row in data_df.iterrows():
        app = Appraisal()
        for attr in data_df:
            if row[attr] not in [-9999, 'ZZZZZ']:
                if attr == 'estate':
                    est = Estate.objects.get(pk=row[attr])
                else:
                    setattr(app, attr, row[attr])
        app.save()
        est.appraisal.add(app)