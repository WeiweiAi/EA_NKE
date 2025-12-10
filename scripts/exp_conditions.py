import copy
import sys
import os
import json
import numpy as np
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
R=8.314 #J mol-1 K-1
T=310 #K, 37C

deltaG_ATP=np.array([-46*1000,-48*1000,-50*1000,-52*1000,-54*1000,-56*1000,-57*1000,-57.25*1000,-57.5*1000,-58*1000,-58.25*1000,-59*1000,-60*1000,-62*1000]) #J/mol, literature values range from -45 to -60 kJ/mol
deltaG_ATP_0=11.9*1000 #J/mol, standard Gibbs free energy change of ATP hydrolysis at pH 7.0, 37C
ratio_ATP=np.exp((deltaG_ATP-deltaG_ATP_0)/(R*T))*1e6  # ratio of [ADP][Pi][H+]/[ATP] affects the Gibbs free energy of ATP hydrolysis
def template_conditions():
    c_Nai=10.0 #mM, default 10,  4–16 mM https://doi.org/10.1161/01.CIR.0000016701.85760.97
    c_Nao=140.0 #mM  ∼140 mM https://doi.org/10.1016/S0008-6363(02)00656-9
    c_Ki=145 #mM default 145, 140-150 https://doi.org/10.1159/000446268
    c_Ko=4.5 #mM 3.5-5.0, default 4.5
    c_ATP=1 #mM ~1 mM https://doi.org/10.1073/pnas.2318535121, previously estimated 8 to 10 mM level, 
    c_ADP=0.035  #mM default 0.035,  20–40 μM https://doi.org/10.1016/S0005-2728(01)00247-X, 
    pH=7.2 # default 7.2, range 7.15-7.25
    #c_H=10**(-pH)*1000 #mM
    c_Pi=0.8 #mM 1-10  https://pmc.ncbi.nlm.nih.gov/articles/PMC4552539/, default 0.8
    ratio=(c_ADP)*(c_Pi)*(10**(-pH)*1000)/(c_ATP) #mM, [ADP][Pi][H+]/[ATP]
    print('Default ratio of [ADP][Pi][H+]/[ATP]: ', ratio)
    template_conditions_dict= {
     'c_Nai':{'Parameter':'$c_{Nai}$', 'Value':str(c_Nai), 'Units': 'mM', 'Description':'Intracellular Sodium Concentration','References': 'despa_intracellular_2002,bers_intracellular_2003'},
     'c_Nao':{'Parameter':'$c_{Nao}$', 'Value':str(c_Nao),  'Units': 'mM', 'Description':'Extracellular Sodium Concentration','References': 'despa_intracellular_2002,bers_intracellular_2003'},
     'c_Ki':{'Parameter':'$c_{Ki}$',   'Value':str(c_Ki), 'Units': 'mM', 'Description':'Intracellular Potassium Concentration', 'References': 'zacchia_potassium_2016'},
     'c_Ko':{'Parameter':'$c_{Ko}$', 'Value':str(c_Ko), 'Units': 'mM', 'Description':'Extracellular Potassium Concentration', 'References': 'zacchia_potassium_2016'},
     'c_ATP':{'Parameter':'$c_{ATP}$', 'Value':str(c_ATP), 'Units': 'mM', 'Description':'Intracellular ATP Concentration', 'References': 'rhana_fueling_2024'},
     'c_ADP':{'Parameter':'$c_{ADP}$', 'Value':str(c_ADP), 'Units': 'mM', 'Description':'Intracellular ADP Concentration', 'References': 'dobson_heart_2002'},
     'c_Pi':{'Parameter':'$c_{Pi}$', 'Value':str(c_Pi), 'Units': 'mM', 'Description':'Intracellular Inorganic Phosphate Concentration', 'References': 'tran_regulation_2015'},
     'pH':{'Parameter':'pH', 'Value':str(pH), 'Units': 'dimensionless','Description':'Intracellular pH', 'References': 'orlowski_intracellular_2025'}
      }
    # save the template conditions to a csv file: Parameter, Description, Value, Units, References
    pd.DataFrame.from_dict(template_conditions_dict, orient='index', 
                           columns=['Parameter', 'Description','Value', 'Units','References']).to_csv(parent_path / ('default_conditions.csv'), index=False)
    changes_dict={'c_Nai':{'component':component_name,'name':'c_Nai','newValue':template_conditions_dict['c_Nai']['Value']},
                      'c_Nao':{'component':component_name,'name':'c_Nao','newValue':template_conditions_dict['c_Nao']['Value']},
                      'c_Ki':{'component':component_name,'name':'c_Ki','newValue':template_conditions_dict['c_Ki']['Value']},
                      'c_Ko':{'component':component_name,'name':'c_Ko','newValue':template_conditions_dict['c_Ko']['Value']},
                      'c_ATP':{'component':component_name,'name':'c_ATP','newValue':template_conditions_dict['c_ATP']['Value']},
                      'c_ADP':{'component':component_name,'name':'c_ADP','newValue':template_conditions_dict['c_ADP']['Value']},
                      'c_Pi':{'component':component_name,'name':'c_Pi','newValue':template_conditions_dict['c_Pi']['Value']},
                      'pH':{'component':component_name,'name':'pH','newValue':template_conditions_dict['pH']['Value']}
                      }
    return changes_dict

