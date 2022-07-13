accountables_ref_urls = {
    'lease_realty': { 'list':'accountables:lease_realty_list', 'create':'accountables:lease_realty_create', 'detail':'accountables:lease_realty_detail', 'update':'accountables:lease_realty_update', 'delete':'accountables:lease_realty_delete', 'activate':'accountables:lease_realty_activate', 'accounting':'accountables:lease_realty_accounting' }
}

def acc_con2code(chacon):
    return f'{chacon.transaction_type}^{chacon.date.strftime("%Y-%m-%d")}_{chacon.accountable}'

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
            'omit_actions' : ['detail', 'update'],
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
            'omit_actions' : [],
            'create_url': 'accountables:lease_realty_person_create',
            'detail_url': 'accountables:lease_realty_person_detail',
            'update_url': 'accountables:lease_realty_person_update',
            'delete_url': 'accountables:lease_realty_person_delete',
            'activate_url': 'accountables:lease_realty_person_activate'
        },
        'Canon(es):': {
            'class': Date_Value,
            'formset': Date_ValueModelFormSet,
            'filter_expresion': 'accountable__code',
            'omit_field' : 'accountable',
            'omit_actions' : ['detail'],
            'create_url': 'accountables:date_value_create',
            'update_url': 'accountables:date_value_update',
            'delete_url': 'accountables:date_value_delete',
            'activate_url': 'accountables:date_value_activate'
        }
    }
    
    return related_data

def accountable_related_data(*args):
    from accountables.models import Accountable_Transaction_Type, Accountable_Concept
    from accountables.forms.accountable_transaction_type_forms import Accountable_Transaction_TypeModelFormSet
    from accountables.forms.accountable_concept_forms import Accountable_ConceptModelFormSet
    
    accounting_data = {
        'Tipos de Transacción:':{
            'class': Accountable_Transaction_Type,
            'formset': Accountable_Transaction_TypeModelFormSet,
            'filter_expresion': 'accountable__code',
            'm2m_direct': True,
            'add_url': 'accountables:accountable_transaction_type_add',
            'remove_url': 'accountables:accountable_transaction_type_remove'
        },
        'Transacciones:':{
            'class': Accountable_Concept,
            'formset': Accountable_ConceptModelFormSet,
            'filter_expresion': 'accountable__code',
            'omit_field' : 'accountable',
            'omit_actions' : ['detail'],
            'create_url': 'accountables:accountable_charge_concept_create',
            'delete_url': 'accountables:accountable_charge_concept_delete',
            'activate_url': 'accountables:accountable_charge_concept_activate'
        }
    }

    return accounting_data