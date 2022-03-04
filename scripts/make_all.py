import pandas as pd
from scripts.utils import AddressToCode
from people.models import Person, Person_Natural, Person_Legal
from references.models import Address, Appraisal
from properties.models import Estate, Estate_Person, Realty, Realty_Estate

people_df = pd.read_csv('_files/people_raw.csv')
people_info_df = pd.read_json('_files/people_info.json')
addresses_df = pd.read_csv('_files/address_raw.csv')
estates_df = pd.read_csv('_files/estate_raw.csv')
estates_people_data_df = pd.read_csv('_files/estate_person_raw.csv')
appraisal_df = pd.read_csv('_files/appraisal_raw.csv')
realties_df = pd.read_csv('_files/realties_raw.csv')
realties_estates_df = pd.read_csv('_files/realties_estates_raw.csv')

def run():
    # create people
    for index, row in people_df.iterrows():
        per = eval(f"{people_info_df.loc['class', row['type']]}()")
        for attr in people_info_df.loc['include', row['type']]:
            setattr(per, attr, row[attr])
        per.save()

    # create addresses
    for index, row in addresses_df.iterrows():
        add = Address()
        for attr in addresses_df:
            if row[attr] not in [-9999, 'ZZZZZ']:
                setattr(add, attr, row[attr])
        add.code = AddressToCode(add)
        add.save()

    # create estates
    for index, row in estates_df.iterrows():
        est = Estate()
        for attr in estates_df:
            if row[attr] not in [-9999, 'ZZZZZ']:
                if attr == 'address':
                    setattr(est, attr, Address.objects.get(pk=row[attr]))                
                else:
                    setattr(est, attr, row[attr])
        est.save()

    # create estates_people
    for index, row in estates_people_data_df.iterrows():
        est_per = Estate_Person()
        for attr in estates_people_data_df:
            if row[attr] not in [-9999, 'ZZZZZ']:
                if attr == 'estate':
                    setattr(est_per, attr, Estate.objects.get(pk=row[attr]))
                elif attr == 'person':
                    setattr(est_per, attr, Person.objects.get(pk=row[attr]))
                else:
                    setattr(est_per, attr, row[attr])
        est_per.save()

    # create appraisals
    for index, row in appraisal_df.iterrows():
        app = Appraisal()
        for attr in appraisal_df:
            if row[attr] not in [-9999, 'ZZZZZ']:
                if attr == 'estate':
                    est = Estate.objects.get(pk=row[attr])
                else:
                    setattr(app, attr, row[attr])
        app.save()
        est.appraisal.add(app)

    # create realties
    for index, row in realties_estates_df.iterrows():
        rea = Realty()
        for attr in realties_estates_df:
            if row[attr] not in [-9999, 'ZZZZZ']:
                if attr == 'address':
                    setattr(rea, attr, Address.objects.get(pk=row[attr]))                
                else:
                    setattr(rea, attr, row[attr])
        rea.save()

    # create realties_estates
    for index, row in realties_estates_df.iterrows():
        rea_est = Realty_Estate()
        for attr in realties_estates_df:
            if row[attr] not in [-9999, 'ZZZZZ']:
                if attr == 'realty':
                    setattr(rea_est, attr, Realty.objects.get(pk=row[attr]))                
                elif attr == 'estate':
                    setattr(rea_est, attr, Estate.objects.get(pk=row[attr]))                
                else:
                    setattr(rea_est, attr, row[attr])
        rea_est.save()