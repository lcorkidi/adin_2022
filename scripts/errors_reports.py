import pandas as pd
from os.path import join
from adin.settings import BASE_DIR
from datetime import datetime

from scripts.utils import models_lists, models_info

def run(models_list=None):
    if not models_list:
        models_list = models_lists['errors_check']
    for item in models_list:
        errors_report = models_info[item]['model'].get_errors_report(True)
        errors_report.to_csv(join(BASE_DIR, f'_files/reports/{datetime.today().strftime("%Y-%m-%d")}_{models_info[item]["model"]._meta.model.__name__.lower()}_errors.csv'), float_format='%.0f', na_rep=None, index=False)