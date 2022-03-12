def estate_related_data(*args):
    from .models import Estate_Person, Estate_Appraisal
    from .forms.estate_person_forms import Estate_PersonModelFormSet
    from .forms.estate_appraisal_forms import Estate_AppraisalModelFormSet
    
    related_data = {
        'owner': {
            'class': Estate_Person,
            'formset': Estate_PersonModelFormSet,
            'filter_expresion': 'estate__code',
            'omit_field' : 'estate',
            'create_url': 'properties:estate_person_create',
            'update_url': 'properties:estate_person_update',
            'delete_url': 'properties:estate_person_delete'
        },
        'Avaluo(s) Predio(s):': {
            'class': Estate_Appraisal,
            'formset': Estate_AppraisalModelFormSet,
            'filter_expresion': 'estate__code',
            'create_url': 'properties:estate_appraisal_create',
            'update_url': 'properties:estate_appraisal_update',
            'delete_url': 'properties:estate_appraisal_delete'
        }      
    }
    
    return related_data
