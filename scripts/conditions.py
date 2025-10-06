from calendar import c
import sys
import os
# Add parent directory to sys.path for module imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
# Import Path for filesystem operations
from pathlib import Path
from exp_conditions import read_json

simulation_path = Path(__file__).parent.parent / 'cad' / 'models' / 'simulation'
path_ = Path(__file__).parent.parent / 'cad' /  'data'

df_conditions = pd.DataFrame()

json_file_conditions = ['ATP','ADP','Pi','pH','Nai','Ko']
for jf in json_file_conditions:
    json_file=simulation_path / f'NKE_BG_Env_{jf}.json'
    dict_conditions=read_json(json_file)
    values=[]
    df_conditions = pd.DataFrame(columns=[jf])
    for dict_condition in dict_conditions:
        if jf in ['pH']:
            values+=[dict_condition['pH']['newValue']]
        else:        
            values+=[dict_condition['c_'+jf]['newValue']]    
    df_conditions[jf]=values
    # save to csv
    csv_file=simulation_path / f'{jf}.csv'
    df_conditions.to_csv(csv_file,index=False)


    