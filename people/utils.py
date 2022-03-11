
def personcompletename(person):
    if person.type == 0:
        return f'{person.last_name}, {person.name}'
    elif person.type == 1:
        return f'{person.name} {person.get_legal_type_display()}'

def person_natural_m2m_data(*args):
    from .models import Person_Phone, Person_E_Mail, Person_Address
    from .forms.person_e_mail_forms import Person_EmailModelFormSet
    from .forms.person_address_forms import Person_AddressModelFormSet
    from .forms.person_phone_forms import Person_PhoneModelFormSet
    
    m2m_data = {
        'phone': {
            'class': Person_Phone,
            'formset': Person_PhoneModelFormSet,
            'filter_expresion': 'person__id_number',
            'omit_field' : 'person',
            'create_url': 'people:person_phone_create',
            'update_url': 'people:person_phone_update',
            'delete_url': 'people:person_phone_delete'
        },
        'e_mail': {
            'class': Person_E_Mail,
            'formset': Person_EmailModelFormSet,
            'filter_expresion': 'person__id_number',
            'omit_field' : 'person',
            'create_url': 'people:person_e_mail_create',
            'update_url': 'people:person_e_mail_update',
            'delete_url': 'people:person_e_mail_delete'
        },
        'address': {
            'class': Person_Address,
            'formset': Person_AddressModelFormSet,
            'filter_expresion': 'person__id_number',
            'omit_field' : 'person',
            'create_url': 'people:person_address_create',
            'update_url': 'people:person_address_update',
            'delete_url': 'people:person_address_delete'
        }      
    }
    return m2m_data

def person_legal_m2m_data(*args):

    from .models import Person_Legal_Person_Natural
    from .forms.person_legal_person_natural_forms import Person_Legal_Person_NaturalModelFormSet

    m2m_data = person_natural_m2m_data()
    m2m_data['staff'] = {
        'class': Person_Legal_Person_Natural,
        'formset': Person_Legal_Person_NaturalModelFormSet,
        'filter_expresion': 'person_legal__id_number',
        'omit_field' : 'person_legal',
        'create_url': 'people:person_legal_person_natural_create',
        'update_url': 'people:person_legal_person_natural_update',
        'delete_url': 'people:person_legal_person_natural_delete'
    }        
    return m2m_data