def vary_pH(changes_dict):
    filename= component_name +'_pH.json' 
    json_path = parent_path / filename
    #pH=[7.15, 7.2, 7.25,7.3, 7.4] # default 7.2, range 7.15-7.25
    #c_H=10**(-pH)*1000 #mM
    # construct the changes dictionary for different pH values 
    c_ATP=float(changes_dict['c_ATP']['newValue'])
    c_ADP=float(changes_dict['c_ADP']['newValue'])
    c_Pi=float(changes_dict['c_Pi']['newValue'])
    c_H=ratio_ATP*c_ATP/(c_ADP*c_Pi) #mM, corresponding to the default ratio value
    pH= -np.log10(c_H/1000)
    changes=[]    
    for i in range(len(pH)):
        changes_dict_copy=copy.deepcopy(changes_dict)
        changes_dict_copy['pH']['newValue']=str(pH[i])
        changes.append(changes_dict_copy)
        #ratio.append([ADP][Pi][H+]/[ATP])
    # save ATP, ADP, Pi, pH and the ratio of [ADP][Pi][H+]/[ATP] to a csv file
    df_ratio=pd.DataFrame({ 'ATP':[c_ATP]*len(pH), 'ADP':[c_ADP]*len(pH), 'Pi':[c_Pi]*len(pH), 'pH':pH, 
                           'ratio_with_H':1/ratio_ATP,'ratio_without_H':c_H/ratio_ATP,'ATP_ADP':c_ATP/c_ADP,'deltaG_ATP':deltaG_ATP/1000})
    df_ratio.to_csv(json_path.with_suffix('.csv'), index=False)
    
    write_json(json_path, changes)

def vary_Nai(changes_dict):

    filename= component_name +'_Nai.json'
    json_path = parent_path / filename

    c_Nai=[4, 6, 8, 10, 12, 14, 16] #mM, default 10,  4–16 mM https://doi.org/10.1161/01.CIR.0000016701.85760.97
    # construct the changes dictionary
    changes=[]
    for i in range(len(c_Nai)):
        changes_dict_copy=copy.deepcopy(changes_dict)
        changes_dict_copy['c_Nai']['newValue']=str(c_Nai[i])
        changes.append(changes_dict_copy)
    write_json(json_path, changes)

