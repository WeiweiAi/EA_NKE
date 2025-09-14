import csv
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

def vary_pH():

    c_Nai=10.0 #mM, default 10,  4–16 mM https://doi.org/10.1161/01.CIR.0000016701.85760.97
    c_Nao=140.0 #mM  ∼140 mM https://doi.org/10.1016/S0008-6363(02)00656-9
    c_Ki=145 #mM default 145, 140-150 https://doi.org/10.1159/000446268
    c_Ko=4.5 #mM 3.5-5.0, default 4.5
    c_ATP=1 #mM ~1 mM https://doi.org/10.1073/pnas.2318535121, previously estimated 8 to 10 mM level, 
    c_ADP=0.035  #mM default 0.035,  20–40 μM https://doi.org/10.1016/S0005-2728(01)00247-X, 
    pH=[7.15, 7.2, 7.25,7.3, 7.4] # default 7.2, range 7.15-7.25
    #c_H=10**(-pH)*1000 #mM
    c_Pi=0.8 #mM 1-10  https://pmc.ncbi.nlm.nih.gov/articles/PMC4552539/, default 0.8

    # construct the changes dictionary for different pH values    
    changes=[]
    for i in range(len(pH)):
        c_H=10**(-pH[i])*1000 #mM
        changes_dict={'c_Nai':{'component':component_name,'name':'c_Nai','newValue':str(c_Nai)},
                      'c_Nao':{'component':component_name,'name':'c_Nao','newValue':str(c_Nao)},
                      'c_Ki':{'component':component_name,'name':'c_Ki','newValue':str(c_Ki)},
                      'c_Ko':{'component':component_name,'name':'c_Ko','newValue':str(c_Ko)},
                      'c_ATP':{'component':component_name,'name':'c_ATP','newValue':str(c_ATP)},
                      'c_ADP':{'component':component_name,'name':'c_ADP','newValue':str(c_ADP)},
                      'c_Pi':{'component':component_name,'name':'c_Pi','newValue':str(c_Pi)},
                      'c_H':{'component':component_name,'name':'c_H','newValue':str(c_H)}
                      }
        changes.append(changes_dict)
    filename= component_name +'_pH.json' 
    json_path = parent_path / filename
    write_json(json_path, changes)

def vary_Nai():

    filename= component_name +'_Nai.json'
    json_path = parent_path / filename

    c_Nai=[4, 6, 8, 10, 12, 14, 16] #mM, default 10,  4–16 mM https://doi.org/10.1161/01.CIR.0000016701.85760.97
    c_Nao=140.0 #mM  ∼140 mM https://doi.org/10.1016/S0008-6363(02)00656-9
    c_Ki=145 #mM 140-150 https://doi.org/10.1159/000446268
    c_Ko=4.5 #mM 3.5-5.0, default 4.5
    c_ATP=1 #mM ~1 mM https://doi.org/10.1073/pnas.2318535121, previously estimated 8 to 10 mM level, 
    c_ADP=0.035 #mM 20–40 μM https://doi.org/10.1016/S0005-2728(01)00247-X, default 0.035
    pH=7.2# default 7.2, range 7.15-7.25
    c_H=10**(-pH)*1000 #mM
    c_Pi=0.8 #mM 1-10  https://pmc.ncbi.nlm.nih.gov/articles/PMC4552539/, default 0.8

    # construct the changes dictionary
    changes=[]
    for i in range(len(c_Nai)):
        changes_dict={'c_Nai':{'component':component_name,'name':'c_Nai','newValue':str(c_Nai[i])},
                      'c_Nao':{'component':component_name,'name':'c_Nao','newValue':str(c_Nao)},
                      'c_Ki':{'component':component_name,'name':'c_Ki','newValue':str(c_Ki)},
                      'c_Ko':{'component':component_name,'name':'c_Ko','newValue':str(c_Ko)},
                      'c_ATP':{'component':component_name,'name':'c_ATP','newValue':str(c_ATP)},
                      'c_ADP':{'component':component_name,'name':'c_ADP','newValue':str(c_ADP)},
                      'c_Pi':{'component':component_name,'name':'c_Pi','newValue':str(c_Pi)},
                      'c_H':{'component':component_name,'name':'c_H','newValue':str(c_H)}
                      }
        changes.append(changes_dict)

    write_json(json_path, changes)
