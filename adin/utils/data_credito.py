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

def StartValue(lease):
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

def FeeCount(lease):
    from accounting.models import Charge
    from accountables.utils.accounting_data import ACCOUNT_RECEIPT_PRIORITY

    fees = 0
    ref_date = previousyearlydate(lease.doc_date, Charge.pending.accountable_receivable_age_start_date(lease, ACCOUNT_RECEIPT_PRIORITY))
    if lease.end_date:
        end_date = lease.end_date
    else:
        end_date = nextyearlydate(lease.doc_date,  datetime.date.today()) - relativedelta(days=1)

    while ref_date <= end_date:
        fees += 1
        ref_date = ref_date + relativedelta(months=1)

    return fees

def SettledFeeCount(lease):
    from accounting.models import Charge
    from accountables.utils.accounting_data import ACCOUNT_RECEIPT_PRIORITY

    fees = 0
    age_start_date = Charge.pending.accountable_receivable_age_start_date(lease, ACCOUNT_RECEIPT_PRIORITY)
    ref_date = previousyearlydate(lease.doc_date, age_start_date)

    while ref_date < age_start_date:
        fees += 1
        ref_date = ref_date + relativedelta(months=1)

    return fees

def PendingFeeCount(lease):
    from accounting.models import Charge
    from accountables.utils.accounting_data import ACCOUNT_RECEIPT_PRIORITY

    due_age = Charge.pending.accountable_receivable_age_months(lease, ACCOUNT_RECEIPT_PRIORITY)
    months = due_age[0]
    days = due_age[1]

    if months == 0 and days > 5:
        months = 1
    elif days > 0:
        months += 1

    return months
    
def CityCodeParse(city):
    if city.lower() == 'cali':
        return 76001
    if city.lower() == 'medellin':
        return 5001
    if city.lower() == 'tulua':
        return 76834
    if city.lower() == 'buga':
        return 76111
    if city.lower() == 'pasto':
        return 52001
    if city.lower() == 'bogota':
        return 11001
    if city.lower() == 'bucaramanga':
        return 68001
    if city.lower() == 'yumbo':
        return 76892
    return 0

def AddressParse(address):
    code = address.get_street_type_display()
    code += " " + str(address.street_number)
    if address.street_letter != None:
        code += address.get_street_letter_display()
    if address.street_bis:
        code += 'bis'
        if address.street_bis_complement:
            code += address.get_street_bis_complement_display()
    if address.street_coordinate != None:
        code += " " + address.get_street_coordinate_display()
    code += " No " + str(address.numeral_number)
    if address.numeral_letter != None:
        code += address.get_numeral_letter_display()
    if address.numeral_bis:
        code += 'bis'
        if address.numeral_bis_complement:
            code += address.get_numeral_bis_complement_display()
    if address.numeral_coordinate != None:
        code += " " + address.get_numeral_coordinate_display()
    code += " - " + str(address.height_number)
    if address.interior_type != None:
        code += ', '
    if address.interior_group_type != None:
        code += address.get_interior_group_type_display()
        code += " " + str(address.interior_group_code) + ", "
    if address.interior_type != None:
        code += address.get_interior_type_display()
        code += " " + str(address.interior_code)

    return code
