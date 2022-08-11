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
    month = relativedelta(months=1)
    if monthrange(doc_date.year, doc_date.month)[1] == doc_date.day:
        if monthrange(ref_date.year, ref_date.month)[1] == ref_date.day:
            return (list(rrule(MONTHLY, count=2, bymonthday=-1, dtstart=ref_date))[0]).date()
        return (list(rrule(MONTHLY, count=2, bymonthday=-1, dtstart=ref_date-month))[0]).date()
    if doc_date.day == 30:
        if monthrange(ref_date.year, ref_date.month)[1] == ref_date.day:
            if ref_date.month in [1, 3, 5, 7, 8, 10, 12]:
                return (list(rrule(MONTHLY, count=2, bymonthday=-2, dtstart=ref_date-month))[0]).date()
            return (list(rrule(MONTHLY, count=2, bymonthday=-1, dtstart=ref_date))[0]).date()
        if ref_date.day == 30:
            return (list(rrule(MONTHLY, count=2, bymonthday=-2, dtstart=ref_date))[0]).date()
        if ref_date.month in [3, 5, 7, 10, 12]:
            return (list(rrule(MONTHLY, count=2, bymonthday=-1, dtstart=ref_date-month))[0]).date()
        return (list(rrule(MONTHLY, count=2, bymonthday=-2, dtstart=ref_date-month))[0]).date()
    if doc_date.day == 29:
        if monthrange(ref_date.year, ref_date.month)[1] == ref_date.day:
            if ref_date.month in [1, 3, 5, 7, 8, 10, 12]:
                return (list(rrule(MONTHLY, count=2, bymonthday=-3, dtstart=ref_date-month))[0]).date()
            if ref_date.month == 2:
                return (list(rrule(MONTHLY, count=2, bymonthday=-1, dtstart=ref_date-month))[1]).date()
            return (list(rrule(MONTHLY, count=2, bymonthday=-2, dtstart=ref_date-month))[1]).date()
        if ref_date.day == 30:
            return (list(rrule(MONTHLY, count=2, bymonthday=-3, dtstart=ref_date))[0]).date()
        if ref_date.month in [5, 7, 10, 12]:
            return (list(rrule(MONTHLY, count=2, bymonthday=-2, dtstart=ref_date-month))[0]).date()
        if ref_date.month == 3:
            return (list(rrule(MONTHLY, count=2, bymonthday=-1, dtstart=ref_date-month))[0]).date()
        return (list(rrule(MONTHLY, count=2, bymonthday=-3, dtstart=ref_date-month))[0]).date()
    if ref_date.day >= doc_date.day:
        return date(ref_date.year, ref_date.month, doc_date.day)
    return date((ref_date-month).year, (ref_date-month).month, doc_date.day)

# returns next monthly date
def nextmonthlydate(doc_date, ref_date):
    buffer_date = date(ref_date.year - 1, doc_date.month, doc_date.day)
    while buffer_date <= ref_date:
        buffer_date = buffer_date + relativedelta(months=1)
    return buffer_date
    month = relativedelta(months=1)
    if monthrange(doc_date.year, doc_date.month)[1] == doc_date.day:
        if monthrange(ref_date.year, ref_date.month)[1] == ref_date.day:
            return (list(rrule(MONTHLY, count=2, bymonthday=-1, dtstart=ref_date))[1]).date()
        return (list(rrule(MONTHLY, count=2, bymonthday=-1, dtstart=ref_date))[0]).date()
    if doc_date.day == 30:
        if monthrange(ref_date.year, ref_date.month)[1] == ref_date.day:
            if ref_date.month in [1, 3, 5, 8, 10]:
                return (list(rrule(MONTHLY, count=2, bymonthday=-1, dtstart=ref_date))[1]).date()
            return (list(rrule(MONTHLY, count=2, bymonthday=-2, dtstart=ref_date))[0]).date()
        if ref_date.day == 30:
            return (list(rrule(MONTHLY, count=2, bymonthday=-1, dtstart=ref_date))[1]).date()
        if ref_date.month in [1, 3, 5, 8, 10]:
            return (list(rrule(MONTHLY, count=2, bymonthday=-2, dtstart=ref_date))[0]).date()
        return (list(rrule(MONTHLY, count=2, bymonthday=-1, dtstart=ref_date))[0]).date()
    if doc_date.day == 29:
        if monthrange(ref_date.year, ref_date.month)[1] == ref_date.day:
            if ref_date.month in [3, 5, 8, 10]:
                return (list(rrule(MONTHLY, count=2, bymonthday=-2, dtstart=ref_date))[0]).date()
            if ref_date.month in [1, 3, 5, 8, 10]:
                return (list(rrule(MONTHLY, count=2, bymonthday=-1, dtstart=ref_date))[1]).date()
            return (list(rrule(MONTHLY, count=2, bymonthday=-3, dtstart=ref_date))[0]).date()
        if ref_date.day == 30:
            return (list(rrule(MONTHLY, count=2, bymonthday=-2, dtstart=ref_date))[1]).date()
        if ref_date.month in [1, 3, 5, 8, 10]:
            return (list(rrule(MONTHLY, count=2, bymonthday=-3, dtstart=ref_date))[0]).date()
        return (list(rrule(MONTHLY, count=2, bymonthday=-2, dtstart=ref_date))[0]).date()
    if ref_date.day >= doc_date.day:
        return date((ref_date+month).year, (ref_date+month).month, doc_date.day)
    return date(ref_date.year, ref_date.month, doc_date.day)
    
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
        
    if monthrange(doc_date.year, doc_date.month)[1] - doc_date.day == 0 and doc_date.month == 2:
        return list(rrule(MONTHLY, count=13, bymonthday=-1, dtstart=date(ref_date.year - 1, doc_date.month, 28)))[12].date()
    return date(ref_date.year, doc_date.month, doc_date.day) if date(ref_date.year, doc_date.month, doc_date.day) <= ref_date else date(ref_date.year - 1, doc_date.month, doc_date.day)

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

    if monthrange(doc_date.year, doc_date.month)[1] - doc_date.day == 0 and doc_date.month == 2:
        return list(rrule(MONTHLY, count=13, bymonthday=-1, dtstart=date(ref_date.year, doc_date.month, 28)))[12].date()
    return date(ref_date.year + 1, doc_date.month, doc_date.day) if date(ref_date.year, doc_date.month, doc_date.day) <= ref_date else date(ref_date.year, doc_date.month, doc_date.day)
