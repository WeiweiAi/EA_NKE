import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pathlib import Path
from run_sedmls import run_simulation

parent_path = Path(__file__).parent.parent / 'cad' / 'models'
simulation_path = Path(__file__).parent.parent / 'cad' / 'models' / 'simulation'

full_path= parent_path / 'NKE_BG_6_state_ATPNaZKV2_fixedV_ss_pe.sedml'
ss_time={'fit_1':0.3,'fit_2':0.3,'fit_3':0.3,'fit_4':0.3}
run_simulation(full_path,rel_out_path='./simulation', external_variables_info={},
                  external_variables_values=[],ss_time=ss_time)