def vary_Ko():
    filename= component_name +'_Ko.json'
    json_path = parent_path / filename

    c_Nai=10.0 #mM, default 10,  4–16 mM https://doi.org/10.1161/01.CIR.0000016701.85760.97
    c_Nao=140.0 #mM  ∼140 mM https://doi.org/10.1016/S0008-6363(02)00656-9
    c_Ki=145 #mM 140-150 https://doi.org/10.1159/000446268
    c_Ko=[3.5, 4, 4.5,5, 5.5] #mM 3.5-5.0
    c_ATP=1 #mM ~1 mM https://doi.org/10.1073/pnas.2318535121, previously estimated 8 to 10 mM level, 
    c_ADP=0.035 #mM 20–40 μM https://doi.org/10.1016/S0005-2728(01)00247-X, default 0.035
    pH=7.2# default 7.2, range 7.15-7.25
    c_H=10**(-pH)*1000 #mM
    c_Pi=0.8 #mM 1-10  https://pmc.ncbi.nlm.nih.gov/articles/PMC4552539/, default 0.8

    # construct the changes dictionary
    changes=[]
    for i in range(len(c_Ko)):
        changes_dict={'c_Nai':{'component':component_name,'name':'c_Nai','newValue':str(c_Nai)},
                      'c_Nao':{'component':component_name,'name':'c_Nao','newValue':str(c_Nao)},
                      'c_Ki':{'component':component_name,'name':'c_Ki','newValue':str(c_Ki)},
                      'c_Ko':{'component':component_name,'name':'c_Ko','newValue':str(c_Ko[i])},
                      'c_ATP':{'component':component_name,'name':'c_ATP','newValue':str(c_ATP)},
                      'c_ADP':{'component':component_name,'name':'c_ADP','newValue':str(c_ADP)},
                      'c_Pi':{'component':component_name,'name':'c_Pi','newValue':str(c_Pi)},
                      'c_H':{'component':component_name,'name':'c_H','newValue':str(c_H)}
                      }
        changes.append(changes_dict)

    write_json(json_path, changes)
def vary_ATP():    
    filename= component_name +'_ATP.json'
    json_path = parent_path / filename
    c_Nai=10.0 #mM, default 10,  4–16 mM https://doi.org/10.1161/01.CIR.0000016701.85760.97
    c_Nao=140.0 #mM  ∼140 mM https://doi.org/10.1016/S0008-6363(02)00656-9
    c_Ki=145 #mM 140-150 https://doi.org/10.1159/000446268  
    c_Ko=4.5 #mM 3.5-5.0, default 4.5
    c_ATP=[0.5, 1, 4, 7, 10] #mM ~1 mM https://doi.org/10.1073/pnas.2318535121, previously estimated 8 to 10 mM level, 
    c_ADP=0.035 #mM 20–40 μM https://doi.org/10.1016/S0005-2728(01)00247-X, default 0.035
    pH=7.2# default 7.2, range 7.15-7.25
    c_H=10**(-pH)*1000 #mM
    c_Pi=0.8 #mM 1-10  https://pmc.ncbi.nlm.nih.gov/articles/PMC4552539/, default 0.8

    # construct the changes dictionary
    changes=[]
    for i in range(len(c_ATP)):
        changes_dict={'c_Nai':{'component':component_name,'name':'c_Nai','newValue':str(c_Nai)},
                      'c_Nao':{'component':component_name,'name':'c_Nao','newValue':str(c_Nao)},
                      'c_Ki':{'component':component_name,'name':'c_Ki','newValue':str(c_Ki)},
                      'c_Ko':{'component':component_name,'name':'c_Ko','newValue':str(c_Ko)},
                      'c_ATP':{'component':component_name,'name':'c_ATP','newValue':str(c_ATP[i])},
                      'c_ADP':{'component':component_name,'name':'c_ADP','newValue':str(c_ADP)},
                      'c_Pi':{'component':component_name,'name':'c_Pi','newValue':str(c_Pi)},
                      'c_H':{'component':component_name,'name':'c_H','newValue':str(c_H)}
                      }
        changes.append(changes_dict)

    write_json(json_path, changes)
