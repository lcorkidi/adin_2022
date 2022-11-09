
per_dict = {
        'Account':  {
            'accounting.activate_account': 'activate',
            'accounting.add_account': 'create',
            'accounting.change_account': 'update',
            'accounting.check_account' : 'check',
            'accounting.delete_account': 'deactivate',
            'accounting.view_account': 'detail'
            },
        'Ledger_Template':  {
            'accounting.activate_ledger_template': 'activate',
            'accounting.add_ledger_template': 'create',
            'accounting.check_ledger_template' : 'check',
            'accounting.delete_ledger_template': 'deactivate',
            'accounting.view_ledger_template': 'detail',
            },
        'Ledger':  {
            'accounting.activate_ledger': 'activate',
            'accounting.add_ledger': 'create',
            'accounting.check_ledger' : 'check',
            'accounting.delete_ledger': 'deactivate',
            'accounting.view_ledger': 'detail',
            },
        'Ledger_Type':  {
            'accounting.activate_ledger_type': 'activate',
            'accounting.add_ledger_type': 'create',
            'accounting.check_ledger_type' : 'check',
            'accounting.delete_ledger_type': 'deactivate',
            'accounting.view_ledger_type': 'detail'
            },
        'Charge_Template':  {
            'accounting.activate_charge_template': 'activate',
            'accounting.add_charge_template': 'create',
            'accounting.check_charge_template' : 'check',
            'accounting.delete_charge_template': 'deactivate',
            'accounting.view_charge_template': 'detail',
            },
        'Charge':  {
            'accounting.activate_charge': 'activate',
            'accounting.add_charge': 'create',
            'accounting.check_charge' : 'check',
            'accounting.delete_charge': 'deactivate',
            'accounting.view_charge': 'detail',
            }
        }

perm_dict = {
        'Ledger_Type': 'accounting.activate_ledger_type',
        'Ledger': 'accounting.activate_ledger',
        'Account': 'accounting.activate_account',
        'Ledger_Template': 'accounting.activate_ledger_template',
        'Charge_Template': 'accounting.activate_charge_template',
        'Charge': 'accounting.activate_charge'
        }

def ledger_related_data(*args):
    from ..models import Charge
    from ..forms.charge_forms import ChargeModelFormSet

    related_data = {
        'Movimientos:': {
            'class': Charge,
            'formset': ChargeModelFormSet,
            'filter_expresion': 'ledger__code',
            'actions_on' : ActionsOn,
            'included_states' : IncludedStates,
            'create_url': 'accounting:charge_create',
            'update_url': 'accounting:charge_update',
            'delete_url': 'accounting:charge_delete',
            'activate_url': 'accounting:charge_activate'
        } 
    }

    return related_data

def ledger_template_related_data(*args):
    from ..models import Charge_Template
    from ..forms.charge_template_forms import Charge_TemplateModelFormSet

    related_data = {
        'Formatos Movimientos:': {
            'class': Charge_Template,
            'formset': Charge_TemplateModelFormSet,
            'filter_expresion': 'ledger_template__code',
            'actions_on' : ActionsOn,
            'included_states' : IncludedStates,
            'create_url': 'accounting:charge_template_create',
            'update_url': 'accounting:charge_template_update',
            'delete_url': 'accounting:charge_template_delete',
            'activate_url': 'accounting:charge_template_activate'
        } 
    }

    return related_data

def ledger_template_register_receipt_data(*args):
    from accountables.models import Accountable
    from accounting.forms.charge_forms import ChargeReceivablePendingFormSet
    from accountables.forms.accountable_forms import AccountableAccountingForm

    related_data = {
        'Cartera:': {
            'class' : Accountable,
            'form' : AccountableAccountingForm,
            'formset': ChargeReceivablePendingFormSet,
            'filter_expresion': 'ledger_template__code',
            'actions_on' : ActionsOn,
            'included_states' : IncludedStates,
            'create_url': 'accounting:charge_template_create',
            'update_url': 'accounting:charge_template_update',
            'delete_url': 'accounting:charge_template_delete',
            'activate_url': 'accounting:charge_template_activate'
        } 
    }

    
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
