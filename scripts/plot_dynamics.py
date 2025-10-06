import sys
import os

# Add parent directory to sys.path for module imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Add 'dataPlot' subdirectory to sys.path for module imports
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'dataPlot'))

# Import Path for filesystem operations
from pathlib import Path
# Import plot_line2D function from dataPlot.dataPlot module
from dataPlot.dataPlot import plot_line2D

simulation_path = Path(__file__).parent.parent / 'cad' / 'models' / 'simulation'
path_ = Path(__file__).parent.parent / 'cad' /  'data'

save_fig = {'save_fig': True, 'fig_format': 'tif', 'file_path': simulation_path.as_posix()+'/', 'filename': 'Terkildsen'}
fig_cfg = {'num_rows': 1, 'num_cols': 1, 'width':7.5, 'height':6, 'fig_title': None, 'title_y': 1, 'fontsize': 8, 
           'left': 0.1, 'bottom': 0.15, 'right': 0.9, 'top': 0.95, 'wspace': 0.2, 'hspace': 0.4}|save_fig

filename_ss = Path(simulation_path /'report_task_Terkildsen_NaK_kinetic_modular_V_default_0.csv').as_posix()
filename_bg15 = Path(simulation_path /'report_task_NKE_BG_15_state_ATP_0.csv').as_posix()
filename_bg6_ZK = Path(simulation_path /'report_task_NKE_BG_15_state_ATP_1.csv').as_posix()
filename_bg6 = Path(simulation_path /'report_task_NKE_BG_15_state_ATP_2.csv').as_posix()

line_cfg={}
line_cfg['ss'] = { 'xdata': (filename_ss,'t'), 'ydata':(filename_ss,'i_Vm'),
                'color': 'k', 'linestyle': '-',  'label': 'Terkildsen ss model'}
line_cfg['bg15'] = { 'xdata': (filename_bg15,'t'), 'ydata':(filename_bg15,'i_Vm'),
                'color': 'b', 'linestyle': '-.',  'label': 'Terkildsen 15-state model'}
line_cfg['bg6_ZK'] = { 'xdata': (filename_bg6_ZK,'t'), 'ydata':(filename_bg6_ZK,'i_Vm'),
                'color': 'c', 'linestyle': '-.',  'label': '6-ZK model'}
line_cfg['bg6'] = { 'xdata': (filename_bg6,'t'), 'ydata':(filename_bg6,'i_Vm'),
                'color': 'm', 'linestyle': '-.',  'label': '6 model'}

lines_dict={1:{'xlabel': 't', 'line':['ss', 'bg15','bg6_ZK','bg6']}}

def plot_cfg_ss(lines_dict):
    plot_cfg = {}
    for plot_id, line_group in lines_dict.items():
        plot_cfg[plot_id] = {'ylabel': 'current', 'xlabel': line_group['xlabel'],'show_grid': 'both', 'grid_axis': 'both',  'title_y': -0.3,
                'line': line_group['line'], 'legend': line_group['line']}

    return plot_cfg

plot_cfg = plot_cfg_ss(lines_dict)

plot_line2D(fig_cfg, plot_cfg, line_cfg)
