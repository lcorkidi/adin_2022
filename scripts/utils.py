from people.models import Person, Person_Natural, Person_Legal
from references.models import Address, PUC
from properties.models import Estate, Estate_Person, Realty, Realty_Estate, Appraisal

def personcompletename(person):
    if person.type == 0:
        return f'{person.last_name}, {person.name}'
    elif person.type == 1:
        return f'{person.name} {person.get_legal_type_display()}'

def address2code(address):
    STREET_TYPE_CHOICE =  {
        0: 'A',
        1: 'C',
        2: 'K',
        3: 'D',
        4: 'T',
        5: 'V',
        6: 'L',
        7: 'U'
    }
    LETTER_CHOICE = {
        0: 'A',
        1: 'B',
        2: 'C',
        3: 'D',
        4: 'E',
        5: 'F',
        6: 'G',
        7: 'H',
        8: 'I',
        9: 'J',
        10: 'K',
        11: 'L',
        12: 'M',
        13: 'M',
        14: 'O',
        15: 'P',
        16: 'Q',
        17: 'R',
        18: 'S',
        19: 'T',
        20: 'U',
        21: 'V',
        22: 'W',
        23: 'X',
        24: 'Y',
        25: 'Z'
    }
    COORDINATE_CHOICE = {
        0: 'N',
        1: 'S',
        2: 'E',
        3: 'O',
        4: 'C'
    }
    INTERIOR_GROUP_TYPE_CHOICE = {
        0: 'B',
        1: 'T',
        2: 'E'
    }
    INTERIOR_TYPE_CHOICE = {
        0: 'A',
        1: 'L',
        2: 'O',
        3: 'B',
        4: 'P',
        5: 'D',
        6: 'I',
        7: 'C',
        8: 'T',
        9: 'F',
        10: 'S'
    }

    code = STREET_TYPE_CHOICE[address.street_type]
    code += str(address.street_number)
    if address.street_letter != None:
        code += LETTER_CHOICE[address.street_letter]
    if address.street_bis:
        code += 'b'
        if address.street_bis_complement:
            code += LETTER_CHOICE[address.street_bis_complement].lower()
    if address.street_coordinate != None:
        code += COORDINATE_CHOICE[address.street_coordinate]
    code += f'-{address.numeral_number}'
    if address.numeral_letter != None:
        code += LETTER_CHOICE[address.numeral_letter]
    if address.numeral_coordinate != None:
        code += COORDINATE_CHOICE[address.numeral_coordinate]
    code += f'-{str(address.height_number)}'
    if address.interior_type != None:
        code += '-'
    if address.interior_group_type != None:
        code += INTERIOR_GROUP_TYPE_CHOICE[address.interior_group_type]
        code += str(int(address.interior_group_code))
    if address.interior_type != None:
        code += INTERIOR_TYPE_CHOICE[address.interior_type]
        code += str(int(address.interior_code))

    return code

def df2objs(dr, rdi, save=False):
    objs = []
    for index, row in dr.iterrows():
        obj = eval(f"{row['class']}()")
        for attr in rdi.loc['data_attrs', row['class']]:
            if row[attr] not in [-9999, 'ZZZZZ']:
                setattr(obj, attr, row[attr])
        for attr in rdi.loc['fk_attrs', row['class']]:
            if row[attr.lower()] not in [-9999, 'ZZZZZ']:
                setattr(obj, attr.lower(), eval(f"{attr}.objects.get(pk='{row[attr.lower()]}')"))
        if save: obj.save()
        objs.append(obj)
        for attr in rdi.loc['attrs_2_relate', row['class']]:
            eval(f"{attr[0]}.objects.get(pk='{row[attr[0].lower()]}').{attr[1]}.add(obj)")
    return objs
