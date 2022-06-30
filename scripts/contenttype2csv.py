import datetime
import pandas as pd
from django.contrib.contenttypes.models import ContentType

def run():
    today = datetime.date.today()

    for con_typ in ContentType.objects.all():
        class_objects = con_typ.model_class().objects.all()
        if class_objects.exists():
            pd.DataFrame(class_objects.values()).to_csv(f'_files/exports/{today.strftime("%Y-%m-%d")}_{con_typ.model}.csv', float_format='%.0f', na_rep=None)