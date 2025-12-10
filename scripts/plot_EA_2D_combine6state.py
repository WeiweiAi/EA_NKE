import sys
import os
# Add parent directory to sys.path for module imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Add 'dataPlot' subdirectory to sys.path for module imports
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'dataPlot'))

# Import Path for filesystem operations
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm

import pandas as pd
simulation_path = Path(__file__).parent.parent / 'cad' / 'models' / 'simulation'
path_ = Path(__file__).parent.parent / 'cad' /  'data'
exp_id=['Nai','Ko','ATP','ADP','Pi','pH']
exp_id=['ATP','ADP','Pi','pH']
file_deltaG='deltaG_efficiency_report_task_NKE_BG_6_state_ATPNaZK_free'
T_0=np.array([600,800,1000,1200])
z_var_names=['Thermodynamic efficiency', 'Chemical conversion efficiency', 
             'Electrical conversion efficiency', 'Chemical-Electrical ratio',
             'ATP Hydrolysis Power','Mean flow rate']
subtitles=[r'Thermodynamic efficiency $\eta$ (%)', r'Chemical conversion efficiency $\eta_c$ (%)', 
           r'Electrical conversion efficiency $\eta_e$ (%)', r'Chemical-Electrical ratio $\gamma$',
           'ATP Hydrolysis Power (pW)', 'Mean flow rate (fmol/s)']
# Chemical conversion efficiency, Electrical conversion efficiency, Chemical-Electrical ratio
basefile_1='EA_report_task_NKE_BG_6_state_ATPNaZK_free_SS_'
basefile_2='EA_report_task_NKE_BG_6_state_ATPNaZK_free_'
col_map = cm.get_cmap('viridis', len(T_0))
for i,z_var_name in enumerate(z_var_names):
    ncols=2
    nrows=2
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(8,8))
    fig.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.15)
    #add title
    fig.suptitle(f'{subtitles[i]}', fontsize=16)
    fig_name=f'EA_2D_combine_6state_{z_var_name}'.replace(' ','_').replace('-','_') 
    for i in range(len(exp_id)):
        filename_T600=Path(simulation_path /f'{basefile_1}{exp_id[i]}_T600ms.csv').as_posix()
        filename_T800=Path(simulation_path /f'{basefile_1}{exp_id[i]}_T800ms.csv').as_posix()
        filename_T1000=Path(simulation_path /f'{basefile_1}{exp_id[i]}_T1000ms.csv').as_posix()
        filename_T1200=Path(simulation_path /f'{basefile_1}{exp_id[i]}_T1200ms.csv').as_posix()
        c=pd.read_csv(Path(simulation_path /f'{exp_id[i]}.csv').as_posix())['{}'.format(exp_id[i])].values
        efficiency_T600=pd.read_csv(filename_T600)[z_var_name].values
        efficiency_T800=pd.read_csv(filename_T800)[z_var_name].values
        efficiency_T1000=pd.read_csv(filename_T1000)[z_var_name].values
        efficiency_T1200=pd.read_csv(filename_T1200)[z_var_name].values
        filename_T1000_2=Path(simulation_path /f'{basefile_2}{exp_id[i]}_T1000ms.csv').as_posix()
        filename_T800_2=Path(simulation_path /f'{basefile_2}{exp_id[i]}_T800ms.csv').as_posix()
        filename_T600_2=Path(simulation_path /f'{basefile_2}{exp_id[i]}_T600ms.csv').as_posix()
        filename_T1200_2=Path(simulation_path /f'{basefile_2}{exp_id[i]}_T1200ms.csv').as_posix()
        efficiency_T1000_2=pd.read_csv(filename_T1000_2)[z_var_name].values
        efficiency_T800_2=pd.read_csv(filename_T800_2)[z_var_name].values
        efficiency_T600_2=pd.read_csv(filename_T600_2)[z_var_name].values
        efficiency_T1200_2=pd.read_csv(filename_T1200_2)[z_var_name].values
        deltaG=pd.read_csv(Path(simulation_path /f'{file_deltaG}_{exp_id[i]}_T600ms.csv').as_posix())['ATP_hydrolysis'].values/1000  #kJ/mol
        X=c
        Y1s=[]
        Y2s=[]
        r, c = divmod(i, ncols)
        for idx, T in enumerate(T_0):
            if T==600:
                Y1, Y2, label = efficiency_T600, efficiency_T600_2, 'T=600ms'
            elif T==800:
                Y1, Y2, label = efficiency_T800, efficiency_T800_2, 'T=800ms'
            elif T==1000:
                Y1, Y2, label = efficiency_T1000, efficiency_T1000_2, 'T=1000ms'
            else:
                Y1, Y2, label = efficiency_T1200, efficiency_T1200_2, 'T=1200ms'
            r, c = divmod(i, ncols)
            color = col_map(idx)  
            if 'Power' in z_var_name: # absolute values
                Y1 = -np.array(Y1)/1000 # pW
                Y2 = -np.array(Y2)/1000
            ax[r,c].plot(X, Y1, marker='.', label=label+'_ss', color=color)
            ax[r,c].plot(X, Y2, marker='x', label=label+'_6state', color=color, linestyle='--')
            ax2=ax[r,c].twinx()
            ax2.plot(X, deltaG, marker='o', label='deltaG_ATP', color='b', linestyle=':')
            ax2.tick_params(axis='y', colors='b')
            ax2.set_ylabel(r'$\Delta G_{ATP}$ (kJ/mol)', color='b')
            ax[r,c].grid(True, linestyle='--', alpha=0.5)
            Y1s.append(Y1)
            Y2s.append(Y2)
        if 'efficiency' in z_var_name:
            # ymax to max(Y1,Y2)+10%
            # if min(Y1,Y2)>0, set ymin to min(Y1,Y2)-10%,else set ymin to 0
            if min(np.min(Y1s), np.min(Y2s))>0:
                ymin = min(np.min(Y1s), np.min(Y2s)) * 0.95
            else:
                ymin = 0
            ymax = max(np.max(Y1s), np.max(Y2s)) * 1.05
            ax[r,c].set_ylim(ymin, ymax)     
        
    # show legend only on the first subplot
    ax[0,0].legend(title='Cycle length', loc='upper right', fontsize='small')
    for j in range(nrows):
        for k in range(ncols):
            if 'pH' in exp_id[j*ncols+k]:
                ax[j,k].set_xlabel('pH')
            else:
                ax[j,k].set_xlabel(f'{exp_id[j*ncols+k]} (mM)')       

    #plt.tight_layout()
    save_fig = {'save_fig': True, 'fig_format': 'png', 'file_path': simulation_path.as_posix()+'/', 'filename': fig_name}
    plt.savefig(save_fig['file_path'] + save_fig['filename'] + '.' + save_fig['fig_format'])
    plt.show()

