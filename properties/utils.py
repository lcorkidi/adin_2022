def estate_m2m_data(*args):
    from .models import Estate_Person
    from .forms.estate_person_forms import Estate_PersonModelFormSet
    
    m2m_data = {
        'owner': {
            'class': Estate_Person,
            'formset': Estate_PersonModelFormSet,
            'filter_expresion': 'estate__code',
            'omit_field' : 'estate',
            'create_url': 'properties:estate_person_create',
            'update_url': 'properties:estate_person_update',
            'delete_url': 'properties:estate_person_delete'
        }      
    }
    
    return m2m_data