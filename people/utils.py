
per_dict = {
        'Person':  {
            'people.activate_person': 'activate',
            'people.add_person': 'create',
            'people.change_person': 'update',
            'people.check_person' : 'check',
            'people.delete_person': 'deactivate',
            'people.view_person': 'detail'
            },
        'Person_Natural':  {
            'people.activate_person': 'activate',
            'people.add_person': 'create',
            'people.change_person': 'update',
            'people.check_person' : 'check',
            'people.delete_person': 'deactivate',
            'people.view_person': 'detail'
            },
        'Person_Legal':  {
            'people.activate_person': 'activate',
            'people.add_person': 'create',
            'people.change_person': 'update',
            'people.check_person' : 'check',
            'people.delete_person': 'deactivate',
            'people.view_person': 'detail'
            },
        'Person_Address':  {
            'people.activate_person': 'activate',
            'people.add_person': 'create',
            'people.change_person': 'update',
            'people.check_person' : 'check',
            'people.delete_person': 'deactivate',
            },
        'Person_Phone':  {
            'people.activate_person': 'activate',
            'people.add_person': 'create',
            'people.change_person': 'update',
            'people.check_person' : 'check',
            'people.delete_person': 'deactivate',
            },
        'Person_E_Mail':  {
            'people.activate_person': 'activate',
            'people.add_person': 'create',
            'people.change_person': 'update',
            'people.check_person' : 'check',
            'people.delete_person': 'deactivate',
            },
        'Person_Legal_Person_Natural':  {
            'people.activate_person': 'activate',
            'people.add_person': 'create',
            'people.change_person': 'update',
            'people.check_person' : 'check',
            'people.delete_person': 'deactivate',
            }
        }

perm_dict = {
        'Person': 'people.activate_person',
        'Person_Natural': 'people.activate_person',
        'Person_Legal': 'people.activate_person',
        'Person_Address': 'people.activate_person',
        'Person_Phone': 'people.activate_person',
        'Person_E_Mail': 'people.activate_person',
        'Person_Legal_Person_Natural': 'people.activate_person'
        }

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
            'actions_on' : ActionsOn,
            'included_states' : IncludedStates,
            'create_url': 'people:person_phone_create',
            'update_url': 'people:person_phone_update',
            'delete_url': 'people:person_phone_delete',
            'activate_url': 'people:person_phone_activate',
            'check_url': 'people:person_phone_update'
        },
        'Correo(s) Electrónico(s):': {
            'class': Person_E_Mail,
            'formset': Person_E_MailModelFormSet,
            'filter_expresion': 'person__id_number',
            'actions_on' : ActionsOn,
            'included_states' : IncludedStates,
            'create_url': 'people:person_e_mail_create',
            'update_url': 'people:person_e_mail_update',
            'delete_url': 'people:person_e_mail_delete',
            'activate_url': 'people:person_e_mail_activate',
            'check_url': 'people:person_e_mail_update'
        },
        'Direccione(s)': {
            'class': Person_Address,
            'formset': Person_AddressModelFormSet,
            'filter_expresion': 'person__id_number',
            'actions_on' : ActionsOn,
            'included_states' : IncludedStates,
            'create_url': 'people:person_address_create',
            'update_url': 'people:person_address_update',
            'delete_url': 'people:person_address_delete',
            'activate_url': 'people:person_address_activate',
            'check_url': 'people:person_address_update'
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
        'actions_on' : ActionsOn,
        'included_states' : IncludedStates,
        'create_url': 'people:person_legal_person_natural_create',
        'update_url': 'people:person_legal_person_natural_update',
        'delete_url': 'people:person_legal_person_natural_delete',
        'activate_url': 'people:person_legal_person_natural_activate',
        'check_url': 'people:person_legal_person_natural_update'
    }        
    return related_data

def GetActionsOn(self, user, model):
    return ActionsOn(user, model)

def GetIncludedStates(self, user, model):
    return IncludedStates(user, model)

def ActionsOn(user, model):
    actions_on = []
    permissions = per_dict[model]
    for per, action in permissions.items():
        if user.has_perm(per):
            actions_on.append(action)
    return actions_on

def IncludedStates(user, model):
    permission = perm_dict[model]
    if user.has_perm(permission):
        return [ 0, 1, 2, 3 ]
    return [ 1, 2, 3 ]