def vary_ADP():
    filename= component_name +'_ADP.json'
    json_path = parent_path / filename
    c_Nai=10.0 #mM, default 10,  4–16 mM https://doi.org/10.1161/01.CIR.0000016701.85760.97
    c_Nao=140.0 #mM  ∼140 mM https://doi.org/10.1016/S0008-6363(02)00656-9
    c_Ki=145 #mM 140-150 https://doi.org/10.1159/000446268  
    c_Ko=4.5 #mM 3.5-5.0, default 4.5
    c_ATP=1 #mM ~1 mM https://doi.org/10.1073/pnas.2318535121, previously estimated 8 to 10 mM level,
    c_ADP=[0.01, 0.02, 0.035, 0.05, 0.07] #mM 20–40 μM https://doi.org/10.1016/S0005-2728(01)00247-X, default 0.035
    pH=7.2# default 7.2, range 7.15-7.25
    c_H=10**(-pH)*1000 #mM
    c_Pi=0.8 #mM 1-10  https://pmc.ncbi.nlm.nih.gov/articles/PMC4552539/, default 0.8
    # construct the changes dictionary
    changes=[]
    for i in range(len(c_ADP)):
        changes_dict={'c_Nai':{'component':component_name,'name':'c_Nai','newValue':str(c_Nai)},
                      'c_Nao':{'component':component_name,'name':'c_Nao','newValue':str(c_Nao)},
                      'c_Ki':{'component':component_name,'name':'c_Ki','newValue':str(c_Ki)},
                      'c_Ko':{'component':component_name,'name':'c_Ko','newValue':str(c_Ko)},
                      'c_ATP':{'component':component_name,'name':'c_ATP','newValue':str(c_ATP)},
                      'c_ADP':{'component':component_name,'name':'c_ADP','newValue':str(c_ADP[i])},
                      'c_Pi':{'component':component_name,'name':'c_Pi','newValue':str(c_Pi)},
                      'c_H':{'component':component_name,'name':'c_H','newValue':str(c_H)}
                      }
        changes.append(changes_dict)

    write_json(json_path, changes)
def vary_Pi():
    filename= component_name +'_Pi.json'
    json_path = parent_path / filename
    c_Nai=10.0 #mM, default 10,  4–16 mM https://doi.org/10.1161/01.CIR.0000016701.85760.97
    c_Nao=140.0 #mM  ∼140 mM https://doi.org/10.1016/S0008-6363(02)00656-9
    c_Ki=145 #mM 140-150 https://doi.org/10.1159/000446268  
    c_Ko=4.5 #mM 3.5-5.0, default 4.5
    c_ATP=1 #mM ~1 mM https://doi.org/10.1073/pnas.2318535121, previously estimated 8 to 10 mM level,
    c_ADP=0.035 #mM 20–40 μM https://doi.org/10.1016/S0005-2728(01)00247-X, default 0.035
    pH=7.2# default 7.2, range 7.15-7.25
    c_H=10**(-pH)*1000 #mM
    c_Pi=[0.8, 1, 4, 7, 10] #mM 1-10  https://pmc.ncbi.nlm.nih.gov/articles/PMC4552539/, default 0.8

    # construct the changes dictionary
    changes=[]
    for i in range(len(c_Pi)):
        changes_dict={'c_Nai':{'component':component_name,'name':'c_Nai','newValue':str(c_Nai)},
                      'c_Nao':{'component':component_name,'name':'c_Nao','newValue':str(c_Nao)},
                      'c_Ki':{'component':component_name,'name':'c_Ki','newValue':str(c_Ki)},
                      'c_Ko':{'component':component_name,'name':'c_Ko','newValue':str(c_Ko)},
                      'c_ATP':{'component':component_name,'name':'c_ATP','newValue':str(c_ATP)},
                      'c_ADP':{'component':component_name,'name':'c_ADP','newValue':str(c_ADP)},
                      'c_Pi':{'component':component_name,'name':'c_Pi','newValue':str(c_Pi[i])},
                      'c_H':{'component':component_name,'name':'c_H','newValue':str(c_H)}
                      }
        changes.append(changes_dict)

    write_json(json_path, changes)
