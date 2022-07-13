def ledger2consecutive(ledger):
    from accounting.models import Ledger
    return Ledger.objects.filter(type=ledger.type).count() + 1

def ledger2code(ledger):
    ref_num_str = str(ledger.consecutive)
    for i in range(8 - len(ref_num_str)):
        ref_num_str = '0' + ref_num_str
    return f'{ledger.type.abreviation}-{ref_num_str}'

def ledgertemplate2code(template):
    return f'{template.ledger_type.abreviation}_{template.transaction_type.name}'

def ledger_related_data(*args):
    from .models import Charge
    from .forms.charge_forms import ChargeModelFormSet

    related_data = {
        'Movimientos:': {
            'class': Charge,
            'formset': ChargeModelFormSet,
            'filter_expresion': 'ledger__code',
            'omit_field' : 'ledger',
            'omit_actions' : ['detail'],
            'create_url': 'accounting:charge_create',
            'update_url': 'accounting:charge_update',
            'delete_url': 'accounting:charge_delete',
            'activate_url': 'accounting:charge_activate'
        } 
    }

    return related_data

def ledger_template_related_data(*args):
    from .models import Charge_Template
    from .forms.charge_template_forms import Charge_TemplateModelFormSet

    related_data = {
        'Formatos Movimientos:': {
            'class': Charge_Template,
            'formset': Charge_TemplateModelFormSet,
            'filter_expresion': 'ledger_template__code',
            'omit_field' : 'ledger_template',
            'omit_actions' : ['detail'],
            'create_url': 'accounting:charge_template_create',
            'update_url': 'accounting:charge_template_update',
            'delete_url': 'accounting:charge_template_delete',
            'activate_url': 'accounting:charge_template_activate'
        } 
    }

    return related_data
