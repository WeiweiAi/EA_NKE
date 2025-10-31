import os
import sys
import pandas as pd
# Get the directory containing the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
path_=os.path.join(current_dir, '../cad/data/')
from dataPlot.manData import combine_csv_files

C_m=153400
new_csv_file = path_+'Hansen_Nai.csv'

ss_csv_file_new=path_+'fig3a_cond.csv'
df_ss_new = pd.DataFrame()
df_ss_old = pd.read_csv(new_csv_file)
N_cond=len(df_ss_old['x'])

u_e=0
small_value=1e-3
df_ss_new['u_0_Vm'] = [u_e for i in range(N_cond)]
df_ss_new['c_Nai'] = df_ss_old['x']
df_ss_new['c_Nao']=[5 for i in range(N_cond)]
df_ss_new['c_Ki']=[80 for i in range(N_cond)]
df_ss_new['c_Ko']=[15 for i in range(N_cond)]
df_ss_new['c_Pi']=[1 for i in range(N_cond)]
df_ss_new['c_ATP']=[2 for i in range(N_cond)]
df_ss_new['c_ADP']=[small_value for i in range(N_cond)]
df_ss_new['T']=[308 for i in range(N_cond)]
df_ss_new['pH']=[7.2 for i in range(N_cond)]
df_ss_new['v_ss'] = df_ss_old['Cycling rate']
df_ss_new.to_csv(ss_csv_file_new, index=False)

new_csv_file = path_+'nakao_gadsby_Ko_activation_points.csv'

small_value=1e-3
ss_csv_file_new=path_+'fig3b_cond.csv'
df_ss_new = pd.DataFrame()
df_ss_old = pd.read_csv(new_csv_file)
N_cond=len(df_ss_old['x'])

u_e=0
df_ss_new['u_0_Vm'] = [u_e for i in range(N_cond)]
df_ss_new['c_Nai'] =[50 for i in range(N_cond)]
df_ss_new['c_Nao']=[150 for i in range(N_cond)]
df_ss_new['c_Ki']=[140 for i in range(N_cond)]
df_ss_new['c_Ko']=df_ss_old['x']
df_ss_new['c_Pi']=[0.5 for i in range(N_cond)]
df_ss_new['c_ATP']=[10 for i in range(N_cond)]
df_ss_new['c_ADP']=[0.02 for i in range(N_cond)]
df_ss_new['T']=[310 for i in range(N_cond)]
df_ss_new['pH']=[7.4 for i in range(N_cond)]
df_ss_new['v_ss'] = df_ss_old['Relative pump current']
df_ss_new.to_csv(ss_csv_file_new, index=False)

new_csv_file = path_+'Friedrich_ATP.csv'

ss_csv_file_new=path_+'fig3c_cond.csv'
df_ss_new = pd.DataFrame()
df_ss_old = pd.read_csv(new_csv_file)
N_cond=len(df_ss_old['x'])

u_e=0
df_ss_new['u_0_Vm'] = [u_e for i in range(N_cond)]
df_ss_new['c_Nai'] =[40 for i in range(N_cond)]
df_ss_new['c_Nao']=[0.1 for i in range(N_cond)]
df_ss_new['c_Ki']=[small_value for i in range(N_cond)]
df_ss_new['c_Ko']=[5 for i in range(N_cond)]
df_ss_new['c_Pi']=[0.005 for i in range(N_cond)]
df_ss_new['c_ATP']=df_ss_old['x']/1000
df_ss_new['c_ADP']=[small_value for i in range(N_cond)]
df_ss_new['T']=[297 for i in range(N_cond)]
df_ss_new['pH']=[7.4 for i in range(N_cond)]
df_ss_new['v_ss'] = df_ss_old['Normalised current']
df_ss_new.to_csv(ss_csv_file_new, index=False)

new_csv_file = path_+'nakao_gadsby_points_new.csv'
ss_csv_file_Nai=path_+'nakao_gadsby_points.csv'

csv_files=[(ss_csv_file_Nai, 0, 0),
           (ss_csv_file_Nai, 4, 41, 4) ]
