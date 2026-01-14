from cProfile import label
from calendar import c
import sys
import os
from mpl_toolkits.axes_grid1 import make_axes_locatable
# Add parent directory to sys.path for module imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Add 'dataPlot' subdirectory to sys.path for module imports
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'dataPlot'))

# Import Path for filesystem operations
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from matplotlib.ticker import LinearLocator
import pandas as pd
simulation_path = Path(__file__).parent.parent / 'cad' / 'models' / 'simulation'

heat_6_file=Path(simulation_path / 'report_task_NKE_BG_6_state_ATPNaZKV2_default_T1000ms_0EA_summary.csv').as_posix()
heat_6state=pd.read_csv(heat_6_file)['meanPower'].values[0:6]
labels=['$Rx_m^1$','$Rx_m^2$','$Rx_m^3$','$Rx_m^4$','$Rx_m^5$','$Rx_m^6$']

# plot bar chart
fig, ax = plt.subplots(figsize=(3,3))
y_pos = np.arange(len(labels))
plt.bar(y_pos, np.array(heat_6state)/1000, align='center', alpha=0.5)
plt.xticks(y_pos, labels)
plt.xlabel('Reactions')
plt.ylabel('Heat production rate (pW)')
plt.tight_layout()
# grid lines
ax.yaxis.grid(True, linestyle='--', alpha=0.5)
fig.savefig(Path(simulation_path / 'EA_6state_heat_bar.png').as_posix(), dpi=300)
plt.show()

heat_15_file=Path(simulation_path / 'report_task_NKE_BG_15_state_default_T1000ms_0EA_summary.csv').as_posix()
heat_15state=pd.read_csv(heat_15_file)['meanPower'].values[0:15]

labels_15state=['$Rx_m^1$','$Rx_m^2$','$Rx_m^3$','$Rx_m^4$','$Rx_m^5$','$Rx_m^6$','$Rx_m^7$','$Rx_m^8$','$Rx_m^9$','$Rx_m^{10}$','$Rx_m^{11}$','$Rx_m^{12}$','$Rx_m^{13}$','$Rx_m^{14}$','$Rx_m^{15}$']
# plot bar chart
fig, ax = plt.subplots(figsize=(6,3))
y_pos = np.arange(len(labels_15state))
plt.bar(y_pos, np.array(heat_15state)/1000, align='center', alpha=0.5)
plt.xticks(y_pos, labels_15state)
plt.xlabel('Reactions')
plt.ylabel('Heat production rate (pW)')
plt.tight_layout()
# grid lines
ax.yaxis.grid(True, linestyle='--', alpha=0.5)  
fig.savefig(Path(simulation_path / 'EA_15state_heat_bar.png').as_posix(), dpi=300)
plt.show()