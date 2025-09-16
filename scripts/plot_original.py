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
from dataPlot.manData import combine_csv_files

simulation_path = Path(__file__).parent.parent / 'cad' / 'models' / 'simulation'
path_ = Path(__file__).parent.parent / 'cad' /  'data'

def original_lines_ss():
    filename_volt = Path(path_ /'New_Terkildsen_NaK_BG_Fig5_Data.csv').as_posix()
    filename_Nai = Path(path_ /'Terkildsen_NaK_kinetic_Fig3a_Data.csv').as_posix() #path_+'Terkildsen_NaK_kinetic_Fig3a_Data.csv'
    filename_Ke = Path (path_ /'Terkildsen_NaK_kinetic_Fig3b_Data.csv').as_posix() #path_+'Terkildsen_NaK_kinetic_Fig3b_Data.csv'
    filename_ATP = Path (path_ /'Terkildsen_NaK_kinetic_Fig3c_Data.csv').as_posix() # path_+'Terkildsen_NaK_kinetic_Fig3c_Data.csv'
    line_cfg = {}
    line_cfg['volt'] = { 'xdata': (filename_volt,'environment | V_mem (volt)'), 'ydata':(filename_volt,'environment | v_R1 (fmol_per_sec)'),
                'color': 'k', 'linestyle': '-',  'label': 'Terkildsen ss model'}
    line_cfg['Nai'] = { 'xdata': (filename_Nai,'environment | Nai (mM)'), 'ydata':(filename_Nai,'environment | v_cyc_nak (per_second)'),
                'color': 'k', 'linestyle': '-',  'label': 'Terkildsen ss model'}
    line_cfg['Ke'] = { 'xdata': (filename_Ke,'environment | Ke (mM)'), 'ydata':(filename_Ke,'environment | v_cyc_nak (per_second)'),
                'color': 'k', 'linestyle': '-',  'label': 'Terkildsen ss model'}
    line_cfg['ATP'] = { 'xdata': (filename_ATP,'environment | MgATP (mM)'), 'ydata':(filename_ATP,'environment | v_cyc_nak (per_second)'),
                'color': 'k', 'linestyle': '-',  'label': 'Terkildsen ss model'}
    return line_cfg


def merge_csv_files_ss(new_csv_file):
    new_csv_file_name = new_csv_file +'.csv'
    new_csv_file_fullpath = Path(simulation_path/new_csv_file_name).as_posix() 
    # find the csv files whose name starts with report_task_NKE_BG_15_state_fixedV_fig3a_ and ends with .csv in the simulation folder
    list_csv_files = [f for f in os.listdir(simulation_path) if f.startswith(new_csv_file+'_') and f.endswith('.csv')]
    
    first_file=Path(simulation_path/list_csv_files[0]).as_posix()
    csv_files=[(first_file, 0, 0)] # [list_csv_files[0]]
    for csv_file in list_csv_files:
        csv_files.append((Path(simulation_path/csv_file).as_posix(), 1, 1))

    combine_csv_files(new_csv_file_fullpath, csv_files)
    return new_csv_file_fullpath

def new_lines_ss(dict_data,label=''):
    line_cfg = {}
    for key, file in dict_data.items():
        bg_fig_file=merge_csv_files_ss(file)
        line_cfg[key] = { 'xdata': (bg_fig_file,key), 'ydata':(bg_fig_file,'v_r1'),
                'color': 'b', 'linestyle': '-',  'label': label}
    return line_cfg


def plot_cfg_ss():
    plot_cfg = {}
    plot_cfg[1] = {'ylabel': 'cycle rate', 'xlabel': 'potential (mV)','show_grid': 'both', 'grid_axis': 'both',  'title_y': -0.3,
                'line': ['volt','u_Vm'], 'legend': ['volt','u_Vm']}
    plot_cfg[2] = {'ylabel': 'cycle rate', 'xlabel': 'Na_i (mM)','show_grid': 'both', 'grid_axis': 'both',   'title_y': -0.3,
                'line': ['Nai', 'c_Nai'], 'legend': ['Nai', 'c_Nai']}
    plot_cfg[3] = {'ylabel': 'cycle rate', 'xlabel': 'K_e (mM)','show_grid': 'both', 'grid_axis': 'both',  'title_y': -0.3,
                'line': ['Ke', 'c_Ko'], 'legend': ['Ke', 'c_Ko']}
    plot_cfg[4] = {'ylabel': 'cycle rate', 'xlabel': 'ATP (mM)','show_grid': 'both', 'grid_axis': 'both', 'title_y': -0.3,
                'line': ['ATP', 'c_ATP'], 'legend': ['ATP', 'c_ATP']}

    return plot_cfg


if __name__ == '__main__':
    
    save_fig = {'save_fig': True, 'fig_format': 'tif', 'file_path': simulation_path.as_posix(), 'filename': 'NKE_BG_6_state_ATPNaZK'}
    fig_cfg = {'num_rows': 2, 'num_cols': 2, 'width':7.5, 'height':6, 'fig_title': None, 'title_y': 1, 'fontsize': 8, 
           'left': 0.1, 'bottom': 0.15, 'right': 0.9, 'top': 0.95, 'wspace': 0.2, 'hspace': 0.4}|save_fig
    
    data_dict={'u_Vm': 'report_task_NKE_BG_6_state_ATPNaZK_fit_fixedV_fig5',
               'c_Nai': 'report_task_NKE_BG_6_state_ATPNaZK_fit_fixedV_fig3a',
               'c_Ko': 'report_task_NKE_BG_6_state_ATPNaZK_fit_fixedV_fig3b',
               'c_ATP': 'report_task_NKE_BG_6_state_ATPNaZK_fit_fixedV_fig3c'}
    
    line_cfg=new_lines_ss(data_dict,'6-state BG model')
    original_line_cfg=original_lines_ss()
    original_line_cfg.update(line_cfg)
    plot_cfg = plot_cfg_ss()

    plot_line2D(fig_cfg, plot_cfg, original_line_cfg)