def vary_Nai_ATP(changes_dict):

    filename= component_name +'_NaiATP.json'
    json_path = parent_path / filename

    c_Nai=[4, 6, 8, 10, 12, 14, 16] #mM, default 10,  4–16 mM https://doi.org/10.1161/01.CIR.0000016701.85760.97
    c_ADP=float(changes_dict['c_ADP']['newValue'])
    c_Pi=float(changes_dict['c_Pi']['newValue'])
    c_H=float(10**(-float(changes_dict['pH']['newValue']))*1000) #mM
    pH=float(changes_dict['pH']['newValue'])
    c_ATP=(c_ADP*c_Pi*c_H)/ratio_ATP #mM, corresponding to the default ratio value 

    # construct the changes dictionary
    changes=[]
    for i in range(len(c_Nai)):
        changes_dict_copy=copy.deepcopy(changes_dict)
        changes_dict_copy['c_Nai']['newValue']=str(c_Nai[i])
        for j in range(len(c_ATP)):
            changes_dict_copy=copy.deepcopy(changes_dict)
            changes_dict_copy['c_ATP']['newValue']=str(c_ATP[j])
            changes.append(changes_dict_copy)

    write_json(json_path, changes)

def vary_Ko(changes_dict):
    filename= component_name +'_Ko.json'
    json_path = parent_path / filename
    c_Ko=[3.5, 4, 4.5,5, 5.5] #mM 3.5-5.0
    # construct the changes dictionary
    changes=[]
    for i in range(len(c_Ko)):
        changes_dict_copy=copy.deepcopy(changes_dict)
        changes_dict_copy['c_Ko']['newValue']=str(c_Ko[i])
        changes.append(changes_dict_copy)
    write_json(json_path, changes)

def vary_ATP(changes_dict):    
    filename= component_name +'_ATP.json'
    json_path = parent_path / filename
    #c_ATP=[0.5, 1, 4, 7, 10] #mM ~1 mM https://doi.org/10.1073/pnas.2318535121, previously estimated 8 to 10 mM level, 
    # construct the changes dictionary
    c_ADP=float(changes_dict['c_ADP']['newValue'])
    c_Pi=float(changes_dict['c_Pi']['newValue'])
    c_H=float(10**(-float(changes_dict['pH']['newValue']))*1000) #mM
    pH=float(changes_dict['pH']['newValue'])
    c_ATP=(c_ADP*c_Pi*c_H)/ratio_ATP #mM, corresponding to the default ratio value
    changes=[]
    for i in range(len(c_ATP)):
        changes_dict_copy=copy.deepcopy(changes_dict)
        changes_dict_copy['c_ATP']['newValue']=str(c_ATP[i])
        changes.append(changes_dict_copy)
    # save ATP, ADP, Pi, pH and the ratio of [ADP][Pi][H+]/[ATP] to a csv file
    df_ratio=pd.DataFrame({ 'ATP':c_ATP, 'ADP':[c_ADP]*len(c_ATP), 'Pi':[c_Pi]*len(c_ATP), 
                           'pH':[pH]*len(c_ATP), 'ratio_with_H':1/ratio_ATP, 'ratio_without_H':c_H/ratio_ATP, 'ATP_ADP':c_ATP/c_ADP, 'deltaG_ATP':deltaG_ATP/1000})
    df_ratio.to_csv(json_path.with_suffix('.csv'), index=False)

    write_json(json_path, changes)
