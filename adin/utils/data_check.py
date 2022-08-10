import pandas as pd

def errors_report(cls, all=False):
    objs_df = pd.DataFrame(cls.objects.values()).drop(['state_change_user_id', 'state_change_date'], axis=1)
    errors_report = objs_df.assign(errors=objs_df[cls._meta.pk.name].apply(lambda x: cls.objects.get(pk=x).get_obj_errors()))
    if all:
        return errors_report
    return errors_report[errors_report['errors'].map(lambda x: len(x) > 0)]

def children_errors_report(cls, all=False):
    objs_df = pd.DataFrame(cls.objects.values()).drop(['state_change_user_id', 'state_change_date'], axis=1)
    errors_report = objs_df.assign(errors=objs_df[f'{cls._meta.pk.name}_id'].apply(lambda x: eval(f'cls.objects.get(pk=x).{cls._meta.pk.name}.get_obj_errors()')))
    if all:
        return errors_report
    return errors_report[errors_report['errors'].map(lambda x: len(x) > 0)]
