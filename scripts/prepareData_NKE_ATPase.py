import os
import sys
import pandas as pd
# Get the directory containing the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
path_=os.path.join(current_dir, '../cad/data/')
from dataPlot.manData import combine_csv_files

C_m=153400
new_csv_file = path_+'Terkildsen_NaK_kinetic_Nai.csv'
ss_csv_file_Nai=path_+'Terkildsen_NaK_kinetic_Fig3a_Data.csv'

csv_files=[(ss_csv_file_Nai, 0, 0),
           (ss_csv_file_Nai, 51, 51), (ss_csv_file_Nai, 101, 101), (ss_csv_file_Nai, 201, 201),
           (ss_csv_file_Nai, 251, 251), (ss_csv_file_Nai, 301, 301),(ss_csv_file_Nai, 351, 351),(ss_csv_file_Nai, 401, 401),
           (ss_csv_file_Nai, 501, 501),  (ss_csv_file_Nai, 601, 601), (ss_csv_file_Nai, 801, 801)]

combine_csv_files(new_csv_file, csv_files)

ss_csv_file_new=path_+'Terkildsen_NaK_kinetic_Nai_cond.csv'
df_ss_new = pd.DataFrame()
df_ss_old = pd.read_csv(new_csv_file)
N_cond=len(df_ss_old['environment | t (second)'])

u_e=0
small_value=1e-3
df_ss_new['u_0_Vm'] = [u_e for i in range(N_cond)]
df_ss_new['c_Nai'] = df_ss_old['environment | Nai (mM)']
df_ss_new['c_Nao']=[5 for i in range(N_cond)]
df_ss_new['c_Ki']=[80 for i in range(N_cond)]
df_ss_new['c_Ko']=[15 for i in range(N_cond)]
df_ss_new['c_Pi']=[1 for i in range(N_cond)]
df_ss_new['c_ATP']=[2 for i in range(N_cond)]
df_ss_new['c_ADP']=[small_value for i in range(N_cond)]
df_ss_new['T']=[308 for i in range(N_cond)]
df_ss_new['pH']=[7.2 for i in range(N_cond)]
df_ss_new['v_ss'] = df_ss_old['environment | v_cyc_nak (per_second)']
df_ss_new.to_csv(ss_csv_file_new, index=False)

new_csv_file = path_+'Terkildsen_NaK_kinetic_Ke.csv'
ss_csv_file_Nai=path_+'Terkildsen_NaK_kinetic_Fig3b_Data.csv'

csv_files=[(ss_csv_file_Nai, 0, 0),
           (ss_csv_file_Nai, 3, 3), (ss_csv_file_Nai, 11, 11),(ss_csv_file_Nai, 21, 21),(ss_csv_file_Nai, 31, 31), 
           (ss_csv_file_Nai, 41, 41), (ss_csv_file_Nai, 51, 51), (ss_csv_file_Nai, 61, 61),
            (ss_csv_file_Nai, 81, 81), (ss_csv_file_Nai, 101, 101),(ss_csv_file_Nai, 201, 201)]
combine_csv_files(new_csv_file, csv_files)

small_value=1e-3
ss_csv_file_new=path_+'Terkildsen_NaK_kinetic_Ke_cond.csv'
df_ss_new = pd.DataFrame()
df_ss_old = pd.read_csv(new_csv_file)
N_cond=len(df_ss_old['environment | t (second)'])

u_e=0
df_ss_new['u_0_Vm'] = [u_e for i in range(N_cond)]
df_ss_new['c_Nai'] =[50 for i in range(N_cond)]
df_ss_new['c_Nao']=[150 for i in range(N_cond)]
df_ss_new['c_Ki']=[140 for i in range(N_cond)]
df_ss_new['c_Ko']=df_ss_old['environment | Ke (mM)']
df_ss_new['c_Pi']=[0.5 for i in range(N_cond)]
df_ss_new['c_ATP']=[10 for i in range(N_cond)]
df_ss_new['c_ADP']=[0.02 for i in range(N_cond)]
df_ss_new['T']=[310 for i in range(N_cond)]
df_ss_new['pH']=[7.4 for i in range(N_cond)]
df_ss_new['v_ss'] = df_ss_old['environment | v_cyc_nak (per_second)']
df_ss_new.to_csv(ss_csv_file_new, index=False)

