import sys
import os
import pandas as pd

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

def original_data_fig2a():
    line_cfg = {}
    filename_fig2a1= Path(path_ /'fig2a_cond_1.csv').as_posix() #path_+'Terkildsen_NaK_kinetic_Fig2a1_Data.csv'
    filename_fig2a2= Path(path_ /'fig2a_cond_2.csv').as_posix()
    filename_fig2a3= Path(path_ /'fig2a_cond_3.csv').as_posix()
    filename_fig2a4= Path(path_ /'fig2a_cond_4.csv').as_posix()
    pdf=pd.read_csv(filename_fig2a1)
    xdata_array=pdf['u_0_Vm'].values*1000
    line_cfg['fig2a1_data'] = { 'xdata_array': xdata_array, 'ydata': (filename_fig2a1,'v_ss'),
                          'color': 'c', 'marker': '.', 'linestyle':'', 'label': ''}
    line_cfg['fig2a2_data'] = { 'xdata_array': xdata_array, 'ydata': (filename_fig2a2,'v_ss'),
                          'color': 'r', 'marker': '.',  'linestyle':'','label': ''}
    line_cfg['fig2a3_data'] = { 'xdata_array': xdata_array, 'ydata': (filename_fig2a3,'v_ss'),
                          'color': 'b', 'marker': '.', 'linestyle':'', 'label': ''}
    line_cfg['fig2a4_data'] = { 'xdata_array': xdata_array, 'ydata': (filename_fig2a4,'v_ss'),
                          'color': 'g', 'marker': '.',  'linestyle':'', 'label': ''}
    return line_cfg

def original_data_fig2b():
    line_cfg = {}
    filename_fig2b1= Path(path_ /'fig2b_cond_1.csv').as_posix() #path_+'Terkildsen_NaK_kinetic_Fig2a1_Data.csv'
    filename_fig2b2= Path(path_ /'fig2b_cond_2.csv').as_posix()
    filename_fig2b3= Path(path_ /'fig2b_cond_3.csv').as_posix()
    pdf=pd.read_csv(filename_fig2b1)
    xdata_array=pdf['u_0_Vm'].values*1000
    line_cfg['fig2b1_data'] = { 'xdata_array': xdata_array, 'ydata': (filename_fig2b1,'v_ss'),
                          'color': 'c', 'marker': '.', 'linestyle':'', 'label': ''}
    line_cfg['fig2b2_data'] = { 'xdata_array': xdata_array, 'ydata': (filename_fig2b2,'v_ss'),
                          'color': 'r', 'marker': '.',  'linestyle':'', 'label': ''}
    line_cfg['fig2b3_data'] = { 'xdata_array': xdata_array, 'ydata': (filename_fig2b3,'v_ss'),
                          'color': 'b', 'marker': '.',  'linestyle':'', 'label': ''}
    return line_cfg

def original_data_fig3a():
    line_cfg = {}
    filename_fig3a= Path(path_ /'fig3a_cond.csv').as_posix() #path_+'Terkildsen_NaK_kinetic_Fig2a1_Data.csv'
    pdf=pd.read_csv(filename_fig3a)
    xdata_array=pdf['c_Nai'].values
    line_cfg['fig3a_data'] = { 'xdata_array': xdata_array, 'ydata': (filename_fig3a,'v_ss'),
                          'color': 'k', 'marker': '.','linestyle':'',  'label': ''}
    return line_cfg
def original_data_fig3b():
    line_cfg = {}
    filename_fig3b= Path(path_ /'fig3b_cond.csv').as_posix() #path_+'Terkildsen_NaK_kinetic_Fig2a1_Data.csv'
    pdf=pd.read_csv(filename_fig3b)
    xdata_array=pdf['c_Ko'].values
    line_cfg['fig3b_data'] = { 'xdata_array': xdata_array, 'ydata': (filename_fig3b,'v_ss'),
                          'color': 'k', 'marker': '.', 'linestyle':'', 'label': ''}
    return line_cfg

