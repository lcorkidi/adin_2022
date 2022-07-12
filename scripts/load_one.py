from scripts.utils import data_load, models_info

def run(model):
    data_load(models_info, load_list=[model])