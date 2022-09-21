def phone2code(phone):
    return f'+{phone.country}{" " + str(phone.region) if phone.region != None else ""} {phone.number}'

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
        25: 'Z',
        26: 'A1',
        27: 'B1'
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
        10: 'S',
        11: 'I'
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
    if address.numeral_bis:
        code += 'b'
        if address.numeral_bis_complement:
            code += LETTER_CHOICE[address.numeral_bis_complement].lower()
    if address.numeral_coordinate != None:
        code += COORDINATE_CHOICE[address.numeral_coordinate]
    code += f'-{str(address.height_number)}'
    if address.interior_type != None:
        code += '-'
    if address.interior_group_type != None:
        code += INTERIOR_GROUP_TYPE_CHOICE[address.interior_group_type]
        code += str(address.interior_group_code)
    if address.interior_type != None:
        code += INTERIOR_TYPE_CHOICE[address.interior_type]
        code += str(address.interior_code)

    return code

def addresslong(address):

    code = address.get_street_type_display()
    code += " " + str(address.street_number)
    if address.street_letter != None:
        code += address.get_street_letter_display()
    if address.street_bis:
        code += 'bis'
        if address.street_bis_complement:
            code += address.get_street_bis_complement_display()
    if address.street_coordinate != None:
        code += " " + address.get_street_coordinate_display()
    code += " # " + str(address.numeral_number)
    if address.numeral_letter != None:
        code += address.get_numeral_letter_display()
    if address.numeral_bis:
        code += 'bis'
        if address.numeral_bis_complement:
            code += address.get_numeral_bis_complement_display()
    if address.numeral_coordinate != None:
        code += " " + address.get_numeral_coordinate_display()
    code += " - " + str(address.height_number)
    if address.interior_type != None:
        code += ', '
    if address.interior_group_type != None:
        code += address.get_interior_group_type_display()
        code += " " + str(address.interior_group_code) + ", "
    if address.interior_type != None:
        code += address.get_interior_type_display()
        code += " " + str(address.interior_code)
    code += ", " + address.city

    return code
