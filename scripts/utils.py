from django.contrib.auth import get_user_model

from people.models import Person, Person_Natural, Person_Legal, Person_E_Mail, Person_Address, Person_Phone
from references.models import Address, PUC, E_Mail, Phone
from properties.models import Estate, Estate_Person, Realty, Realty_Estate, Estate_Appraisal

def df2objs(dr, rdi, save=False):
    user = get_user_model().objects.all()[0]
    objs = []
    for index, row in dr.iterrows():
        obj = eval(f"{row['class']}()")
        for attr in rdi.loc['data_attrs', row['class']]:
            if row[attr] not in [-9999, 'ZZZZZ']:
                setattr(obj, attr, row[attr])
        for attr in rdi.loc['fk_attrs', row['class']]:
            if row[attr.lower()] not in [-9999, 'ZZZZZ']:
                setattr(obj, attr.lower(), eval(f"{attr}.objects.get(pk='{row[attr.lower()]}')"))
        obj.state_change_user = user
        if save: obj.save()
        objs.append(obj)
        for attr in rdi.loc['attrs_2_relate', row['class']]:
            eval(f"{attr[0]}.objects.get(pk='{row[attr[0].lower()]}').{attr[1]}.add(obj)")
    return objs
