import datetime
from dateutil.relativedelta import relativedelta

def ledger2consecutive(ledger):
    from accounting.models import Ledger
    return Ledger.objects.filter(type=ledger.type).count() + 1

def ledger2code(ledger):
    ref_num_str = str(ledger.consecutive)
    for i in range(8 - len(ref_num_str)):
        ref_num_str = '0' + ref_num_str
    return f'{ledger.type.abreviation}-{ref_num_str}'

def ledgertemplate2code(template):
    return f'{template.ledger_type.abreviation}^{template.accountable_class.name}_{template.transaction_type.name}'

def DueAge(_dueDate, split_months=True):
    bufferDate=_dueDate
    months=0
    days=0
    while bufferDate < datetime.date.today():
        if bufferDate + relativedelta(months=1) < datetime.date.today():
            months = months +1
        else:
            days=(datetime.date.today() - bufferDate).days
        bufferDate = bufferDate + relativedelta(months=1)
    return (months, days) if split_months else (datetime.date.today() - _dueDate).days

