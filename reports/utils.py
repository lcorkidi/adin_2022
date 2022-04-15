import pandas as pd
import datetime

from accounting.core.structure import Account_Structure
from people.models import Person
from accounting.models import Account, Charge

def get_ledger_db():    
    ledger = pd.DataFrame(Charge.objects.values('ledger', 'ledger__date', 'ledger__third_party', 'concept__accountable', 'concept__transaction_type', 'concept__date', 'account', 'value'))
    ledger = ledger.rename(columns={'ledger__date':'date', 'ledger__third_party':'third_party', 'concept__accountable':'accountable','concept__transaction_type':'concept'})
    return ledger\
            .assign(third_party=ledger.third_party.apply(lambda x: Person.objects.get(pk=x).complete_name),
                debit = ledger.apply(lambda x: x.value if x.value > 0 else 0, axis=1),
                credit = ledger.apply(lambda x: -x.value if x.value < 0 else 0, axis=1))

def df_to_dict(df):
    return df.to_dict('records')

def balance(ledger, level=1, start_date=datetime.date(datetime.date.today().year, 1, 1), end_date=datetime.date.today()):
    ledger = ledger.assign(**{f'level{level+1}': code for level, code in ledger.account.apply(lambda x: Account_Structure.levels(x)).items()})\
                .assign(previous_balance = ledger.apply(lambda x: x.value if x.date < start_date else 0, axis=1),
                    debit = ledger.apply(lambda x: x.value if x.date >= start_date and  x.date <= end_date and x.value > 0 else 0, axis=1),
                    credit = ledger.apply(lambda x: -x.value if x.date >= start_date and  x.date <= end_date and x.value < 0 else 0, axis=1),
                    value = ledger.apply(lambda x: x.value if x.date <= end_date else 0, axis=1))\
                .groupby(f'level{level}')\
                .sum()\
                .rename(columns={'value':'closing_balance'})
    ledger = ledger.assign(account = ledger.index)
    ledger = ledger.assign(name = ledger.account.apply(lambda x: Account.account_name(x)))
    return ledger[['account', 'name', 'previous_balance', 'debit', 'credit', 'closing_balance']]

def charges_pending(df, receivable=True):    
    # query obligation establishing charges and annottate pending_value
    obligation_charges = df.query(f'value {">" if receivable else "<"} 0').assign(pending_value = abs(df.value))
    
    # sum obligation settling charges
    settling_sum = abs(df.query(f'value {"<" if receivable else ">"} 0')['value'].sum())
    
    # each pending_value in query df is tallied against the settling sum and is adjusted accordingly
    buffer_sum = 0
    for pe_index, pe_row in obligation_charges.iterrows():
        buffer_value = pe_row['pending_value']
        if buffer_sum + buffer_value <= settling_sum:
            obligation_charges.at[pe_index, 'pending_value'] = 0
        elif buffer_sum < settling_sum:
            obligation_charges.at[pe_index, 'pending_value'] = buffer_value - (settling_sum - buffer_sum)
        buffer_sum += buffer_value
        
    return  obligation_charges.assign(account = obligation_charges.account.apply(lambda x: Account.account_name(x))).query(f'pending_value > 0')