def original_data_fig3c():
    line_cfg = {}
    filename_fig3c= Path(path_ /'fig3c_cond.csv').as_posix() #path_+'Terkildsen_NaK_kinetic_Fig2a1_Data.csv'
    pdf=pd.read_csv(filename_fig3c)
    xdata_array=pdf['c_ATP'].values
    line_cfg['fig3c_data'] = { 'xdata_array': xdata_array, 'ydata': (filename_fig3c,'v_ss'),
                          'color': 'k', 'marker': '.', 'linestyle':'', 'label': ''}
    return line_cfg

def original_kinetic_ss_fig2a():
    filename_fig2a = Path(path_ /'Terkildsen_NaK_kinetic_Fig2a_Data.csv').as_posix()
    line_cfg = {}
    line_cfg['fig2a1_kinetic'] = { 'xdata': (filename_fig2a,'environment | Vm (mV)'), 'ydata':(filename_fig2a,'environment | scaled_v_cyc1 (per_second)'),
                'color': 'c', 'linestyle': '-',  'label': '[Na_o] = 1.5 mM'}
    line_cfg['fig2a2_kinetic'] = { 'xdata': (filename_fig2a,'environment | Vm (mV)'), 'ydata':(filename_fig2a,'environment | scaled_v_cyc2 (per_second)'),
                'color': 'r', 'linestyle': '-',  'label': '[Na_o] = 50 mM'}
    line_cfg['fig2a3_kinetic'] = { 'xdata': (filename_fig2a,'environment | Vm (mV)'), 'ydata':(filename_fig2a,'environment | scaled_v_cyc3 (per_second)'),
                'color': 'b', 'linestyle': '-',  'label': '[Na_o] =100 mM'}
    line_cfg['fig2a4_kinetic'] = { 'xdata': (filename_fig2a,'environment | Vm (mV)'), 'ydata':(filename_fig2a,'environment | scaled_v_cyc4 (per_second)'),
                'color': 'g', 'linestyle': '-',  'label': '[Na_o] = 150 mM'}
    return line_cfg

def original_kinetic_ss_fig2b():
    filename_fig2b = Path(path_ /'Terkildsen_NaK_kinetic_Fig2b_Data.csv').as_posix() 
    line_cfg = {}
    line_cfg['fig2b1_kinetic'] = { 'xdata': (filename_fig2b,'environment | Vm (mV)'), 'ydata':(filename_fig2b,'environment | current_density1 (uA_per_uF)'),
                'color': 'c', 'linestyle': '-',  'label': '[Na_o] = 50 mM'}
    line_cfg['fig2b2_kinetic'] = { 'xdata': (filename_fig2b,'environment | Vm (mV)'), 'ydata':(filename_fig2b,'environment | current_density2 (uA_per_uF)'),
                'color': 'r', 'linestyle': '-',  'label': '[Na_o] = 100 mM'}
    line_cfg['fig2b3_kinetic'] = { 'xdata': (filename_fig2b,'environment | Vm (mV)'), 'ydata':(filename_fig2b,'environment | current_density3 (uA_per_uF)'),
                'color': 'b', 'linestyle': '-',  'label': '[Na_o] = 150 mM'}
    return line_cfg

def original_kinetic_ss_fig3a():
    filename_Nai = Path(path_ /'Terkildsen_NaK_kinetic_Fig3a_Data.csv').as_posix() #path_+'Terkildsen_NaK_kinetic_Fig3a_Data.csv'
    line_cfg = {}
    yvar='environment | v_cyc_nak (per_second)'
    pdf=pd.read_csv(filename_Nai)
    norm_v_cyc_nak = pdf[yvar].values/51.945
    line_cfg['fig3a_kinetic'] = { 'xdata': (filename_Nai,'environment | Nai (mM)'), 'ydata_array':norm_v_cyc_nak,
                'color': 'k', 'linestyle': '-',  'label': 'Terkildsen ss model'}
    return line_cfg

