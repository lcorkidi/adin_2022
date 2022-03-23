def lease_realty_related_data(*args):
    from .models import Lease_Realty_Realty, Lease_Realty_Person
    from .forms.lease_realty_realty_forms import Lease_Realty_RealtyModelFormSet
    from .forms.lease_realty_person_forms import Lease_Realty_PersonModelFormSet
    
    related_data = {
        'Inmueble(s):': {
            'class': Lease_Realty_Realty,
            'formset': Lease_Realty_RealtyModelFormSet,
            'filter_expresion': 'lease__code',
            'omit_field' : 'lease',
            'create_url': 'properties:realty_estate_create',
            'update_url': 'properties:realty_estate_update',
            'delete_url': 'properties:realty_estate_delete'
        },
        'Partes:': {
            'class': Lease_Realty_Person,
            'formset': Lease_Realty_PersonModelFormSet,
            'filter_expresion': 'lease__code',
            'omit_field' : 'lease',
            'create_url': 'properties:realty_estate_create',
            'update_url': 'properties:realty_estate_update',
            'delete_url': 'properties:realty_estate_delete'
        }
    }
    
    return related_data
