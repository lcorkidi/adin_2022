def lease_realty_code(realty, doc_date):
    return f'{realty.code}^{doc_date.strftime("%Y-%m-%d")}'

def accon_2_code(accon):
    return f'{accon.transaction_type}^{accon.date.strftime("%Y-%m-%d")}_{accon.accountable.code}'
