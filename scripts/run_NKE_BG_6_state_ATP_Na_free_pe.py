import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pathlib import Path
from run_sedmls import run_simulation

parent_path = Path(__file__).parent.parent / 'cad' / 'models'
simulation_path = Path(__file__).parent.parent / 'cad' / 'models' / 'simulation'

full_path= parent_path / 'NKE_BG_6_state_ATP_Na_free_pulseV_pe.sedml'
run_simulation(full_path)