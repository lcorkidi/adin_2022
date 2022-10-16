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
            'properties.add_realty': 'create',
            'properties.change_realty': 'update',
            'properties.check_realty' : 'check',
            'properties.delete_realty': 'deactivate',
            'properties.view_realty': 'detail'
            },
        'Estate_Person':  {
            'properties.activate_realty': 'activate',
            'properties.add_estate': 'create',
            'properties.change_estate': 'update',
            'properties.check_estate' : 'check',
            'properties.delete_estate': 'deactivate',
            },
        'Estate_Appraisal':  {
            'properties.activate_realty': 'activate',
            'properties.add_estate': 'create',
            'properties.change_estate': 'update',
            'properties.check_estate' : 'check',
            'properties.delete_estate': 'deactivate',
            },
        'Realty_Estate':  {
            'properties.activate_realty': 'activate',
            'properties.add_realty': 'create',
            'properties.change_realty': 'update',
            'properties.check_realty' : 'check',
            'properties.delete_realty': 'deactivate',
            }
        }

perm_dict = {
        'Estate': 'properties.activate_estate',
        'Realty': 'properties.activate_realty',
        'Estate_Person': 'properties.activate_estate',
        'Estate_Appraisal': 'properties.activate_estate',
        'Realty_Estate': 'properties.activate_realty'
        }

def estate_related_data(*args):
    from .models import Estate_Person, Estate_Appraisal
    from .forms.estate_person_forms import Estate_PersonModelFormSet
    from .forms.estate_appraisal_forms import Estate_AppraisalModelFormSet
    
    related_data = {
        'Propietario(s):': {
            'class': Estate_Person,
            'formset': Estate_PersonModelFormSet,
            'filter_expresion': 'estate__national_number',
            'actions_on' : ActionsOn,
            'included_states' : IncludedStates,
            'create_url': 'properties:estate_person_create',
            'update_url': 'properties:estate_person_update',
            'delete_url': 'properties:estate_person_delete',
            'activate_url': 'properties:estate_person_activate',
            'check_url': 'properties:estate_person_update'
        },
        'Avaluo(s):': {
            'class': Estate_Appraisal,
            'formset': Estate_AppraisalModelFormSet,
            'filter_expresion': 'estate__national_number',
            'actions_on' : ActionsOn,
            'included_states' : IncludedStates,
            'create_url': 'properties:estate_appraisal_create',
            'update_url': 'properties:estate_appraisal_update',
            'delete_url': 'properties:estate_appraisal_delete',
            'activate_url': 'properties:estate_appraisal_activate',
            'check_url': 'properties:estate_appraisal_update'
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
            'actions_on' : ActionsOn,
            'included_states' : IncludedStates,
            'create_url': 'properties:realty_estate_create',
            'update_url': 'properties:realty_estate_update',
            'delete_url': 'properties:realty_estate_delete',
            'activate_url': 'properties:realty_estate_activate',
            'check_url': 'properties:realty_estate_update'
        }
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