def original_kinetic_ss_fig3b():
    filename_Ke = Path (path_ /'Terkildsen_NaK_kinetic_Fig3b_Data.csv').as_posix() #path_+'Terkildsen_NaK_kinetic_Fig3b_Data.csv'
    line_cfg = {}
    yvar='environment | v_cyc_nak (per_second)'
    pdf=pd.read_csv(filename_Ke)
    norm_v_cyc_nak = pdf[yvar].values/51.1069
    line_cfg['fig3b_kinetic'] = { 'xdata': (filename_Ke,'environment | Ke (mM)'), 'ydata_array':norm_v_cyc_nak,
                'color': 'k', 'linestyle': '-',  'label': 'Terkildsen ss model'}
    return line_cfg

def original_kinetic_ss_fig3c():
    filename_ATP = Path (path_ /'Terkildsen_NaK_kinetic_Fig3c_Data.csv').as_posix() # path_+'Terkildsen_NaK_kinetic_Fig3c_Data.csv'
    line_cfg = {}
    yvar='environment | v_cyc_nak (per_second)'
    pdf=pd.read_csv(filename_ATP)
    norm_v_cyc_nak = pdf[yvar].values/34.0994
    line_cfg['fig3c_kinetic'] = { 'xdata': (filename_ATP,'environment | MgATP (mM)'), 'ydata_array':norm_v_cyc_nak,
                'color': 'k', 'linestyle': '-',  'label': 'Terkildsen ss model'}
    return line_cfg

def merge_csv_files_ss(new_csv_file):
    new_csv_file_name = new_csv_file +'.csv'
    new_csv_file_fullpath = Path(simulation_path/new_csv_file_name).as_posix() 
    # find the csv files whose name starts with report_task_NKE_BG_15_state_fixedV_fig3a_ and ends with .csv in the simulation folder
    # rule out the files report_task_NKE_BG_15_state_fixedV_fig3a_***_ss.csv
    # order from _0.csv, _1.csv, _2.csv, ...
    list_csv_files=[f.name for f in simulation_path.glob(new_csv_file + '_*.csv') if not f.name.endswith('_ss.csv')]
    list_csv_files.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))
    first_file=Path(simulation_path/list_csv_files[0]).as_posix()
    csv_files=[(first_file, 0, 0)] # [list_csv_files[0]]
    for csv_file in list_csv_files: 
        csv_files.append((Path(simulation_path/csv_file).as_posix(), 1, 1))
    combine_csv_files(new_csv_file_fullpath, csv_files)
    return new_csv_file_fullpath

def new_lines_fig2a(dict_data):
    line_cfg = {}
    color_idx=0
    colors=['c','r','b','g','k']
    for key, file in dict_data.items():
        # color repeats every 4 lines
        if color_idx==4:
            color_idx=0
        color=colors[color_idx]
        color_idx+=1
        bg_fig_file=merge_csv_files_ss(file)
        pdf=pd.read_csv(bg_fig_file)
        if 'ss' in key:
            yvar='v_NKE'
            xvar='u_Vm'
            xdata_array=pdf[xvar].values*1000
            ydata_array=pdf[yvar].values*55/pdf[yvar].values[8]
            line_cfg[key] = { 'xdata_array': xdata_array, 'ydata_array': ydata_array,
                'color': color,  'linestyle': '-.' }
        else:
            yvar='v_r1'
            xvar='u_Vm'
            xdata_array=pdf[xvar].values*1000
            ydata_array=pdf[yvar].values*55/pdf[yvar].values[8]
            line_cfg[key] = { 'xdata_array': xdata_array, 'ydata_array': ydata_array,
                'color': color,  'marker': '+', 'linestyle': ''}
    return line_cfg

