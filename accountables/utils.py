accountables_ref_urls = {
    'lease_realty': { 'list':'accountables:lease_realty_list', 'create':'accountables:lease_realty_create', 'detail':'accountables:lease_realty_detail', 'update':'accountables:lease_realty_update', 'delete':'accountables:lease_realty_delete', 'activate':'accountables:lease_realty_activate', 'accounting':'accountables:lease_realty_accounting' }
}

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
        'Lease_Realty_Realty':  {
            'accountables.activate_lease_realty': 'activate',
            'accountables.add_lease_realty': 'create',
            # 'accountables.check_lease_realty' : 'check',
            'accountables.delete_lease_realty': 'deactivate',
            },
        'Lease_Realty_Person':  {
            'accountables.activate_lease_realty': 'activate',
            'accountables.add_lease_realty': 'create',
            'accountables.change_lease_realty': 'update',
            'accountables.check_lease_realty' : 'check',
            'accountables.delete_lease_realty': 'deactivate',
            },
        'Date_Value':  {
            'accountables.activate_realty': 'activate',
            'accountables.add_realty': 'create',
            'accountables.change_realty': 'update',
            'accountables.check_realty' : 'check',
            'accountables.delete_realty': 'deactivate',
            },
        'Accountable_Transaction_Type':  {
            'accountables.activate_accountble_transaction_type': 'activate',
            'accountables.add_accountble_transaction_type': 'create',
            'accountables.check_accountble_transaction_type' : 'check',
            'accountables.delete_accountble_transaction_type': 'deactivate',
            },
        'Accountable_Concept':  {
            # 'accountables.activate_accountable_concept': 'activate',
            'accountables.add_accountable_concept': 'create',
            # 'accountables.check_accountable_concept' : 'check',
            # 'accountables.delete_accountable_concept': 'deactivate',
            }
        }

perm_dict = {
        'Lease_Realty': 'accountables.activate_lease_realty',
        'Lease_Realty_Realty': 'accountables.activate_lease_realty',
        'Lease_Realty_Person': 'accountables.activate_lease_realty',
        'Date_Value': 'accountables.activate_lease_realty',
        'Accountable_Transaction_Type': 'accountables.activate_realty',
        'Accountable_Concept': 'accountables.activate_accountable_concept'
        }

def lease_realty_code(realty, doc_date):
    return f'{realty.code}^{doc_date.strftime("%Y-%m-%d")}'

def accon_2_code(accon):
    return f'{accon.transaction_type}^{accon.date.strftime("%Y-%m-%d")}_{accon.accountable.code}'

def lease_realty_related_data(*args):
    from .models import Lease_Realty_Realty, Lease_Realty_Person, Date_Value
    from .forms.lease_realty_realty_forms import Lease_Realty_RealtyModelFormSet
    from .forms.lease_realty_person_forms import Lease_Realty_PersonModelFormSet, Lease_Realty_PersonRelatedUpdateModelFormSet
    from .forms.date_value_forms import Date_ValueModelFormSet, Date_ValueRelatedUpdateModelFormSet
    
    related_data = {
        'Inmueble(s):': {
            'class': Lease_Realty_Realty,
            'formset': Lease_Realty_RealtyModelFormSet,
            'filter_expresion': 'lease__code',
            'actions_on' : ActionsOn,
            'included_states' : IncludedStates,
            'create_url': 'accountables:lease_realty_realty_create',
            'check_url': 'accountables:lease_realty_realty_update',
            'delete_url': 'accountables:lease_realty_realty_delete',
            'activate_url': 'accountables:lease_realty_realty_activate'
        },
        'Partes:': {
            'class': Lease_Realty_Person,
            'formset': Lease_Realty_PersonRelatedUpdateModelFormSet,
            'filter_expresion': 'lease__code',
            'actions_on' : ActionsOn,
            'included_states' : IncludedStates,
            'create_url': 'accountables:lease_realty_person_create',
            'check_url': 'accountables:lease_realty_person_update',
            'update_url': 'accountables:lease_realty_person_update',
            'delete_url': 'accountables:lease_realty_person_delete',
            'activate_url': 'accountables:lease_realty_person_activate'
        },
        'Canon(es):': {
            'class': Date_Value,
            'formset': Date_ValueRelatedUpdateModelFormSet,
            'filter_expresion': 'accountable__code',
            'actions_on' : ActionsOn,
            'included_states' : IncludedStates,
            'create_url': 'accountables:date_value_create',
            'check_url': 'accountables:date_value_update',
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
        'Conceptos Transacciones:':{
            'class': Accountable_Concept,
            'formset': Accountable_ConceptModelFormSet,
            'filter_expresion': 'accountable__code',
            'actions_on' : ActionsOn,
            'included_states' : IncludedStates,
            'create_url': 'accountables:accountable_concept_create',
            'pending_url': 'accountables:pending_accountable_concept_create',
            'delete_url': 'accountables:accountable_concept_delete',
            'activate_url': 'accountables:accountable_concept_activate',
            'commit_url': 'accounting:ledger_template_register_commit'
        }
    }

    return accounting_data

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
