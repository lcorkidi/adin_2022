accountables_ref_urls = {
    'lease_realty': { 'list':'accountables:lease_realty_list', 'create':'accountables:lease_realty_create', 'detail':'accountables:lease_realty_detail', 'update':'accountables:lease_realty_update', 'delete':'accountables:lease_realty_delete', 'activate':'accountables:lease_realty_activate', 'accounting':'accountables:lease_realty_accounting' }
}

def lease_realty_code(realty, doc_date):
    return f'{realty.code}^{doc_date.strftime("%Y-%m-%d")}'

def accon_2_code(accon):
    return f'{accon.transaction_type}^{accon.date.strftime("%Y-%m-%d")}_{accon.accountable.code}'

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
    from accounting.models import Ledger_Template
    from accountables.forms.accountable_transaction_type_forms import Accountable_Transaction_TypeModelFormSet
    from accountables.forms.accountable_concept_forms import Accountable_ConceptModelFormSet
    from accounting.forms.ledger_template_forms import Ledger_TemplateAvailableModelFormset
    
    accounting_data = {
        'Tipos de Transacción:':{
            'class': Accountable_Transaction_Type,
            'formset': Accountable_Transaction_TypeModelFormSet,
            'filter_expresion': 'accountable__code',
            'm2m_direct': True,
            'add_url': 'accountables:accountable_transaction_type_add',
            'remove_url': 'accountables:accountable_transaction_type_remove'
        },
        'Conceptos Transacciones:':{
            'class': Accountable_Concept,
            'formset': Accountable_ConceptModelFormSet,
            'filter_expresion': 'accountable__code',
            'omit_field' : 'accountable',
            'omit_actions' : ['detail'],
            'create_url': 'accountables:accountable_concept_create',
            'pending_url': 'accountables:pending_accountable_concept_create',
            'delete_url': 'accountables:accountable_concept_delete',
            'activate_url': 'accountables:accountable_concept_activate'
        }
    }

    return accounting_data

def GetActionsOn(self, user, model):
    actions_on = []
    per_dict = {
        'Lease_Realty':  {
            'accountables.activate_lease_realty': 'activate',
            'accountables.add_lease_realty': 'create',
            'accountables.change_lease_realty': 'update',
            'accountables.check_lease_realty' : 'check',
            'accountables.delete_lease_realty': 'deactivate',
            'accountables.view_lease_realty': 'detail',
            'accountables.accounting_lease_realty': 'accounting',
            },
        'Accountable_Transaction_Type':  {
            'accountables.activate_accountble_transaction_type': 'activate',
            'accountables.add_accountble_transaction_type': 'create',
            'accountables.check_accountble_transaction_type' : 'check',
            'accountables.delete_accountble_transaction_type': 'deactivate',
            }
        }
    permissions = per_dict[model]
    for per, action in permissions.items():
        if user.has_perm(per):
            actions_on.append(action)
    return actions_on

def GetIncludedStates(self, user, model):
    perm_dict = {
        'Lease_Realty': 'accountables.activate_lease_realty',
        'Accountable_Transaction_Type': 'accountables.activate_realty'
        }
    permission = perm_dict[model]
    if user.has_perm(permission):
        return [ 0, 1, 2, 3 ]
    return [ 1, 2, 3 ]