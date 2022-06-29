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
            'omit_actions' : [],
            'create_url': 'properties:estate_person_create',
            'update_url': 'properties:estate_person_update',
            'delete_url': 'properties:estate_person_delete',
            'activate_url': 'properties:estate_person_activate'
        },
        'Avaluo(s):': {
            'class': Estate_Appraisal,
            'formset': Estate_AppraisalModelFormSet,
            'filter_expresion': 'estate__national_number',
            'omit_actions' : [],
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
            'omit_actions' : [],
            'create_url': 'properties:realty_estate_create',
            'update_url': 'properties:realty_estate_update',
            'delete_url': 'properties:realty_estate_delete',
            'activate_url': 'properties:realty_estate_activate'
        }
    }
    
    return related_data
