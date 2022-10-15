def estate_related_data(*args):
    from .models import Estate_Person, Estate_Appraisal
    from .forms.estate_person_forms import Estate_PersonModelFormSet
    from .forms.estate_appraisal_forms import Estate_AppraisalModelFormSet
    
    related_data = {
        'Propietario(s):': {
            'class': Estate_Person,
            'formset': Estate_PersonModelFormSet,
            'filter_expresion': 'estate__national_number',
            'omit_field' : 'estate',
            'omit_actions' : ['detail'],
            'create_url': 'properties:estate_person_create',
            'update_url': 'properties:estate_person_update',
            'delete_url': 'properties:estate_person_delete',
            'activate_url': 'properties:estate_person_activate'
        },
        'Avaluo(s):': {
            'class': Estate_Appraisal,
            'formset': Estate_AppraisalModelFormSet,
            'filter_expresion': 'estate__national_number',
            'omit_actions' : ['detail'],
            'create_url': 'properties:estate_appraisal_create',
            'update_url': 'properties:estate_appraisal_update',
            'delete_url': 'properties:estate_appraisal_delete',
            'activate_url': 'properties:estate_appraisal_activate'
        }      
    }
    
    return related_data

def realty_related_data(*args):
    from .models import Realty_Estate
    from .forms.realty_estate_forms import Realty_EstateModelFormSet
    
    related_data = {
        'Predio(s):': {
            'class': Realty_Estate,
            'formset': Realty_EstateModelFormSet,
            'filter_expresion': 'realty__code',
            'omit_field' : 'realty',
            'omit_actions' : ['detail'],
            'create_url': 'properties:realty_estate_create',
            'update_url': 'properties:realty_estate_update',
            'delete_url': 'properties:realty_estate_delete',
            'activate_url': 'properties:realty_estate_activate'
        }
    }
    
    return related_data

def GetActionsOn(self, user, model):
    actions_on = []
    per_dict = {
        'Estate':  {
            'properties.activate_estate': 'activate',
            'properties.add_estate': 'create',
            'properties.change_estate': 'update',
            'properties.check_estate' : 'check',
            'properties.delete_estate': 'deactivate',
            'properties.view_estate': 'detail'
            },
        'Realty':  {
            'properties.activate_realty': 'activate',
            'properties.add_estate': 'create',
            'properties.change_estate': 'update',
            'properties.check_estate' : 'check',
            'properties.delete_estate': 'deactivate',
            'properties.view_estate': 'detail'
            }
        }
    permissions = per_dict[model]
    for per, action in permissions.items():
        if user.has_perm(per):
            actions_on.append(action)
    return actions_on

def GetIncludedStates(self, user, model):
    perm_dict = {
        'Estate': 'properties.activate_estate',
        'Realty': 'properties.activate_realty'
        }
    permission = perm_dict[model]
    if user.has_perm(permission):
        return [ 0, 1, 2, 3 ]
    return [ 1, 2, 3 ]