def new_lines_fig2b(dict_data):
    line_cfg = {}
    pump_density = 1360.2624  # pumps per um^2
    color_idx=0
    colors=['c','r','b']
    for key, file in dict_data.items():
        # color repeats every 3 lines
        if color_idx==3:
            color_idx=0
        color=colors[color_idx]
        color_idx+=1
        bg_fig_file=merge_csv_files_ss(file)
        pdf=pd.read_csv(bg_fig_file)       
        if 'ss' in key:
            yvar='v_NKE'
            xvar='u_Vm'
            xdata_array=pdf[xvar].values*1000
            ydata_array=pdf[yvar].values*pump_density*1.6e-5 # uA per uF
            line_cfg[key] = { 'xdata_array': xdata_array, 'ydata_array': ydata_array,
                'color': color,  'linestyle': '-.' }
        else:
            yvar='v_r1'
            xvar='u_Vm'
            xdata_array=pdf[xvar].values*1000
            ydata_array=pdf[yvar].values*pump_density*1.6e-5 # uA per uF
            line_cfg[key] = { 'xdata_array': xdata_array, 'ydata_array': ydata_array,
                'color': color,  'marker': '+', 'linestyle': '' }
    return line_cfg

def new_lines_fig3a(dict_data,color='b'):
    line_cfg = {}
    for key, file in dict_data.items():
        bg_fig_file=merge_csv_files_ss(file)
        pdf=pd.read_csv(bg_fig_file)
        num_simulations=len(pdf)        
        if 'ss' in key:
            yvar='v_NKE'
            xvar='c_Nai'
            ydata_array=pdf[yvar].values/pdf[yvar].values[7]
            line_cfg[key] = { 'xdata': (bg_fig_file,xvar), 'ydata_array': ydata_array,
                'color': color,   'linestyle': '-.'}
        else:
            yvar='v_r1'
            xvar='c_Nai'
            ydata_array=pdf[yvar].values/pdf[yvar].values[int(num_simulations-2)]
            line_cfg[key] = { 'xdata': (bg_fig_file,xvar), 'ydata_array': ydata_array,
                'color': color,   'marker': '+', 'linestyle': ''}
    return line_cfg

def new_lines_fig3b(dict_data,color='b'):
    line_cfg = {}
    for key, file in dict_data.items():
        bg_fig_file=merge_csv_files_ss(file)
        pdf=pd.read_csv(bg_fig_file)
        num_simulations=len(pdf)
        if 'ss' in key:
            yvar='v_NKE'
            xvar='c_Ko'
            ydata_array=pdf[yvar].values/pdf[yvar].values[8]
            line_cfg[key] = { 'xdata': (bg_fig_file,xvar), 'ydata_array': ydata_array,
                'color': color,   'linestyle': '-.'}
        else:
            yvar='v_r1'
            xvar='c_Ko'
            ydata_array=pdf[yvar].values/pdf[yvar].values[int(num_simulations-2)]
            line_cfg[key] = { 'xdata': (bg_fig_file,xvar), 'ydata_array': ydata_array,
                'color': color,   'marker': '+', 'linestyle': ''}
    return line_cfg

def new_lines_fig3c(dict_data,color='b'):
    line_cfg = {}
    for key, file in dict_data.items():
        bg_fig_file=merge_csv_files_ss(file)
        pdf=pd.read_csv(bg_fig_file)
        if 'ss' in key:
            yvar='v_NKE'
            xvar='c_ATP'
            ydata_array=pdf[yvar].values/pdf[yvar].values[-1]
            line_cfg[key] = { 'xdata': (bg_fig_file,xvar), 'ydata_array': ydata_array,
                'color': color,   'linestyle': '-.'}
        else:
            yvar='v_r1'
            xvar='c_ATP'
            ydata_array=pdf[yvar].values/pdf[yvar].values[-1]
            line_cfg[key] = { 'xdata': (bg_fig_file,xvar), 'ydata_array': ydata_array,
                'color': color,   'marker': '+', 'linestyle': ''}
    return line_cfg

