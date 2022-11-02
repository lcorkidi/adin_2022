from calendar import monthrange
from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, MONTHLY
from datetime import date

# returns previous or equal monthly date
def previousmonthlydate(doc_date, ref_date):
    buffer_date = date(ref_date.year + 1, doc_date.month, doc_date.day)
    while buffer_date > ref_date:
        buffer_date = buffer_date - relativedelta(months=1)
    return buffer_date

# returns next monthly date
def nextmonthlydate(doc_date, ref_date):
    buffer_date = date(ref_date.year - 1, doc_date.month, doc_date.day)
    while buffer_date <= ref_date:
        buffer_date = buffer_date + relativedelta(months=1)
    return buffer_date
    
# returns previous yearly date
def previousyearlydate(doc_date, ref_date):
    if doc_date > ref_date:
        buffer_date = doc_date
        while buffer_date > ref_date:
            buffer_date = buffer_date - relativedelta(years=1)
    else:
        buffer_date = doc_date
        while buffer_date <= ref_date:
            buffer_date = buffer_date + relativedelta(years=1)
        buffer_date = buffer_date - relativedelta(years=1)
    return buffer_date

# retunrs next yearly date 
def nextyearlydate(doc_date, ref_date):
    if doc_date <= ref_date:
        buffer_date = doc_date
        while buffer_date <= ref_date:
            buffer_date = buffer_date + relativedelta(years=1)
    else:
        buffer_date = doc_date
        while buffer_date > ref_date:
            buffer_date = buffer_date - relativedelta(years=1)
        buffer_date = buffer_date + relativedelta(years=1)
    return buffer_date
