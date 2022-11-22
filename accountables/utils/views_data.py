accountables_ref_urls = {
    'lease_realty': { 'list':'accountables:lease_realty_list', 'create':'accountables:lease_realty_create', 'detail':'accountables:lease_realty_detail', 'update':'accountables:lease_realty_update', 'delete':'accountables:lease_realty_delete', 'activate':'accountables:lease_realty_activate', 'accounting':'accountables:lease_realty_accounting' }
}

per_dict = {
        'Lease_Realty':  {
            'accountables.activate_lease_realty': ['activate'],
            'accountables.add_lease_realty': ['create'],
            'accountables.change_lease_realty': ['update'],
            'accountables.check_lease_realty' : ['check'],
            'accountables.delete_lease_realty': ['deactivate'],
            'accountables.view_lease_realty': ['detail', 'report'],
            'accountables.accounting_lease_realty': ['accounting']
            },
        'Lease_Realty_Main_Errors':  {
            'accountables.activate_lease_realty': ['activate'],
            'accountables.change_lease_realty': ['update'],
            'accountables.check_lease_realty' : ['check'],
            'accountables.delete_lease_realty': ['deactivate'],
            'accountables.view_lease_realty': ['detail', 'report'],
            'accountables.accounting_lease_realty': ['accounting']
            },
        'Lease_Realty_Main_Pending_Date_Value':  {
            'accountables.activate_lease_realty': ['activate'],
            'accountables.change_lease_realty': ['update'],
            'accountables.check_lease_realty' : ['check'],
            'accountables.delete_lease_realty': ['deactivate'],
            'accountables.view_lease_realty': ['detail', 'report'],
            'accountables.accounting_lease_realty': ['accounting']
            },
        'Lease_Realty_Main_Pending_Transaction_Concept':  {
            'accountables.add_lease_realty': ['create']
            },
        'Lease_Realty_Main_Pending_Monthly_Fee_Commit':  {
            'accounting.add_ledger': ['commit']
            },
        'Lease_Realty_Main_Pending_Monthly_Fee_Bill':  {
            'accounting.add_ledger': ['bill']
            },
        'Lease_Realty_Realty':  {
            'accountables.activate_lease_realty': ['activate'],
            'accountables.add_lease_realty': ['create'],
            # 'accountables.check_lease_realty' : 'check',
            'accountables.delete_lease_realty': ['deactivate'],
            },
        'Lease_Realty_Person':  {
            'accountables.activate_lease_realty': ['activate'],
            'accountables.add_lease_realty': ['create'],
            'accountables.view_lease_realty': ['detail'],
            'accountables.change_lease_realty': ['update'],
            'accountables.check_lease_realty' : ['check'],
            'accountables.delete_lease_realty': ['deactivate'],
            },
        'Date_Value':  {
            'accountables.activate_realty': ['activate'],
            'accountables.add_realty': ['create'],
            'accountables.change_realty': ['update'],
            'accountables.check_realty' : ['check'],
            'accountables.delete_realty': ['deactivate'],
            },
        'Transaction_Type':  {
            'accountables.activate_transaction_type': ['activate'],
            'accountables.add_transaction_type': ['create'],
            'accountables.check_transaction_type' : ['check'],
            'accountables.delete_transaction_type': ['deactivate'],
            },
        'Accountable_Transaction_Type':  {
            'accountables.activate_accounable_transaction_type': ['activate'],
            'accountables.view_accounable_transaction_type' : ['detail'],
            'accountables.add_accounable_transaction_type': ['create'],
            'accountables.check_accounable_transaction_type' : ['check'],
            'accountables.delete_accounable_transaction_type': ['deactivate'],
            },
        'Accountable_Concept':  {
            # 'accountables.activate_accountable_concept': 'activate',
            'accountables.add_accountable_concept': ['create'],
            # 'accountables.check_accountable_concept' : 'check',
            # 'accountables.delete_accountable_concept': 'deactivate',
            }
        }

perm_dict = {
        'Lease_Realty': 'accountables.activate_lease_realty',
        'Lease_Realty_Main_Errors': 'accountables.activate_lease_realty',
        'Lease_Realty_Main_Pending_Date_Value': 'accountables.activate_lease_realty',
        'Lease_Realty_Main_Pending_Transaction_Concept': 'accountables.activate_lease_realty',
        'Lease_Realty_Main_Pending_Monthly_Fee_Commit': 'accounting.activate_ledger',
        'Lease_Realty_Main_Pending_Monthly_Fee_Bill': 'accounting.activate_ledger',
        'Lease_Realty_Realty': 'accountables.activate_lease_realty',
        'Lease_Realty_Person': 'accountables.activate_lease_realty',
        'Date_Value': 'accountables.activate_lease_realty',
        'Transaction_Type': 'accountables.activate_lease_realty',
        'Accountable_Transaction_Type': 'accountables.activate_lease_realty',
        'Accountable_Concept': 'accountables.activate_accountable_concept'
        }

def lease_realty_related_data(*args):
    from ..models import Lease_Realty_Realty, Lease_Realty_Person, Date_Value
    from ..forms.lease_realty_realty_forms import Lease_Realty_RealtyModelFormSet
    from ..forms.lease_realty_person_forms import Lease_Realty_PersonModelFormSet, Lease_Realty_PersonRelatedUpdateModelFormSet
    from ..forms.date_value_forms import Date_ValueModelFormSet, Date_ValueRelatedUpdateModelFormSet
    
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
            'detail_url': 'accountables:lease_realty_person_detail',
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

