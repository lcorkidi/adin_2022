from scripts.utils import data_load, models_info, models_lists

def run(list):
    data_load(models_info, load_list=models_lists[list])