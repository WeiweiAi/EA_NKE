import sys
import os

from sympy import li

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
    # rule out the files report_task_NKE_BG_15_state_fixedV_fig3a_***_ss.csv
    list_csv_files=[f'{new_csv_file}_{i}.csv' for i in range(10)]    
    first_file=Path(simulation_path/list_csv_files[0]).as_posix()
    csv_files=[(first_file, 0, 0)] # [list_csv_files[0]]
    for csv_file in list_csv_files: 
        csv_files.append((Path(simulation_path/csv_file).as_posix(), 1, 1))
    combine_csv_files(new_csv_file_fullpath, csv_files)
    return new_csv_file_fullpath

def new_lines_ss(dict_data,color='b',label='', ss='v_r1'):
    line_cfg = {}
    for key, file in dict_data.items():
        bg_fig_file=merge_csv_files_ss(file)
        line_cfg[key+'_'+label] = { 'xdata': (bg_fig_file,key), 'ydata':(bg_fig_file,ss),
                'color': color, 'linestyle': '-.',  'label': label}
    return line_cfg


def plot_cfg_ss(lines_dict):
    plot_cfg = {}
    for plot_id, line_group in lines_dict.items():
        plot_cfg[plot_id] = {'ylabel': 'cycle rate (s$^{-1}$)', 'xlabel': line_group['xlabel'],'show_grid': 'both', 'grid_axis': 'both',  'title_y': -0.3,
                'line': line_group['line'], 'legend': line_group['line'],'lgdncol': 1}
    return plot_cfg


