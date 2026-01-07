from matplotlib import sankey
from matplotlib.pylab import f
from matplotlib.sankey import Sankey
import sys
import os
import matplotlib.pyplot as plt
# Add parent directory to sys.path for module imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Add 'dataPlot' subdirectory to sys.path for module imports
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'dataPlot'))

# Import Path for filesystem operations
from pathlib import Path
import numpy as np
import pandas as pd
simulation_path = Path(__file__).parent.parent / 'cad' / 'models' / 'simulation'
path_ = Path(__file__).parent.parent / 'cad' /  'data'

exp_id=['Nai','Ko','ATP','ADP','Pi','pH']
T_0=np.array([600,800,1000,1200])
z_var_names=['Na Energy', 'K Energy', 'ATP Hydrolysis Energy','Total',
              'Vm Energy', 'Reactions Heat Production', 
            ]
basefile='EA_report_task_NKE_BG_15_state_default'
# collect data
ids='_T1000ms'
pdf = pd.read_csv(Path(simulation_path / f'{basefile}{ids}.csv').as_posix())
z_var_vals = {}
for z_var_name in z_var_names:
    if 'ATP Hydrolysis Energy' in z_var_name:
        z_var_vals[z_var_name] = -pdf[z_var_name].values[-1]  # make it positive
    else:
        z_var_vals[z_var_name] = pdf[z_var_name].values[-1]
# normalize to the ATP Hydrolysis Energy
total_input = z_var_vals['ATP Hydrolysis Energy'] 
for key in z_var_vals:
    z_var_vals[key] = z_var_vals[key] / total_input * 100.0  
# draw Sankey diagram for all variables
# From ATP Hydrolysis Energy to NKE; From Total to NKE
# From NKE to 'Na Energy', 'K Energy', 'Vm Energy', 'Reactions Heat Production'
# Using different colors for nodes and links
# Add arrow for better visualization
# fixed target positions for better visualization
fig=plt.figure(figsize=(8,6))
ax=fig.add_subplot(1, 1, 1, xticks=[], yticks=[],frame_on=False)
sankey = Sankey(ax=ax, unit='%', scale=0.01, offset=0.28, gap=0.15, format='%.1f')

flows = [z_var_vals['ATP Hydrolysis Energy'], -z_var_vals['Reactions Heat Production'],
         -z_var_vals['Na Energy'], -z_var_vals['K Energy'],
         -z_var_vals['Vm Energy']]
labels = ['ATP hydrolysis', 'Heat production', r'$Na^+$ storage', r'$K^+$ storage', 'Membrane storage']
orients = [0, 1, 0, 0, -1]

sankey.add(
    flows=flows,
    labels=labels,
    orientations=orients,
    trunklength=1.5,              # extend the central trunk
    pathlengths=[0.4, 0.3, 0.4, 0.4, 0.3],
    alpha=0.6
)
sankey.finish()
fig_name=f'{basefile}_Sankey'
fig.savefig(simulation_path / f'{fig_name}.png', dpi=300, bbox_inches='tight')
plt.show()