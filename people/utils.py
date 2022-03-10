
def personcompletename(person):
    if person.type == 0:
        return f'{person.last_name}, {person.name}'
    elif person.type == 1:
        return f'{person.name} {person.get_legal_type_display()}'

def person_natural_m2m_data(*args):
    from .models import Person_Phone, Person_E_Mail, Person_Address
    from .forms import Person_PhoneModelFormSet, Person_EmailModelFormSet, Person_AddressModelFormSet
    
    m2m_data = {
        'phone': {
            'class': Person_Phone,
            'formset': Person_PhoneModelFormSet,
            'filter_expresion': 'person__id_number',
            'omit_field' : 'person',
            'create_url': 'people:people_phone_create',
            'update_url': 'people:people_phone_update',
            'delete_url': 'people:people_phone_delete'
        },
        'e_mail': {
            'class': Person_E_Mail,
            'formset': Person_EmailModelFormSet,
            'filter_expresion': 'person__id_number',
            'omit_field' : 'person',
            'create_url': 'people:people_email_create',
            'update_url': 'people:people_email_update',
            'delete_url': 'people:people_email_delete'
        },
        'address': {
            'class': Person_Address,
            'formset': Person_AddressModelFormSet,
            'filter_expresion': 'person__id_number',
            'omit_field' : 'person',
            'create_url': 'people:people_address_create',
            'update_url': 'people:people_address_update',
            'delete_url': 'people:people_address_delete'
        }      
    }
    return m2m_data

def person_legal_m2m_data(*args):

    from .models import Person_Legal_Person_Natural
    from .forms import Person_Legal_Person_NaturalModelFormSet

    m2m_data = person_natural_m2m_data()
    m2m_data['staff'] = {
        'class': Person_Legal_Person_Natural,
        'formset': Person_Legal_Person_NaturalModelFormSet,
        'filter_expresion': 'person__id_number',
        'omit_field' : 'person',
        'create_url': 'people:people_staff_create',
        'update_url': 'people:people_staff_update',
        'delete_url': 'people:people_staff_delete'
    }        
    return m2m_data