def vary_ADP(changes_dict):
    filename= component_name +'_ADP.json'
    json_path = parent_path / filename
    #c_ADP=[0.01, 0.02, 0.035, 0.05, 0.07] #mM 20–40 μM https://doi.org/10.1016/S0005-2728(01)00247-X, default 0.035
    # construct the changes dictionary
    ratio=[] # ratio of [ADP][Pi][H+]/[ATP], affects the Gibbs free energy of ATP hydrolysis
    c_ATP=float(changes_dict['c_ATP']['newValue'])
    c_Pi=float(changes_dict['c_Pi']['newValue'])
    c_H=float(10**(-float(changes_dict['pH']['newValue']))*1000) #mM
    pH=float(changes_dict['pH']['newValue'])
    c_ADP=(ratio_ATP*c_ATP)/(c_Pi*c_H) #mM, corresponding to the default ratio value
    changes=[]
    for i in range(len(c_ADP)):
        changes_dict_copy=copy.deepcopy(changes_dict)
        changes_dict_copy['c_ADP']['newValue']=str(c_ADP[i])
        changes.append(changes_dict_copy)
    # save ATP, ADP, Pi, pH and the ratio of [ADP][Pi][H+]/[ATP] to a csv file
    df_ratio=pd.DataFrame({ 'ATP':[c_ATP]*len(c_ADP), 'ADP':c_ADP, 'Pi':[c_Pi]*len(c_ADP), 
                           'pH':[pH]*len(c_ADP), 'ratio_with_H':1/ratio_ATP, 'ratio_without_H':c_H/ratio_ATP, 'ATP_ADP':c_ATP/c_ADP, 'deltaG_ATP':deltaG_ATP/1000})
    df_ratio.to_csv(json_path.with_suffix('.csv'), index=False)
    write_json(json_path, changes)

def vary_Pi(changes_dict):
    filename= component_name +'_Pi.json'
    json_path = parent_path / filename
    #c_Pi=[0.8, 1, 4, 7, 10] #mM 1-10  https://pmc.ncbi.nlm.nih.gov/articles/PMC4552539/, default 0.8
    # construct the changes dictionary
    ratio=[] # ratio of [ADP][Pi][H+]/[ATP], affects the Gibbs free energy of ATP hydrolysis
    c_ATP=float(changes_dict['c_ATP']['newValue'])
    c_ADP=float(changes_dict['c_ADP']['newValue'])
    c_H=float(10**(-float(changes_dict['pH']['newValue']))*1000) #mM
    pH=float(changes_dict['pH']['newValue'])
    c_Pi=(ratio_ATP*c_ATP)/(c_ADP*c_H) #mM, corresponding to the default ratio value
    changes=[]
    for i in range(len(c_Pi)):
        changes_dict_copy=copy.deepcopy(changes_dict)
        changes_dict_copy['c_Pi']['newValue']=str(c_Pi[i])
        changes.append(changes_dict_copy)
    # save ATP, ADP, Pi, pH and the ratio of [ADP][Pi][H+]/[ATP] to a csv file
    df_ratio=pd.DataFrame({ 'ATP':[c_ATP]*len(c_Pi), 'ADP':[c_ADP]*len(c_Pi), 'Pi':c_Pi, 
                           'pH':[pH]*len(c_Pi), 'ratio_with_H':1/ratio_ATP, 'ratio_without_H':c_H/ratio_ATP, 'ATP_ADP':c_ATP/c_ADP, 'deltaG_ATP':deltaG_ATP/1000})
    df_ratio.to_csv(json_path.with_suffix('.csv'), index=False)

    write_json(json_path, changes)
    
def default_conditions(changes_dict):
    filename= component_name +'_default.json'
    json_path = parent_path / filename
    # construct the changes dictionary
    changes=[]
    changes.append(changes_dict)
    write_json(json_path, changes)

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
                      'pH':{'component':component_name,'name':'pH','newValue':str(pH)}
                      }
        changes.append(changes_dict)

    write_json(json_path, changes)

if __name__ == "__main__":
    template_conditions_dict=template_conditions()
    vary_Nai(template_conditions_dict)
    vary_Ko(template_conditions_dict)
    vary_ATP(template_conditions_dict)
    vary_Pi(template_conditions_dict)
    vary_ADP(template_conditions_dict)
    vary_pH(template_conditions_dict)
    vary_Nai_ATP(template_conditions_dict)
    write_fig3a_conditions()
    write_fig3b_conditions()
    write_fig3c_conditions()
    write_fig5_conditions()
    default_conditions_physiome()
    default_conditions(template_conditions_dict)