if __name__ == '__main__':
    
    save_fig_fig5 = {'save_fig': True, 'fig_format': 'eps', 'file_path': simulation_path.as_posix()+'/', 'filename': 'NKE_BG_6_state_fig5_fit'}
    fig_cfg_fig5 = {'num_rows': 1, 'num_cols': 1, 'width':4, 'height':5, 'fig_title': None, 'title_y': 1, 'fontsize': 8, 
               'legend_kwargs': {'fontsize': 6, 'loc': 'best', 'ncols': 2},
           'left': 0.15, 'bottom': 0.15, 'right': 0.9, 'top': 0.95, 'wspace': 0.2, 'hspace': 0.4}|save_fig_fig5
    save_fig_fig3a = {'save_fig': True, 'fig_format': 'eps', 'file_path': simulation_path.as_posix()+'/', 'filename': 'NKE_BG_6_state_fig3a_fit'}
    fig_cfg_fig3a = {'num_rows': 1, 'num_cols': 1, 'width':4, 'height':5, 'fig_title': None, 'title_y': 1, 'fontsize': 8, 
               'legend_kwargs': {'fontsize': 6, 'loc': 'best', 'ncols': 2},
           'left': 0.15, 'bottom': 0.15, 'right': 0.9, 'top': 0.95, 'wspace': 0.2, 'hspace': 0.4}|save_fig_fig3a
    save_fig_fig3b = {'save_fig': True, 'fig_format': 'eps', 'file_path': simulation_path.as_posix()+'/', 'filename': 'NKE_BG_6_state_fig3b_fit'}
    fig_cfg_fig3b = {'num_rows': 1, 'num_cols': 1, 'width':4, 'height':5, 'fig_title': None, 'title_y': 1, 'fontsize': 8, 
               'legend_kwargs': {'fontsize': 6, 'loc': 'best', 'ncols': 2},
           'left': 0.15, 'bottom': 0.15, 'right': 0.9, 'top': 0.95, 'wspace': 0.2, 'hspace': 0.4}|save_fig_fig3b
    save_fig_fig3c = {'save_fig': True, 'fig_format': 'eps', 'file_path': simulation_path.as_posix()+'/', 'filename': 'NKE_BG_6_state_fig3c_fit'}
    fig_cfg_fig3c = {'num_rows': 1, 'num_cols': 1, 'width':4, 'height':5, 'fig_title': None, 'title_y': 1, 'fontsize': 8, 
               'legend_kwargs': {'fontsize': 6, 'loc': 'best', 'ncols': 2},
           'left': 0.15, 'bottom': 0.15, 'right': 0.9, 'top': 0.95, 'wspace': 0.2, 'hspace': 0.4}|save_fig_fig3c

    data_dict_15state={'u_Vm': 'report_task_NKE_BG_15_state_fixedV_fig5',
               'c_Nai': 'report_task_NKE_BG_15_state_fixedV_fig3a',
               'c_Ko': 'report_task_NKE_BG_15_state_fixedV_fig3b',
               'c_ATP': 'report_task_NKE_BG_15_state_fixedV_fig3c'}

    data_dict_6state_v1_ss_free={'u_Vm': 'report_task_NKE_BG_6_state_ATPNaZK_free_fixedV_fig5_ss',
               'c_Nai': 'report_task_NKE_BG_6_state_ATPNaZK_free_fixedV_fig3a_ss',
               'c_Ko': 'report_task_NKE_BG_6_state_ATPNaZK_free_fixedV_fig3b_ss',
               'c_ATP': 'report_task_NKE_BG_6_state_ATPNaZK_free_fixedV_fig3c_ss'}
    
    data_dict_6state_v2_ss_free={'u_Vm': 'report_task_NKE_BG_6_state_ATPNa_free_fixedV_fig5_ss',
               'c_Nai': 'report_task_NKE_BG_6_state_ATPNa_free_fixedV_fig3a_ss',
               'c_Ko': 'report_task_NKE_BG_6_state_ATPNa_free_fixedV_fig3b_ss',
               'c_ATP': 'report_task_NKE_BG_6_state_ATPNa_free_fixedV_fig3c_ss'}
    
    
    data_dict_6state_v1_ss={'u_Vm': 'report_task_NKE_BG_6_state_ATPNaZK_fixedV_fig5_ss',
               'c_Nai': 'report_task_NKE_BG_6_state_ATPNaZK_fixedV_fig3a_ss',
               'c_Ko': 'report_task_NKE_BG_6_state_ATPNaZK_fixedV_fig3b_ss',
               'c_ATP': 'report_task_NKE_BG_6_state_ATPNaZK_fixedV_fig3c_ss'}
    
    data_dict_6state_v1_ss_v2={'u_Vm': 'report_task_NKE_BG_6_state_ATPNaZK_fixedV_fig5_ss_v2',
               'c_Nai': 'report_task_NKE_BG_6_state_ATPNaZK_fixedV_fig3a_ss_v2',
               'c_Ko': 'report_task_NKE_BG_6_state_ATPNaZK_fixedV_fig3b_ss_v2',
               'c_ATP': 'report_task_NKE_BG_6_state_ATPNaZK_fixedV_fig3c_ss_v2'}

    data_dict_6state_v1_ss_steph_v0={'u_Vm': 'report_task_NKE_BG_6_state_ATPNaZK_fixedV_fig5_ss_steph_v0',
               'c_Nai': 'report_task_NKE_BG_6_state_ATPNaZK_fixedV_fig3a_ss_steph_v0',
               'c_Ko': 'report_task_NKE_BG_6_state_ATPNaZK_fixedV_fig3b_ss_steph_v0',
               'c_ATP': 'report_task_NKE_BG_6_state_ATPNaZK_fixedV_fig3c_ss_steph_v0'}    
    
    data_dict_6state_v1_ss_steph_v0_free={'u_Vm': 'report_task_NKE_BG_6_state_ATPNaZK_free_fixedV_fig5_ss_steph_v0',
               'c_Nai': 'report_task_NKE_BG_6_state_ATPNaZK_free_fixedV_fig3a_ss_steph_v0',
               'c_Ko': 'report_task_NKE_BG_6_state_ATPNaZK_free_fixedV_fig3b_ss_steph_v0',
               'c_ATP': 'report_task_NKE_BG_6_state_ATPNaZK_free_fixedV_fig3c_ss_steph_v0'}

    data_dict_6state_v1_ss_steph_v0_withSS={'u_Vm': 'report_task_NKE_BG_6_state_ATPNaZK_fixedV_withSS_fig5_ss_steph_v0',
               'c_Nai': 'report_task_NKE_BG_6_state_ATPNaZK_fixedV_withSS_fig3a_ss_steph_v0',
               'c_Ko': 'report_task_NKE_BG_6_state_ATPNaZK_fixedV_withSS_fig3b_ss_steph_v0',
               'c_ATP': 'report_task_NKE_BG_6_state_ATPNaZK_fixedV_withSS_fig3c_ss_steph_v0'}
    data_dict_6state_v1_ss_steph_v0_withSS_free={'u_Vm': 'report_task_NKE_BG_6_state_ATPNaZK_free_fixedV_withSS_fig5_ss_steph_v0',
                'c_Nai': 'report_task_NKE_BG_6_state_ATPNaZK_free_fixedV_withSS_fig3a_ss_steph_v0',
                'c_Ko': 'report_task_NKE_BG_6_state_ATPNaZK_free_fixedV_withSS_fig3b_ss_steph_v0',
                'c_ATP': 'report_task_NKE_BG_6_state_ATPNaZK_free_fixedV_withSS_fig3c_ss_steph_v0'}

    data_dict_6state_v2_ss={'u_Vm': 'report_task_NKE_BG_6_state_ATPNa_fixedV_fig5_ss',
               'c_Nai': 'report_task_NKE_BG_6_state_ATPNa_fixedV_fig3a_ss',   
               'c_Ko': 'report_task_NKE_BG_6_state_ATPNa_fixedV_fig3b_ss',           
               'c_ATP': 'report_task_NKE_BG_6_state_ATPNa_fixedV_fig3c_ss'} 
    
    data_dict_6state_v3_ss={'u_Vm': 'report_task_NKE_BG_6_state_ATP_Na_fixedV_fig5_ss',
               'c_Nai': 'report_task_NKE_BG_6_state_ATP_Na_fixedV_fig3a_ss',   
               'c_Ko': 'report_task_NKE_BG_6_state_ATP_Na_fixedV_fig3b_ss',           
               'c_ATP': 'report_task_NKE_BG_6_state_ATP_Na_fixedV_fig3c_ss'} 

    data_dict_6state_v3_ss_v2={'u_Vm': 'report_task_NKE_BG_6_state_ATP_Na_fixedV_fig5_ss_v2',
               'c_Nai': 'report_task_NKE_BG_6_state_ATP_Na_fixedV_fig3a_ss_v2',   
               'c_Ko': 'report_task_NKE_BG_6_state_ATP_Na_fixedV_fig3b_ss_v2',           
               'c_ATP': 'report_task_NKE_BG_6_state_ATP_Na_fixedV_fig3c_ss_v2'}        

    line_suffix=['15-state',
                 '6-state_v1_full_BG','6-state_v1_ss','6-state_v1_full_BG_free','6-state_v1_ss_free']
    # construct lines for 15-state and 6-state model
    lines_dict_fig5={1:{'xlabel': 'potential (mV)', 'line':['volt']},}
    lines_dict_fig3a={1:{'xlabel': 'Na_i (mM)', 'line':['Nai']},}
    lines_dict_fig3b={1:{'xlabel': 'K_e (mM)', 'line':['Ke']},}
    lines_dict_fig3c={1:{'xlabel': 'ATP (mM)', 'line':['ATP']},}    
    for line in line_suffix:
        lines_dict_fig5[1]['line'].append('u_Vm_'+line)
        lines_dict_fig3a[1]['line'].append('c_Nai_'+line)
        lines_dict_fig3b[1]['line'].append('c_Ko_'+line)
        lines_dict_fig3c[1]['line'].append('c_ATP_'+line)
    

    line_cfg_15state=new_lines_ss(data_dict_15state,'b','15-state')
    line_cfg_6state_v1_ss=new_lines_ss(data_dict_6state_v1_ss,'g','6-state_v1_ss')
    line_cfg_6state_v1_ss_v2=new_lines_ss(data_dict_6state_v1_ss_v2,'orange','6-state_v1_ss_v2')
    line_cfg_6state_v1_ss_steph_v0=new_lines_ss(data_dict_6state_v1_ss_steph_v0,'r','6-state_v1_full_BG')
    line_cfg_6state_v1_ss_steph_v0_withSS=new_lines_ss(data_dict_6state_v1_ss_steph_v0_withSS,'orange','6-state_v1_ss','v_NKE')
    line_cfg_6state_v1_ss_steph_v0_free=new_lines_ss(data_dict_6state_v1_ss_steph_v0_free,'c','6-state_v1_full_BG_free')
    line_cfg_6state_v1_ss_steph_v0_free_withSS=new_lines_ss(data_dict_6state_v1_ss_steph_v0_withSS_free,'m','6-state_v1_ss_free','v_NKE')
    line_cfg_6state_v2_ss=new_lines_ss(data_dict_6state_v2_ss,'c','6-state_v2_ss')
    line_cfg_6state_v3_ss_v2=new_lines_ss(data_dict_6state_v3_ss_v2,'r','6-state_v3_ss_v2')
    original_line_cfg=original_lines_ss()
    original_line_cfg.update(line_cfg_15state)
    original_line_cfg.update(line_cfg_6state_v1_ss)
    original_line_cfg.update(line_cfg_6state_v2_ss)
    original_line_cfg.update(line_cfg_6state_v3_ss_v2)
    original_line_cfg.update(line_cfg_6state_v1_ss_v2)
    original_line_cfg.update(line_cfg_6state_v1_ss_steph_v0)
    original_line_cfg.update(line_cfg_6state_v1_ss_steph_v0_withSS)
    original_line_cfg.update(line_cfg_6state_v1_ss_steph_v0_free)
    original_line_cfg.update(line_cfg_6state_v1_ss_steph_v0_free_withSS)
    plot_cfg_fig5 = plot_cfg_ss(lines_dict_fig5)
    plot_cfg_fig3a = plot_cfg_ss(lines_dict_fig3a)
    plot_cfg_fig3b = plot_cfg_ss(lines_dict_fig3b)
    plot_cfg_fig3c = plot_cfg_ss(lines_dict_fig3c)

    plot_line2D(fig_cfg_fig5, plot_cfg_fig5, original_line_cfg)
    plot_line2D(fig_cfg_fig3a, plot_cfg_fig3a, original_line_cfg)
    plot_line2D(fig_cfg_fig3b, plot_cfg_fig3b, original_line_cfg)
    plot_line2D(fig_cfg_fig3c, plot_cfg_fig3c, original_line_cfg)
