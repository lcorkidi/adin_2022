def lease_realty_code(realty, doc_date):
    return f'{realty.code}^{doc_date.strftime("%Y-%m-%d")}'

def accon_2_code(accon):
    return f'{accon.transaction_type}^{accon.date.strftime("%Y-%m-%d")}_{accon.accountable.code}'

def lease_realty_errors():
    from accountables.models.lease_realty import Lease_Realty

    return Lease_Realty.pending.errors()

def lease_realty_pending_date_values():
    from accountables.models.lease_realty import Lease_Realty

    return Lease_Realty.pending.date_values()

def lease_realty_pending_monthly_fee_concepts():
    from accountables.models import Transaction_Type
    from accountables.models.lease_realty import Lease_Realty

    transaction_type = Transaction_Type.objects.get(name='Canon Mensual Arriendo Inmueble')
    return Lease_Realty.pending.bulk_concept_data_dict_list(transaction_type)

def lease_realty_pending_monthly_fee_commit():
    from accountables.models.accountable import Accountable_Concept

    return Accountable_Concept.pending.commit()

def lease_realty_pending_monthly_fee_bill():
    from accountables.models.accountable import Accountable_Concept

    return Accountable_Concept.pending.bill()

def formsets_data_call(formsets_data, user):
        if formsets_data:
            formsets_data = formsets_data()
            for attr, data in formsets_data.items():
                included_states = data['included_states'](user, data['perm_dict_key'])
                if 'queryset_function' in data:
                    qs = data['queryset_function']().filter(state__in=included_states)
                    formsets_data[attr]['formset'] = data['formset'](queryset=qs)
                elif 'dict_list_function' in data:
                    dict_list = data['dict_list_function']()
                    formsets_data[attr]['formset'] = data['formset'](initial=dict_list)
                formsets_data[attr]['actions_on'] = data['actions_on'](user, data['perm_dict_key'])
            return formsets_data
        return None