def plot_cfg_ss(lines_dict):
    plot_cfg = {}
    for plot_id, line_group in lines_dict.items():
        plot_cfg[plot_id] = {'ylabel': line_group['ylabel'], 'xlabel': line_group['xlabel'], 'title_y': -0.3,
                'line': line_group['line'], 'legend': line_group['line'],'lgdncol': 1}
    return plot_cfg

if __name__ == '__main__':
    
    save_fig_fig2a = {'save_fig': True, 'fig_format': 'eps', 'file_path': simulation_path.as_posix()+'/', 'filename': 'NKE_BG_6_stateV2_fig2a_fit'}
    fig_cfg_fig2a = {'num_rows': 1, 'num_cols': 1, 'width':3.5, 'height':3.5, 'fig_title': None, 'title_y': 1, 'fontsize': 10, 
               'legend_kwargs': {'fontsize': 8, 'loc': 'best', 'ncols': 2},
           'left': 0.15, 'bottom': 0.15, 'right': 0.9, 'top': 0.95, 'wspace': 0.2, 'hspace': 0.4}|save_fig_fig2a
    save_fig_fig2b = {'save_fig': True, 'fig_format': 'eps', 'file_path': simulation_path.as_posix()+'/', 'filename': 'NKE_BG_6_stateV2_fig2b_fit'}
    fig_cfg_fig2b = {'num_rows': 1, 'num_cols': 1, 'width':3.5, 'height':3.5, 'fig_title': None, 'title_y': 1, 'fontsize': 10, 
               'legend_kwargs': {'fontsize': 8, 'loc': 'best', 'ncols': 2},
           'left': 0.15, 'bottom': 0.15, 'right': 0.9, 'top': 0.95, 'wspace': 0.2, 'hspace': 0.4}|save_fig_fig2b
    save_fig_fig3a = {'save_fig': True, 'fig_format': 'eps', 'file_path': simulation_path.as_posix()+'/', 'filename': 'NKE_BG_6_stateV2_fig3a_fit'}
    fig_cfg_fig3a = {'num_rows': 1, 'num_cols': 1, 'width':3.5, 'height':3.5, 'fig_title': None, 'title_y': 1, 'fontsize': 10, 
               'legend_kwargs': {'fontsize': 8, 'loc': 'best', 'ncols': 2},
           'left': 0.15, 'bottom': 0.15, 'right': 0.9, 'top': 0.95, 'wspace': 0.2, 'hspace': 0.4}|save_fig_fig3a
    save_fig_fig3b = {'save_fig': True, 'fig_format': 'eps', 'file_path': simulation_path.as_posix()+'/', 'filename': 'NKE_BG_6_stateV2_fig3b_fit'}
    fig_cfg_fig3b = {'num_rows': 1, 'num_cols': 1, 'width':3.5, 'height':3.5, 'fig_title': None, 'title_y': 1, 'fontsize': 10, 
               'legend_kwargs': {'fontsize': 8, 'loc': 'best', 'ncols': 2},
           'left': 0.15, 'bottom': 0.15, 'right': 0.9, 'top': 0.95, 'wspace': 0.2, 'hspace': 0.4}|save_fig_fig3b
    save_fig_fig3c = {'save_fig': True, 'fig_format': 'eps', 'file_path': simulation_path.as_posix()+'/', 'filename': 'NKE_BG_6_stateV2_fig3c_fit'}
    fig_cfg_fig3c = {'num_rows': 1, 'num_cols': 1, 'width':3.5, 'height':3.5, 'fig_title': None, 'title_y': 1, 'fontsize': 10, 
               'legend_kwargs': {'fontsize': 8, 'loc': 'best', 'ncols': 2},
           'left': 0.15, 'bottom': 0.15, 'right': 0.9, 'top': 0.95, 'wspace': 0.2, 'hspace': 0.4}|save_fig_fig3c

    data_dict_15state={'u_Vm': 'report_task_NKE_BG_15_state_fixedV_fig5',
               'c_Nai': 'report_task_NKE_BG_15_state_fixedV_fig3a',
               'c_Ko': 'report_task_NKE_BG_15_state_fixedV_fig3b',
               'c_ATP': 'report_task_NKE_BG_15_state_fixedV_fig3c'}

    data_dict_6state_v1_ss_steph_v0_fig2a={
            'fig2a1_ss': 'report_task_NKE_BG_6_state_ATPNaZKV2_SS_fixedV_fig2a1',
            'fig2a2_ss': 'report_task_NKE_BG_6_state_ATPNaZKV2_SS_fixedV_fig2a2',
            'fig2a3_ss': 'report_task_NKE_BG_6_state_ATPNaZKV2_SS_fixedV_fig2a3',
            'fig2a4_ss': 'report_task_NKE_BG_6_state_ATPNaZKV2_SS_fixedV_fig2a4',
            'fig2a1_bg': 'report_task_NKE_BG_6_state_ATPNaZKV2_fixedV_fig2a1',
            'fig2a2_bg': 'report_task_NKE_BG_6_state_ATPNaZKV2_fixedV_fig2a2',
            'fig2a3_bg': 'report_task_NKE_BG_6_state_ATPNaZKV2_fixedV_fig2a3',
            'fig2a4_bg': 'report_task_NKE_BG_6_state_ATPNaZKV2_fixedV_fig2a4',
            }
    data_dict_6state_v1_ss_steph_v0_fig2b={
            'fig2b1_ss': 'report_task_NKE_BG_6_state_ATPNaZKV2_SS_fixedV_fig2b1',
            'fig2b2_ss': 'report_task_NKE_BG_6_state_ATPNaZKV2_SS_fixedV_fig2b2',
            'fig2b3_ss': 'report_task_NKE_BG_6_state_ATPNaZKV2_SS_fixedV_fig2b3',
            'fig2b1_bg': 'report_task_NKE_BG_6_state_ATPNaZKV2_fixedV_fig2b1',
            'fig2b2_bg': 'report_task_NKE_BG_6_state_ATPNaZKV2_fixedV_fig2b2',
            'fig2b3_bg': 'report_task_NKE_BG_6_state_ATPNaZKV2_fixedV_fig2b3',
            }
    
    data_dict_6state_v1_ss_steph_v0_fig3a={
            'fig3a_ss': 'report_task_NKE_BG_6_state_ATPNaZKV2_SS_fixedV_fig3a',
            'fig3a_bg': 'report_task_NKE_BG_6_state_ATPNaZKV2_fixedV_fig3a',
            }   
    data_dict_6state_v1_ss_steph_v0_fig3b={
            'fig3b_ss': 'report_task_NKE_BG_6_state_ATPNaZKV2_SS_fixedV_fig3b',
            'fig3b_bg': 'report_task_NKE_BG_6_state_ATPNaZKV2_fixedV_fig3b',
            }
    data_dict_6state_v1_ss_steph_v0_fig3c={
            'fig3c_ss': 'report_task_NKE_BG_6_state_ATPNaZKV2_SS_fixedV_fig3c',
            'fig3c_bg': 'report_task_NKE_BG_6_state_ATPNaZKV2_fixedV_fig3c',
            }       

    # construct lines for 15-state and 6-state model
    lines_dict_fig2a={1:{'xlabel': 'Membrane voltage (mV)', 'ylabel':'Cycling velocity (s$^{-1}$)',
                         'line':['fig2a1_data', 'fig2a2_data', 'fig2a3_data', 'fig2a4_data',
                                 'fig2a1_kinetic', 'fig2a2_kinetic', 'fig2a3_kinetic', 'fig2a4_kinetic',
                                 'fig2a1_ss', 'fig2a2_ss', 'fig2a3_ss', 'fig2a4_ss',
                                 'fig2a1_bg', 'fig2a2_bg', 'fig2a3_bg', 'fig2a4_bg']},}
    
    lines_dict_fig2b={1:{'xlabel': 'Membrane voltage (mV)', 'ylabel':'Current density (uA/uF)',
                         'line':['fig2b1_data', 'fig2b2_data', 'fig2b3_data',
                                 'fig2b1_kinetic', 'fig2b2_kinetic', 'fig2b3_kinetic',
                                 'fig2b1_ss', 'fig2b2_ss', 'fig2b3_ss',
                                 'fig2b1_bg', 'fig2b2_bg', 'fig2b3_bg']},}
    lines_dict_fig3a={1:{'xlabel': '[Na$_i$] (mM)', 'ylabel':'Relative cycling velocity',
                         'line':['fig3a_data',
                                 'fig3a_kinetic',
                                 'fig3a_ss',
                                 'fig3a_bg']},}
    lines_dict_fig3b={1:{'xlabel': '[K$_o$] (mM)', 'ylabel':'Relative cycling velocity',
                         'line':['fig3b_data',
                                 'fig3b_kinetic',
                                 'fig3b_ss',
                                 'fig3b_bg']},}     
    lines_dict_fig3c={1:{'xlabel': '[ATP] (mM)', 'ylabel':'Relative cycling velocity',
                         'line':['fig3c_data',
                                 'fig3c_kinetic',
                                 'fig3c_ss',                                 
                                 'fig3c_bg']},} 
    
    lines_cfg=original_data_fig2a()
    lines_cfg.update(original_data_fig2b())
    lines_cfg.update(original_data_fig3a())
    lines_cfg.update(original_data_fig3b())
    lines_cfg.update(original_data_fig3c())
    lines_cfg.update(original_kinetic_ss_fig2a())
    lines_cfg.update(original_kinetic_ss_fig2b())
    lines_cfg.update(original_kinetic_ss_fig3a())
    lines_cfg.update(original_kinetic_ss_fig3b())
    lines_cfg.update(original_kinetic_ss_fig3c())
    lines_fig2a=new_lines_fig2a(data_dict_6state_v1_ss_steph_v0_fig2a)
    lines_fig2b=new_lines_fig2b(data_dict_6state_v1_ss_steph_v0_fig2b)
    lines_fig3a=new_lines_fig3a(data_dict_6state_v1_ss_steph_v0_fig3a)
    lines_fig3b=new_lines_fig3b(data_dict_6state_v1_ss_steph_v0_fig3b)
    lines_fig3c=new_lines_fig3c(data_dict_6state_v1_ss_steph_v0_fig3c)
    
    lines_cfg.update(lines_fig2a)
    lines_cfg.update(lines_fig2b)
    lines_cfg.update(lines_fig3a)
    lines_cfg.update(lines_fig3b)
    lines_cfg.update(lines_fig3c)   
    plot_cfg_fig2a = plot_cfg_ss(lines_dict_fig2a)
    plot_cfg_fig2b = plot_cfg_ss(lines_dict_fig2b)
    plot_cfg_fig3a = plot_cfg_ss(lines_dict_fig3a)
    plot_cfg_fig3b = plot_cfg_ss(lines_dict_fig3b)
    plot_cfg_fig3c = plot_cfg_ss(lines_dict_fig3c)

    plot_line2D(fig_cfg_fig2a, plot_cfg_fig2a, lines_cfg)
    plot_line2D(fig_cfg_fig2b, plot_cfg_fig2b, lines_cfg)
    plot_line2D(fig_cfg_fig3a, plot_cfg_fig3a, lines_cfg)
    plot_line2D(fig_cfg_fig3b, plot_cfg_fig3b, lines_cfg)
    plot_line2D(fig_cfg_fig3c, plot_cfg_fig3c, lines_cfg)
