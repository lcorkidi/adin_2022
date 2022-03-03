import pandas as pd
from people.models import Person_Natural, Person_Legal

data_df = pd.read_csv('_files/people_raw.csv')
info_df = pd.read_json('_files/people_info.json')

def run():
    for index, row in data_df.iterrows():
        per = eval(f"{info_df.loc['class', row['type']]}()")
        for attr in info_df.loc['include', row['type']]:
            setattr(per, attr, row[attr])
        per.save()