combine_csv_files(new_csv_file, csv_files)

ss_csv_file_new=path_+'fig2a_cond_1.csv'
df_ss_new = pd.DataFrame()
df_ss_old = pd.read_csv(new_csv_file)
N_cond=len(df_ss_old['x'])

df_ss_new['u_0_Vm'] = df_ss_old['x']/1000
df_ss_new['c_Nai'] =[50 for i in range(N_cond)]
df_ss_new['c_Nao']=[1.5 for i in range(N_cond)]
df_ss_new['c_Ki']=[small_value for i in range(N_cond)]
df_ss_new['c_Ko']=[5.4 for i in range(N_cond)]
df_ss_new['c_Pi']=[small_value for i in range(N_cond)]
df_ss_new['c_ATP']=[10 for i in range(N_cond)]
df_ss_new['c_ADP']=[small_value for i in range(N_cond)]
df_ss_new['T']=[310 for i in range(N_cond)]
df_ss_new['pH']=[7.4 for i in range(N_cond)]
df_ss_new['v_ss'] = df_ss_old['[Na_o] = 1.5mM']
df_ss_new.to_csv(ss_csv_file_new, index=False)

ss_csv_file_new=path_+'fig2a_cond_2.csv'
df_ss_new = pd.DataFrame()
df_ss_old = pd.read_csv(new_csv_file)
N_cond=len(df_ss_old['x'])

df_ss_new['u_0_Vm'] = df_ss_old['x']/1000
df_ss_new['c_Nai'] =[50 for i in range(N_cond)]
df_ss_new['c_Nao']=[50 for i in range(N_cond)]
df_ss_new['c_Ki']=[small_value for i in range(N_cond)]
df_ss_new['c_Ko']=[5.4 for i in range(N_cond)]
df_ss_new['c_Pi']=[small_value for i in range(N_cond)]
df_ss_new['c_ATP']=[10 for i in range(N_cond)]
df_ss_new['c_ADP']=[small_value for i in range(N_cond)]
df_ss_new['T']=[310 for i in range(N_cond)]
df_ss_new['pH']=[7.4 for i in range(N_cond)]
df_ss_new['v_ss'] = df_ss_old['[Na_o] = 50mM']
df_ss_new.to_csv(ss_csv_file_new, index=False)

ss_csv_file_new=path_+'fig2a_cond_3.csv'
df_ss_new = pd.DataFrame()
df_ss_old = pd.read_csv(new_csv_file)
N_cond=len(df_ss_old['x'])

df_ss_new['u_0_Vm'] = df_ss_old['x']/1000
df_ss_new['c_Nai'] =[50 for i in range(N_cond)]
df_ss_new['c_Nao']=[100 for i in range(N_cond)]
df_ss_new['c_Ki']=[small_value for i in range(N_cond)]
df_ss_new['c_Ko']=[5.4 for i in range(N_cond)]
df_ss_new['c_Pi']=[small_value for i in range(N_cond)]
df_ss_new['c_ATP']=[10 for i in range(N_cond)]
df_ss_new['c_ADP']=[small_value for i in range(N_cond)]
df_ss_new['T']=[310 for i in range(N_cond)]
df_ss_new['pH']=[7.4 for i in range(N_cond)]
df_ss_new['v_ss'] = df_ss_old['[Na_o] = 100mM']
df_ss_new.to_csv(ss_csv_file_new, index=False)

ss_csv_file_new=path_+'fig2a_cond_4.csv'
df_ss_new = pd.DataFrame()
df_ss_old = pd.read_csv(new_csv_file)
N_cond=len(df_ss_old['x'])

df_ss_new['u_0_Vm'] = df_ss_old['x']/1000
df_ss_new['c_Nai'] =[50 for i in range(N_cond)]
df_ss_new['c_Nao']=[150 for i in range(N_cond)]
df_ss_new['c_Ki']=[small_value for i in range(N_cond)]
df_ss_new['c_Ko']=[5.4 for i in range(N_cond)]
df_ss_new['c_Pi']=[small_value for i in range(N_cond)]
df_ss_new['c_ATP']=[10 for i in range(N_cond)]
df_ss_new['c_ADP']=[small_value for i in range(N_cond)]
df_ss_new['T']=[310 for i in range(N_cond)]
df_ss_new['pH']=[7.4 for i in range(N_cond)]
df_ss_new['v_ss'] = df_ss_old['[Na_o] = 150mM']
df_ss_new.to_csv(ss_csv_file_new, index=False)