new_csv_file = path_+'Terkildsen_NaK_kinetic_ATP.csv'
ss_csv_file_Nai=path_+'Terkildsen_NaK_kinetic_Fig3c_Data.csv'

csv_files=[(ss_csv_file_Nai, 0, 0),(ss_csv_file_Nai, 2, 2), (ss_csv_file_Nai, 4, 4), (ss_csv_file_Nai, 6, 6),
           (ss_csv_file_Nai, 11, 11), (ss_csv_file_Nai, 16, 16), (ss_csv_file_Nai, 21, 21),
           (ss_csv_file_Nai, 31, 31), (ss_csv_file_Nai, 41, 41), (ss_csv_file_Nai, 51, 51), (ss_csv_file_Nai, 61, 61)]
combine_csv_files(new_csv_file, csv_files)

ss_csv_file_new=path_+'Terkildsen_NaK_kinetic_ATP_cond.csv'
df_ss_new = pd.DataFrame()
df_ss_old = pd.read_csv(new_csv_file)
N_cond=len(df_ss_old['environment | t (second)'])

u_e=0
df_ss_new['u_0_Vm'] = [u_e for i in range(N_cond)]
df_ss_new['c_Nai'] =[40 for i in range(N_cond)]
df_ss_new['c_Nao']=[small_value for i in range(N_cond)]
df_ss_new['c_Ki']=[small_value for i in range(N_cond)]
df_ss_new['c_Ko']=[5 for i in range(N_cond)]
df_ss_new['c_Pi']=[0.005 for i in range(N_cond)]
df_ss_new['c_ATP']=df_ss_old['environment | MgATP (mM)']
df_ss_new['c_ADP']=[small_value for i in range(N_cond)]
df_ss_new['T']=[297 for i in range(N_cond)]
df_ss_new['pH']=[7.4 for i in range(N_cond)]
df_ss_new['v_ss'] = df_ss_old['environment | v_cyc_nak (per_second)']
df_ss_new.to_csv(ss_csv_file_new, index=False)

new_csv_file = path_+'Terkildsen_NaK_kinetic_volt.csv'
ss_csv_file_Nai=path_+'New_Terkildsen_NaK_BG_Fig5_Data.csv'

csv_files=[(ss_csv_file_Nai, 0, 0),
           (ss_csv_file_Nai, 301, 301), (ss_csv_file_Nai, 451, 451),(ss_csv_file_Nai, 601, 601),
           (ss_csv_file_Nai, 751, 751), (ss_csv_file_Nai, 901, 901), (ss_csv_file_Nai, 1101, 1101),(ss_csv_file_Nai, 1201, 1201)
           , (ss_csv_file_Nai, 1301, 1301),(ss_csv_file_Nai, 1501, 1501), (ss_csv_file_Nai, 1701, 1701)]
combine_csv_files(new_csv_file, csv_files)

ss_csv_file_new=path_+'Terkildsen_NaK_kinetic_volt_cond.csv'
df_ss_new = pd.DataFrame()
df_ss_old = pd.read_csv(new_csv_file)
N_cond=len(df_ss_old['environment | t (second)'])

df_ss_new['u_0_Vm'] = df_ss_old['environment | V_mem (volt)']
df_ss_new['c_Nai'] =[50 for i in range(N_cond)]
df_ss_new['c_Nao']=[150 for i in range(N_cond)]
df_ss_new['c_Ki']=[small_value for i in range(N_cond)]
df_ss_new['c_Ko']=[5.4 for i in range(N_cond)]
df_ss_new['c_Pi']=[small_value for i in range(N_cond)]
df_ss_new['c_ATP']=[10 for i in range(N_cond)]
df_ss_new['c_ADP']=[small_value for i in range(N_cond)]
df_ss_new['T']=[310 for i in range(N_cond)]
df_ss_new['pH']=[7.4 for i in range(N_cond)]
df_ss_new['v_ss'] = df_ss_old['environment | v_R1 (fmol_per_sec)']
df_ss_new.to_csv(ss_csv_file_new, index=False)