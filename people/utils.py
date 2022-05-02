
def personcompletename(person):
    if person.type == 0:
        return f'{person.last_name}, {person.name}'
    elif person.type == 1:
        return f'{person.name} {person.get_legal_type_display()}'

def person_natural_related_data(*args):
    from .models import Person_Phone, Person_E_Mail, Person_Address
    from .forms.person_e_mail_forms import Person_E_MailModelFormSet
    from .forms.person_address_forms import Person_AddressModelFormSet
    from .forms.person_phone_forms import Person_PhoneModelFormSet
    
    related_data = {
        'Telefono(s):': {
            'class': Person_Phone,
            'formset': Person_PhoneModelFormSet,
            'filter_expresion': 'person__id_number',
            'omit_field' : 'person',
            'create_url': 'people:person_phone_create',
            'update_url': 'people:person_phone_update',
            'delete_url': 'people:person_phone_delete',
            'activate_url': 'people:person_phone_activate'
        },
        'Correo(s) Electrónico(s):': {
            'class': Person_E_Mail,
            'formset': Person_E_MailModelFormSet,
            'filter_expresion': 'person__id_number',
            'omit_field' : 'person',
            'create_url': 'people:person_e_mail_create',
            'update_url': 'people:person_e_mail_update',
            'delete_url': 'people:person_e_mail_delete',
            'activate_url': 'people:person_e_mail_activate'
        },
        'Direccione(s)': {
            'class': Person_Address,
            'formset': Person_AddressModelFormSet,
            'filter_expresion': 'person__id_number',
            'omit_field' : 'person',
            'create_url': 'people:person_address_create',
            'update_url': 'people:person_address_update',
            'delete_url': 'people:person_address_delete',
            'activate_url': 'people:person_address_activate'
        }      
    }
    return related_data

def person_legal_related_data(*args):

    from .models import Person_Legal_Person_Natural
    from .forms.person_legal_person_natural_forms import Person_Legal_Person_NaturalModelFormSet

    related_data = person_natural_related_data()
    related_data['Personal:'] = {
        'class': Person_Legal_Person_Natural,
        'formset': Person_Legal_Person_NaturalModelFormSet,
        'filter_expresion': 'person_legal__id_number',
        'omit_field' : 'person_legal',
        'create_url': 'people:person_legal_person_natural_create',
        'update_url': 'people:person_legal_person_natural_update',
        'delete_url': 'people:person_legal_person_natural_delete',
        'activate_url': 'people:person_legal_person_natural_activate'
    }        
    return related_data

