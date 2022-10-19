def related_data_formsets_call(related_data, pk, user):
        if related_data:
            related_data = related_data()
            for attr, data in related_data.items():
                model_str = data['class'].__name__
                included_states = data['included_states'](user, model_str)
                filter_expresion = {data['filter_expresion']:pk}
                related_data[attr]['formset'] = data['formset'](queryset=data['class'].objects.filter(state__in=included_states).filter(**filter_expresion), rel_pk=pk)
                related_data[attr]['actions_on'] = data['actions_on'](user, model_str)
            return related_data
        return None
