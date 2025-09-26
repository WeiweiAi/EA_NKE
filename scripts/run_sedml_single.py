from run_sedmls import run_simulation
from pathlib import Path

parent_path = Path(__file__).parent.parent / 'cad' / 'models'
simulation_path = Path(__file__).parent.parent / 'cad' / 'models' / 'simulation'

full_path = parent_path / 'NKE_BG_6_state_ATPNaZK_Nai_V2.sedml'
run_simulation(full_path)
