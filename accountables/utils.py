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
            'delete_url': 'accountables:lease_realty_realty_delete',
            'activate_url': 'accountables:lease_realty_realty_activate'
        },
        'Partes:': {
            'class': Lease_Realty_Person,
            'formset': Lease_Realty_PersonModelFormSet,
            'filter_expresion': 'lease__code',
            'omit_field' : 'lease',
            'create_url': 'accountables:lease_realty_person_create',
            'update_url': 'accountables:lease_realty_person_update',
            'delete_url': 'accountables:lease_realty_person_delete',
            'activate_url': 'accountables:lease_realty_person_activate'
        },
        'Canon(es):': {
            'class': Date_Value,
            'formset': Date_ValueModelFormSet,
            'filter_expresion': 'accountable__code',
            'omit_field' : 'accountable',
            'create_url': 'accountables:date_value_create',
            'update_url': 'accountables:date_value_update',
            'delete_url': 'accountables:date_value_delete',
            'activate_url': 'accountables:date_value_activate'
        }
    }
    
    return related_data

def lease_realty_accounting_data(*args):
    from references.models import Transaction_Type
    from references.forms.transaction_type_forms import Transaction_TypeModelFormSet
    from accounting.models import Charge_Concept
    from accounting.forms.charge_concept_form import Charge_ConceptModelFormSet
    
    accounting_data = {
        'Tipos de Cargos':{
            'class': Transaction_Type,
            'formset': Transaction_TypeModelFormSet,
            'filter_expresion': 'lease_realty__code',
            'm2m_direct': True,
            'add_url': 'accountables:lease_realty_transaction_type_add',
            'remove_url': 'accountables:lease_realty_transaction_type_remove'
        },
        'Cargos':{
            'class': Charge_Concept,
            'formset': Charge_ConceptModelFormSet,
            'filter_expresion': 'accountable__code',
            'omit_field' : 'accountable',
            'create_url': 'accountables:lease_realty_realty_create',
            'update_url': 'accountables:lease_realty_realty_update',
            'delete_url': 'accountables:lease_realty_realty_delete',
            'activate_url': 'accountables:lease_realty_realty_activate'
        }
    }

    return accounting_data