def default_conditions():
    filename= component_name +'_default.json'
    json_path = parent_path / filename
    c_Nai=10.0 #mM, default 10,  4–16 mM https://doi.org/10.1161/01.CIR.0000016701.85760.97
    c_Nao=140.0 #mM  ∼140 mM https://doi.org/10.1016/S0008-6363(02)00656-9
    c_Ki=145 #mM 140-150 https://doi.org/10.1159/000446268  
    c_Ko=4.5 #mM 3.5-5.0, default 4.5
    c_ATP=1 #mM ~1 mM https://doi.org/10.1073/pnas.2318535121, previously estimated 8 to 10 mM level,
    c_ADP=0.035 #mM 20–40 μM https://doi.org/10.1016/S0005-2728(01)00247-X, default 0.035
    pH=7.2# default 7.2, range 7.15-7.25
    c_H=10**(-pH)*1000 #mM
    c_Pi=[0.8] #mM 1-10  https://pmc.ncbi.nlm.nih.gov/articles/PMC4552539/, default 0.8

    # construct the changes dictionary
    changes=[]
    for i in range(len(c_Pi)):
        changes_dict={'c_Nai':{'component':component_name,'name':'c_Nai','newValue':str(c_Nai)},
                      'c_Nao':{'component':component_name,'name':'c_Nao','newValue':str(c_Nao)},
                      'c_Ki':{'component':component_name,'name':'c_Ki','newValue':str(c_Ki)},
                      'c_Ko':{'component':component_name,'name':'c_Ko','newValue':str(c_Ko)},
                      'c_ATP':{'component':component_name,'name':'c_ATP','newValue':str(c_ATP)},
                      'c_ADP':{'component':component_name,'name':'c_ADP','newValue':str(c_ADP)},
                      'c_Pi':{'component':component_name,'name':'c_Pi','newValue':str(c_Pi[i])},
                      'c_H':{'component':component_name,'name':'c_H','newValue':str(c_H)}
                      }
        changes.append(changes_dict)

    write_json(json_path, changes)

list_vars=['c_Nai', 'c_Nao', 'c_Ki', 'c_Ko', 'c_ATP', 'c_ADP', 'c_Pi', 'u_0_Vm','T']
def get_conditions_from_csv(csv_file='experimental_conditions.csv',list_vars=[]):
    # Read the csv file
    df = pd.read_csv(csv_file)
    changes=[]
    
    # Iterate through each row and create a JSON file
    for index, row in df.iterrows():
        changes_dict = {}
        for col in list_vars:
            if col =='pH':
                c_H=10**(-row[col])*1000 #mM
                changes_dict['c_H'] = {
                    'component': component_name,
                    'name': 'c_H',
                    'newValue': str(c_H)
                }
            else:
                changes_dict[col] = {
                    'component': component_name,
                    'name': col,
                    'newValue': str(row[col])
                }
        changes.append(changes_dict)
    return changes

data_path=Path(__file__).parent.parent / 'cad' /'data'

