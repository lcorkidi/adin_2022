import pandas as pd
from datetime import datetime
from scripts.utils import df2objs, classes_list
 
_raw_data_info = pd.read_json('_files/_raw_data_info.json')

def run(classes):
    counter = 0
    timers = { 'dt0': datetime.now()}

    for class_name in classes_list[classes]:
        df2objs(pd.read_csv(f'_files/{class_name}.csv'), _raw_data_info, True)
        counter += 1
        timers[f'dt{counter}'] = datetime.now()
        print('{}: {}'.format(class_name, timers[f'dt{counter}']-timers[f'dt{counter-1}']))

    print('total: {}'.format(timers[f'dt{counter}']-timers['dt0']))
    