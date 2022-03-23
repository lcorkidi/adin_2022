def lease_realty_related_data(*args):
    from .models import Lease_Realty_Realty, Lease_Realty_Person, Date_Value
    from .forms.lease_realty_realty_forms import Lease_Realty_RealtyModelFormSet
    from .forms.lease_realty_person_forms import Lease_Realty_PersonModelFormSet
    from .forms.date_value_forms import Date_ValueModelFormSet
    
    related_data = {
        'Inmueble(s):': {
            'class': Lease_Realty_Realty,
            'formset': Lease_Realty_RealtyModelFormSet,
            'filter_expresion': 'lease__code',
            'omit_field' : 'lease',
            'create_url': 'accountables:lease_realty_realty_create',
            'update_url': 'accountables:lease_realty_realty_update',
            'delete_url': 'accountables:lease_realty_realty_delete'
        },
        'Partes:': {
            'class': Lease_Realty_Person,
            'formset': Lease_Realty_PersonModelFormSet,
            'filter_expresion': 'lease__code',
            'omit_field' : 'lease',
            'create_url': 'accountables:lease_realty_person_create',
            'update_url': 'accountables:lease_realty_person_update',
            'delete_url': 'accountables:lease_realty_person_delete'
        },
        'Canon(es):': {
            'class': Date_Value,
            'formset': Date_ValueModelFormSet,
            'filter_expresion': 'accountable__code',
            'omit_field' : 'accountable',
            'create_url': 'accountables:date_value_create',
            'update_url': 'accountables:date_value_update',
            'delete_url': 'accountables:date_value_delete'
        }
    }
    
    return related_data
