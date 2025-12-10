from run_sedmls import run_sim_jsons
from pathlib import Path
import os
import pandas as pd
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_path = Path(__file__).parent.parent / 'cad' / 'models'
simulation_path = Path(__file__).parent.parent / 'cad' / 'models' / 'simulation'
path_=os.path.join(current_dir, '../cad/data/')
sedml_jsonfiles=['NKE_BG_15_state_fixedV_sedmls.json']

external_data_path = path_ + 'faber_rudy_modified_version_2000_with_corrected_ICaT_data_1000.csv'
pdf_data=pd.read_csv(external_data_path)
vm = (pdf_data['cell | V (millivolt)'].values/1000).tolist()
time_points = (pdf_data['environment | time (ms)'].values/1000).tolist()

run_sim_jsons (sedml_jsonfiles,external_variables_info={1:{'component': 'NKE_BG_Env', 'name': 'u_0_Vm'}},
                  external_variables_values=[time_points,vm])   