def lease_realty_main_data(*args):
    from accountables.forms.lease_realty_forms import Lease_RealtyListModelFormSet
    from accountables.forms.accountable_concept_forms import Accountable_ConceptPendingBulkFormSet, Accountable_ConceptPendingLedgerBulkFormSet
    from accountables.utils.models_func import lease_realty_errors, lease_realty_pending_date_values, lease_realty_pending_monthly_fee_concepts, lease_realty_pending_monthly_fee_commit, lease_realty_pending_monthly_fee_bill
    
    related_data = {
        'Errores:': {
            'perm_dict_key': 'Lease_Realty_Main_Errors',
            'formset': Lease_RealtyListModelFormSet,
            'queryset_function' : lease_realty_errors,
            'actions_on' : ActionsOn,
            'included_states' : IncludedStates,
            'template': 'list',
            'detail_url': 'accountables:lease_realty_detail',
            'check_url': 'accountables:lease_realty_update',
            'update_url': 'accountables:lease_realty_update',
            'delete_url': 'accountables:lease_realty_delete',
            'activate_url': 'accountables:lease_realty_activate',
            'accounting_url': 'accountables:lease_realty_accounting',
            'report_url': 'accountables:lease_realty_report'
        },
        'Valores Pendientes:': {
            'perm_dict_key': 'Lease_Realty_Main_Pending_Date_Value',
            'formset': Lease_RealtyListModelFormSet,
            'queryset_function' : lease_realty_pending_date_values,
            'actions_on' : ActionsOn,
            'included_states' : IncludedStates,
            'template': 'list',
            'detail_url': 'accountables:lease_realty_detail',
            'check_url': 'accountables:lease_realty_update',
            'update_url': 'accountables:lease_realty_update',
            'delete_url': 'accountables:lease_realty_delete',
            'activate_url': 'accountables:lease_realty_activate',
            'accounting_url': 'accountables:lease_realty_accounting',
            'report_url': 'accountables:lease_realty_report'
        },
        'Conceptos Mensualidad Arriendo Pendientes:': {
            'perm_dict_key': 'Lease_Realty_Main_Pending_Transaction_Concept',
            'formset': Accountable_ConceptPendingBulkFormSet,
            'dict_list_function' : lease_realty_pending_monthly_fee_concepts,
            'actions_on' : ActionsOn,
            'included_states' : IncludedStates,
            'template': 'bulk_data',
            'create_url': 'accountables:single_pending_accountable_concept_create',
            'create_bulk_url': 'accountables:bulk_pending_accountable_concept_create'
        },
        'Causacion Mensualidad Arriendo Pendientes:': {
            'perm_dict_key': 'Lease_Realty_Main_Pending_Monthly_Fee_Commit',
            'formset': Accountable_ConceptPendingLedgerBulkFormSet,
            'queryset_function' : lease_realty_pending_monthly_fee_commit,
            'actions_on' : ActionsOn,
            'included_states' : IncludedStates,
            'template': 'bulk_data',
            'commit_url': 'accounting:ledger_template_register_commit',
            'commit_bulk_url': 'accounting:ledger_template_bulk_pending_register'
        },
        'Facturacion Mensualidad Arriendo Pendientes:': {
            'perm_dict_key': 'Lease_Realty_Main_Pending_Monthly_Fee_Bill',
            'formset': Accountable_ConceptPendingLedgerBulkFormSet,
            'queryset_function' : lease_realty_pending_monthly_fee_bill,
            'actions_on' : ActionsOn,
            'included_states' : IncludedStates,
            'template': 'bulk_data',
            'commit_url': 'accounting:ledger_template_register_commit',
            'commit_bulk_url': 'accounting:ledger_template_bulk_pending_register'
        }
    }

    return related_data

def accountable_related_data(*args):
    from accountables.models import Accountable_Transaction_Type, Accountable_Concept
    from accountables.forms.accountable_transaction_type_forms import Accountable_Transaction_TypeModelFormSet
    from accountables.forms.accountable_concept_forms import Accountable_ConceptModelFormSet
    
    accounting_data = {
        'Formatos Registro Transacciones:':{
            'class': Accountable_Transaction_Type,
            'formset': Accountable_Transaction_TypeModelFormSet,
            'filter_expresion': 'accountable__code',
            'actions_on' : ActionsOn,
            'included_states' : IncludedStates,
            'create_url': 'accountables:accountable_transaction_type_create',
            'detail_url': 'accountables:accountable_transaction_type_detail',
            'check_url': 'accountables:accountable_transaction_type_detail',
            'update_url': 'accountables:accountable_transaction_type_update',
            'delete_url': 'accountables:accountable_transaction_type_delete',
            'activate_url': 'accountables:accountable_transaction_type_activate',
        },
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
            actions_on += action
    return actions_on

def IncludedStates(user, model):
    permission = perm_dict[model]
    if user.has_perm(permission):
        return [ 0, 1, 2, 3 ]
    return [ 1, 2, 3 ]