new_csv_file = path_+'Nakao_Gadsby_NaeV_currents_new.csv'
ss_csv_file_Nai=path_+'Nakao_Gadsby_NaeV_currents.csv'

csv_files=[(ss_csv_file_Nai, 0, 0),
           (ss_csv_file_Nai, 1, 34, 3)]
combine_csv_files(new_csv_file, csv_files)
C_m = 183

ss_csv_file_new=path_+'fig2b_cond_1.csv'
df_ss_new = pd.DataFrame()
df_ss_old = pd.read_csv(new_csv_file)
N_cond=len(df_ss_old['x'])

df_ss_new['u_0_Vm'] = df_ss_old['x']/1000
df_ss_new['c_Nai'] =[50 for i in range(N_cond)]
df_ss_new['c_Nao']=[50 for i in range(N_cond)]
df_ss_new['c_Ki']=[small_value for i in range(N_cond)]
df_ss_new['c_Ko']=[5.4 for i in range(N_cond)]
df_ss_new['c_Pi']=[small_value for i in range(N_cond)]
df_ss_new['c_ATP']=[10 for i in range(N_cond)]
df_ss_new['c_ADP']=[small_value for i in range(N_cond)]
df_ss_new['T']=[310 for i in range(N_cond)]
df_ss_new['pH']=[7.4 for i in range(N_cond)]
df_ss_new['v_ss'] = df_ss_old['[Na_e] = 50mM']/C_m
df_ss_new.to_csv(ss_csv_file_new, index=False)

ss_csv_file_new=path_+'fig2b_cond_2.csv'
df_ss_new = pd.DataFrame()
df_ss_old = pd.read_csv(new_csv_file)
N_cond=len(df_ss_old['x'])

df_ss_new['u_0_Vm'] = df_ss_old['x']/1000
df_ss_new['c_Nai'] =[50 for i in range(N_cond)]
df_ss_new['c_Nao']=[100 for i in range(N_cond)]
df_ss_new['c_Ki']=[small_value for i in range(N_cond)]
df_ss_new['c_Ko']=[5.4 for i in range(N_cond)]
df_ss_new['c_Pi']=[small_value for i in range(N_cond)]
df_ss_new['c_ATP']=[10 for i in range(N_cond)]
df_ss_new['c_ADP']=[small_value for i in range(N_cond)]
df_ss_new['T']=[310 for i in range(N_cond)]
df_ss_new['pH']=[7.4 for i in range(N_cond)]
df_ss_new['v_ss'] = df_ss_old['[Na_e] = 100mM']/C_m
df_ss_new.to_csv(ss_csv_file_new, index=False)

ss_csv_file_new=path_+'fig2b_cond_3.csv'
df_ss_new = pd.DataFrame()
df_ss_old = pd.read_csv(new_csv_file)
N_cond=len(df_ss_old['x'])

df_ss_new['u_0_Vm'] = df_ss_old['x']/1000
df_ss_new['c_Nai'] =[50 for i in range(N_cond)]
df_ss_new['c_Nao']=[150 for i in range(N_cond)]
df_ss_new['c_Ki']=[small_value for i in range(N_cond)]
df_ss_new['c_Ko']=[5.4 for i in range(N_cond)]
df_ss_new['c_Pi']=[small_value for i in range(N_cond)]
df_ss_new['c_ATP']=[10 for i in range(N_cond)]
df_ss_new['c_ADP']=[small_value for i in range(N_cond)]
df_ss_new['T']=[310 for i in range(N_cond)]
df_ss_new['pH']=[7.4 for i in range(N_cond)]
df_ss_new['v_ss'] = df_ss_old['[Na_e] = 150mM']/C_m
df_ss_new.to_csv(ss_csv_file_new, index=False)