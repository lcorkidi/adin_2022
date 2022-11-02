import datetime
from dateutil.relativedelta import relativedelta

from adin.utils.date_progression import previousyearlydate, nextyearlydate

def IdTypeParse(id_type):
    if id_type == 0:
        return 1
    if id_type == 1:
        return 2
    if id_type == 2:
        return 7
    if id_type == 3:
        return 4
    return None

def LegalTypeParse(legal_type):
    if legal_type == 0:
        return 'SA'
    if legal_type == 1:
        return 'SAS'
    if legal_type == 2:
        return 'LTDA'
    if legal_type == 3:
        return 'EU'
    if legal_type == 4:
        return 'Y CIA'
    if legal_type == 5:
        return 'S EN C'

def CompleteNameParse(person):
    if person.type != 1:
        return f'{person.name} {person.subclass_obj().last_name}'.upper()
    elif person.type == 1:
        return f'{person.name} {LegalTypeParse(person.subclass_obj().legal_type)}'.upper()

def DateParse(date):
    return date.strftime("%Y%m%d")

def RoleParse(role):
    if role == 1:
        return '00'
    if role == 2:
        return '08'

def DueAgeParse(due_age):
    months = due_age[0]
    if months == 0:
        return '01'
    if months == 1:
        return '06'
    if months == 2:
        return '07'
    if months == 3:
        return '08'
    return '09'

def DueStateParse(due_age):
    if due_age > 5:
        return 2
    return 1

def GradeParse(due_age):
    months = due_age[0]
    if months < 2:
        return 'A'
    if months < 3:
        return 'B'
    if months < 6:
        return 'C'
    if months < 12:
        return 'D'
    return 'E'

def StartValueParse(lease):
    from accountables.models import Date_Value

    value = 0
    month = 12
    ref_date = previousyearlydate(lease.doc_date, datetime.date.today())

    if Date_Value.objects.exclude(state=0).filter(date=ref_date, accountable=lease).exists():
        dat_val = Date_Value.objects.exclude(state=0).get(date=ref_date, accountable=lease)
    else:
        dat_val = Date_Value.objects.exclude(state=0).filter(date__lt=ref_date, accountable=lease).latest('date')
        ref_date = dat_val.date

    while month > 0:
        value += dat_val.value
        ref_date = ref_date + relativedelta(months=1)
        if Date_Value.objects.exclude(state=0).filter(date=ref_date, accountable=lease).exists():
            dat_val = Date_Value.objects.exclude(state=0).get(date=ref_date, accountable=lease)
        month = month - 1

    return value

def FeeCountParse(lease):
    from accounting.models import Charge
    from accountables.utils.accounting_data import ACCOUNT_RECEIPT_PRIORITY

    fees = 0
    ref_date = previousyearlydate(lease.subclass_obj().doc_date, Charge.pending.accountable_receivable_age_start_date(lease, ACCOUNT_RECEIPT_PRIORITY))

    while ref_date <= datetime.date.today():
        fees += 12
        ref_date = ref_date + relativedelta(years=1)

    return fees