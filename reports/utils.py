import pandas as pd
import datetime

from accounting.core.structure import Account_Structure
from people.models import Person
from accounting.models import Account, Charge

def df_to_dict(df):
    return df.to_dict('records')

def ledger_from_db():
    try:    
        ledger = pd.DataFrame(Charge.objects.values('ledger', 'ledger__date', 'ledger__third_party', 'concept__accountable', 'concept__transaction_type', 'concept__date', 'account', 'value'))
        ledger = ledger.rename(columns={'ledger__date':'date', 'ledger__third_party':'third_party', 'concept__accountable':'accountable','concept__transaction_type':'concept'})
        return ledger.assign(third_party=ledger.third_party.apply(lambda x: Person.objects.get(pk=x).complete_name),
                    debit = ledger.apply(lambda x: x.value if x.value > 0 else 0, axis=1),
                    credit = ledger.apply(lambda x: -x.value if x.value < 0 else 0, axis=1))
    except:
        return

def account_charges(ledger, account, start_date=datetime.date(2021, 1, 1), end_date=datetime.date.today(), value=0):
    account_charges = ledger[(ledger.account == account) & (ledger.date >= start_date) & (ledger.date <= end_date)]
    if value < 0:
        account_charges = account_charges[account_charges.value < 0]
    if value > 0:
        account_charges = account_charges[account_charges.value > 0]
    return account_charges

def account_balance(ledger, account, start_date=datetime.date(2021, 1, 1), end_date=datetime.date.today()):
    account_charges = ledger[ledger.account == account]
    balance = account_charges\
                .assign(previous_balance = account_charges.apply(lambda x: x.value if x.date < start_date else 0, axis=1),
                    debit = account_charges.apply(lambda x: x.value if x.date >= start_date and  x.date <= end_date and x.value > 0 else 0, axis=1),
                    credit = account_charges.apply(lambda x: -x.value if x.date >= start_date and  x.date <= end_date and x.value < 0 else 0, axis=1),
                    value = account_charges.apply(lambda x: x.value if x.date <= end_date else 0, axis=1))\
                .rename(columns={'value': 'closing_balance'})\
                .sum(numeric_only=True)
    balance['account'] = account
    return pd.concat([balance, pd.Series([Account.account_name(account), 0, True], index=['name', 'priority', 'chargeable'])]).to_dict()

def ledger_level_balance(ledger, level=1, start_date=datetime.date(datetime.date.today().year, 1, 1), end_date=datetime.date.today()):
    ledger = ledger\
                .assign(**{f'level{level+1}': code for level, code in ledger.account.apply(lambda x: Account_Structure.levels_full(x)).items()})\
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

def ledger_balance(ledger, level=1, start_date=None, end_date=None):
    balances_list = []
    for l in range(1, level+1):
        balance_params = { 'ledger': ledger }
        balance_params['level'] = l
        if start_date:
            balance_params['start_date'] = start_date
        if end_date:
            balance_params['end_date'] = end_date
        loop_balance = ledger_level_balance(**balance_params).assign(priority=level-l+1)
        balances_list.append(loop_balance)
    balances = pd.concat(balances_list)
    balances = balances.assign(**{f'level{level+1}': code for level, code in balances.account.apply(lambda x: Account_Structure.levels_nan(x)).items()},
                    chargeable = balances.apply(lambda x: True if Account.chargeable(x.account) and x.priority == 1 else False, axis=1))
    sort_list = []
    for l in range(1,level):
        sort_list.append(f'level{l}')
    sort_list.append('priority')
    return balances.sort_values(by=sort_list)

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
