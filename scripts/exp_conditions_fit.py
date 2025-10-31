import sys
import os
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pathlib import Path
import pandas as pd

def write_json(json_path, changes):
    with open(json_path, 'w') as f:
        json.dump(changes, f, indent=4)

def read_json(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data

parent_path = Path(__file__).parent.parent / 'cad' / 'models' /'simulation'

component_name='NKE_BG_Env'

list_vars=['c_Nai', 'c_Nao', 'c_Ki', 'c_Ko', 'c_ATP', 'c_ADP', 'c_Pi', 'u_0_Vm','T','pH']
def get_conditions_from_csv(csv_file='experimental_conditions.csv',list_vars=[]):
    # Read the csv file
    df = pd.read_csv(csv_file)
    changes=[]
    
    # Iterate through each row and create a JSON file
    for index, row in df.iterrows():
        changes_dict = {}
        for col in list_vars:
                changes_dict[col] = {
                    'component': component_name,
                    'name': col,
                    'newValue': str(row[col])
                }
        changes.append(changes_dict)
    return changes

data_path=Path(__file__).parent.parent / 'cad' /'data'

def write_fig2a_1_conditions():
    csv_file=data_path / 'fig2a_cond_1.csv'
    fig2a_1_conditions=get_conditions_from_csv(csv_file=csv_file,list_vars=list_vars)
    filename='fig2a_cond_1.json'
    json_path = parent_path / filename
    write_json(json_path, fig2a_1_conditions)

def write_fig2a_2_conditions():
    csv_file=data_path / 'fig2a_cond_2.csv'
    fig2a_2_conditions=get_conditions_from_csv(csv_file=csv_file,list_vars=list_vars)
    filename='fig2a_cond_2.json'
    json_path = parent_path / filename
    write_json(json_path, fig2a_2_conditions)

def write_fig2a_3_conditions():
    csv_file=data_path / 'fig2a_cond_3.csv'
    fig2a_3_conditions=get_conditions_from_csv(csv_file=csv_file,list_vars=list_vars)
    filename='fig2a_cond_3.json'
    json_path = parent_path / filename
    write_json(json_path, fig2a_3_conditions)

def write_fig2a_4_conditions():
    csv_file=data_path / 'fig2a_cond_4.csv'
    fig2a_4_conditions=get_conditions_from_csv(csv_file=csv_file,list_vars=list_vars)
    filename='fig2a_cond_4.json'
    json_path = parent_path / filename
    write_json(json_path, fig2a_4_conditions)

def write_fig2b_1_conditions():
    csv_file=data_path / 'fig2b_cond_1.csv'
    fig2b_1_conditions=get_conditions_from_csv(csv_file=csv_file,list_vars=list_vars)
    filename='fig2b_cond_1.json'
    json_path = parent_path / filename
    write_json(json_path, fig2b_1_conditions)

def write_fig2b_2_conditions():
    csv_file=data_path / 'fig2b_cond_2.csv'
    fig2b_2_conditions=get_conditions_from_csv(csv_file=csv_file,list_vars=list_vars)
    filename='fig2b_cond_2.json'
    json_path = parent_path / filename
    write_json(json_path, fig2b_2_conditions)

def write_fig2b_3_conditions():
    csv_file=data_path / 'fig2b_cond_3.csv'
    fig2b_3_conditions=get_conditions_from_csv(csv_file=csv_file,list_vars=list_vars)
    filename='fig2b_cond_3.json'
    json_path = parent_path / filename
    write_json(json_path, fig2b_3_conditions)

def write_fig3a_conditions():
    csv_file=data_path / 'fig3a_cond.csv'
    fig3a_conditions=get_conditions_from_csv(csv_file=csv_file,list_vars=list_vars)
    filename='fig3a_cond.json'
    json_path = parent_path / filename
    write_json(json_path, fig3a_conditions)

def write_fig3b_conditions():
    csv_file=data_path / 'fig3b_cond.csv'
    fig3b_conditions=get_conditions_from_csv(csv_file=csv_file,list_vars=list_vars)
    filename='fig3b_cond.json'
    json_path = parent_path / filename
    write_json(json_path, fig3b_conditions)

def write_fig3c_conditions():
    csv_file=data_path / 'fig3c_cond.csv'
    fig3c_conditions=get_conditions_from_csv(csv_file=csv_file,list_vars=list_vars)
    filename='fig3c_cond.json'
    json_path = parent_path / filename
    write_json(json_path, fig3c_conditions)

if __name__ == "__main__":
    write_fig2a_1_conditions()
    write_fig2a_2_conditions()
    write_fig2a_3_conditions()
    write_fig2a_4_conditions()
    write_fig2b_1_conditions()
    write_fig2b_2_conditions()
    write_fig2b_3_conditions()
    write_fig3a_conditions()
    write_fig3b_conditions()
    write_fig3c_conditions()
    