def write_fig3a_conditions():
    csv_file=data_path / 'Terkildsen_NaK_kinetic_Nai_cond.csv'
    fig3a_conditions=get_conditions_from_csv(csv_file=csv_file,list_vars=list_vars)
    filename='Terkildsen_NaK_kinetic_Nai_cond.json'
    json_path = parent_path / filename
    write_json(json_path, fig3a_conditions)

def write_fig3b_conditions():
    csv_file=data_path / 'Terkildsen_NaK_kinetic_Ke_cond.csv'
    fig3b_conditions=get_conditions_from_csv(csv_file=csv_file,list_vars=list_vars)
    filename='Terkildsen_NaK_kinetic_Ke_cond.json'
    json_path = parent_path / filename
    write_json(json_path, fig3b_conditions)

def write_fig3c_conditions():
    csv_file=data_path / 'Terkildsen_NaK_kinetic_ATP_cond.csv'
    fig3c_conditions=get_conditions_from_csv(csv_file=csv_file,list_vars=list_vars)
    filename='Terkildsen_NaK_kinetic_ATP_cond.json'
    json_path = parent_path / filename
    write_json(json_path, fig3c_conditions)

def write_fig5_conditions():
    csv_file=data_path / 'Terkildsen_NaK_kinetic_volt_cond.csv'
    fig5_conditions=get_conditions_from_csv(csv_file=csv_file,list_vars=list_vars)
    filename='Terkildsen_NaK_kinetic_volt_cond.json'
    json_path = parent_path / filename
    write_json(json_path, fig5_conditions)

def default_conditions_physiome():
    filename= component_name +'_default_physiome.json'
    json_path = parent_path / filename
    c_Nai=50 #mM, default 10,  4–16 mM https://doi.org/10.1161/01.CIR.0000016701.85760.97
    c_Nao=150.0 #mM  ∼140 mM https://doi.org/10.1016/S0008-6363(02)00656-9
    c_Ki=0.001#mM 140-150 https://doi.org/10.1159/000446268  
    c_Ko=5.4 #mM 3.5-5.0, default 4.5
    c_ATP=10 #mM ~1 mM https://doi.org/10.1073/pnas.2318535121, previously estimated 8 to 10 mM level,
    c_ADP=0.001 #mM 20–40 μM https://doi.org/10.1016/S0005-2728(01)00247-X, default 0.035
    pH=7.4# default 7.2, range 7.15-7.25
    c_H=10**(-pH)*1000 #mM
    c_Pi=[0.001] #mM 1-10  https://pmc.ncbi.nlm.nih.gov/articles/PMC4552539/, default 0.8

    # construct the changes dictionary
    changes=[]
    for i in range(len(c_Pi)):
        changes_dict={'c_Nai':{'component':component_name,'name':'c_Nai','newValue':str(c_Nai)},
                      'c_Nao':{'component':component_name,'name':'c_Nao','newValue':str(c_Nao)},
                      'c_Ki':{'component':component_name,'name':'c_Ki','newValue':str(c_Ki)},
                      'c_Ko':{'component':component_name,'name':'c_Ko','newValue':str(c_Ko)},
                      'c_ATP':{'component':component_name,'name':'c_ATP','newValue':str(c_ATP)},
                      'c_ADP':{'component':component_name,'name':'c_ADP','newValue':str(c_ADP)},
                      'c_Pi':{'component':component_name,'name':'c_Pi','newValue':str(c_Pi[i])},
                      'c_H':{'component':component_name,'name':'c_H','newValue':str(c_H)}
                      }
        changes.append(changes_dict)

    write_json(json_path, changes)

if __name__ == "__main__":
    vary_Nai()
    vary_Ko()
    vary_ATP()
    vary_Pi()
    vary_ADP()
    vary_pH()
    write_fig3a_conditions()
    write_fig3b_conditions()
    write_fig3c_conditions()
    write_fig5_conditions()
    default_conditions_physiome()
    default_conditions()