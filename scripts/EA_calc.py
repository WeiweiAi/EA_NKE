import re
import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from EA.EA import calc_energy
from sympy import sympify
import pandas as pd

def calc_EA(data_path, basefile, reaction_list, storage_list):
    # files ending with _<number>.csv in data_path
    list_csv_files = [f for f in os.listdir(data_path) if f.startswith(basefile+'_') and f.split('_')[-1].split('.')[0].isdigit() and f.endswith('.csv')]
    
    for filename in list_csv_files:
        result_csv=data_path / filename
         # create a dictionary to hold the power expressions for each component
        P_comp_expr_dict={}
        for reaction in reaction_list:
            P_comp_expr_dict[reaction]=sympify(f'mu_{reaction}_0')*sympify(f'v_{reaction}')-sympify(f'mu_{reaction}_1')*sympify(f'v_{reaction}')

        for storage in storage_list:
            P_comp_expr_dict[storage]=sympify(f'v_{storage}')*sympify(f'mu_{storage}')

        P_comp_expr_dict['Vm']=sympify(f'u_Vm')*sympify(f'i_Vm')
        P_comp_expr_dict['itv']=sympify(f'v_r1')

        csv_file_name=result_csv.as_posix().replace('.csv','EA')
        calc_energy(P_comp_expr_dict,result_csv,csv_file_name=csv_file_name)
        


def calc_EA_summary(data_path, basefile, reaction_list, storage_list):  
    ATP_hydrolysis =['ATP','ADP','Pi','H']
    E_dict = {}        
    # create a dictionary to hold the power expressions for each component
    list_csv_files = [f for f in os.listdir(data_path) if f.startswith(basefile+'_') and f.endswith('EA_summary.csv')]
    # sort list_csv_files by the number after the last underscore
    list_csv_files_sorted=sorted(list_csv_files, key=lambda x: int(re.search(r'(\d+)EA', x).group(1)))
    for filename in list_csv_files_sorted:
        result_csv=data_path / filename
        df = pd.read_csv(result_csv)
        # compute energy for each component
        E_ATP=0
        P_ATP=0
        for comp in ATP_hydrolysis:
            E_ATP+=df.loc[df['Component']==comp,'Energy'].values[0]
            P_ATP+=df.loc[df['Component']==comp,'meanPower'].values[0]
        E_dict['ATP Hydrolysis Energy'] = E_dict.get('ATP Hydrolysis Energy', []) + [E_ATP]
        E_dict['ATP Hydrolysis Power'] = E_dict.get('ATP Hydrolysis Power', []) + [P_ATP]
        E_R=0
        P_R=0
        for reaction in reaction_list:
            E_R+=df.loc[df['Component']==reaction,'Energy'].values[0]
            P_R+=df.loc[df['Component']==reaction,'meanPower'].values[0]
        E_dict['Reactions Heat Production'] = E_dict.get('Reactions Heat Production', []) + [E_R]
        E_dict['Reactions Power'] = E_dict.get('Reactions Power', []) + [P_R]
        E_S=0
        P_S=0
        for storage in storage_list:
            E_S+=df.loc[df['Component']==storage,'Energy'].values[0]
            P_S+=df.loc[df['Component']==storage,'meanPower'].values[0]
        E_dict['Storage Energy'] = E_dict.get('Storage Energy', []) + [E_S]
        E_dict['Storage Power'] = E_dict.get('Storage Power', []) + [P_S]

        P_Nai=0
        P_Nao=0
        P_Ki=0
        P_Ko=0
        P_Vm=0
        P_itv=0
        E_Nai=0
        E_Nai+=df.loc[df['Component']=='Nai','Energy'].values[0]
        P_Nai+=df.loc[df['Component']=='Nai','meanPower'].values[0]
        E_dict['Nai Energy'] = E_dict.get('Nai Energy', []) + [E_Nai]
        E_dict['Nai Power'] = E_dict.get('Nai Power', []) + [P_Nai]
        E_Nao=0
      
        E_Nao+=df.loc[df['Component']=='Nao','Energy'].values[0]
        P_Nao+=df.loc[df['Component']=='Nao','meanPower'].values[0]
        E_dict['Nao Energy'] = E_dict.get('Nao Energy', []) +  [E_Nao]
        E_dict['Nao Power'] = E_dict.get('Nao Power', []) + [P_Nao]
        E_Ki=0
    
        E_Ki+=df.loc[df['Component']=='Ki','Energy'].values[0]
        P_Ki+=df.loc[df['Component']=='Ki','meanPower'].values[0]
        E_dict['Ki Energy'] = E_dict.get('Ki Energy', []) + [E_Ki]
        E_dict['Ki Power'] = E_dict.get('Ki Power', []) + [P_Ki]
        E_Ko=0

        E_Ko+=df.loc[df['Component']=='Ko','Energy'].values[0]
        E_dict['Ko Energy'] = E_dict.get('Ko Energy', []) + [E_Ko]
        P_Ko+=df.loc[df['Component']=='Ko','meanPower'].values[0]
        E_dict['Ko Power'] = E_dict.get('Ko Power', []) + [P_Ko]
        E_Vm=0
    
        E_Vm+=df.loc[df['Component']=='Vm','Energy'].values[0]
        E_dict['Vm Energy'] = E_dict.get('Vm Energy', []) + [E_Vm]
        P_Vm+=df.loc[df['Component']=='Vm','meanPower'].values[0]
        E_dict['Vm Power'] = E_dict.get('Vm Power', []) + [P_Vm]

        E_itv=0    
        P_itv=0
        E_itv+=df.loc[df['Component']=='itv','Energy'].values[0]
        E_dict['Mole quantity'] = E_dict.get('Mole quantity', []) + [E_itv]
        P_itv+=df.loc[df['Component']=='itv','meanPower'].values[0]
        E_dict['Mean flow rate'] = E_dict.get('Mean flow rate', []) + [P_itv]
         # total energy
        E_total=E_R+E_S+E_ATP+E_Nai+E_Nao+E_Ki+E_Ko+E_Vm
        E_dict['Na Energy']=E_dict.get('Na Energy', []) + [E_Nai+E_Nao]
        E_dict['K Energy']=E_dict.get('K Energy', []) + [E_Ki+E_Ko]
        E_dict['Na_K_ratio'] = E_dict.get('Na_K_ratio', []) + [(E_Nai+E_Nao)/(E_Ki+E_Ko) if (E_Ki+E_Ko)!=0 else np.nan]
        E_dict['Total'] = E_dict.get('Total', []) + [E_total]
        E_dict['Stored Energy'] = E_dict.get('Stored Energy', []) + [E_total-E_R-E_ATP]
        E_dict['Dissipation-Stored ratio'] = E_dict.get('Dissipation-Stored ratio', []) + [E_R/(E_total-E_R-E_ATP) if (E_total-E_R-E_ATP)!=0 else np.nan]
        E_dict['Dissipation Percent'] = E_dict.get('Dissipation Percent', []) + [(E_R/-E_ATP)*100 if E_ATP!=0 else np.nan]
        E_dict['Thermodynamic efficiency'] = E_dict.get('Thermodynamic efficiency', []) + [(1-E_R/-E_ATP)*100 if E_ATP!=0 else np.nan]
        E_dict['Chemical Energy'] = E_dict.get('Chemical Energy', []) + [E_Nai+E_Nao+E_Ki+E_Ko+E_S]
        E_dict['Electrical Energy'] = E_dict.get('Electrical Energy', []) + [E_Vm]
        E_dict['Chemical conversion efficiency'] = E_dict.get('Chemical conversion efficiency', []) + [(E_Nai+E_Nao+E_Ki+E_Ko)/-E_ATP*100 if E_ATP!=0 else np.nan]
        E_dict['Electrical conversion efficiency'] = E_dict.get('Electrical conversion efficiency', []) + [E_Vm/-E_ATP*100 if E_ATP!=0 else np.nan]
        E_dict['Chemical-Electrical ratio'] = E_dict.get('Chemical-Electrical ratio', []) + [ (E_Nai+E_Nao+E_Ki+E_Ko)/E_Vm if E_Vm!=0 else np.nan]

    # save the results to a summary csv file, prepend the pH value to each column
    df_summary = pd.DataFrame(E_dict)
    sum_file=data_path / f'EA_{basefile}.csv'
    df_summary.to_csv(sum_file, index=False) 

def calc_delta_G(data_path, basefile):
    # files ending with _<number>.csv in data_path
    list_csv_files = [f for f in os.listdir(data_path) if f.startswith(basefile+'_') and f.split('_')[-1].split('.')[0].isdigit() and f.endswith('.csv')]
    # sort list_csv_files by the number after the last underscore
    list_csv_files.sort(key=lambda x: int(re.findall(r'_(\d+)\.', x)[0]))
    def delta_G_func(reactants, products, reaction_name='hydrolysis'):
        delta_G_list = []
        for filename in list_csv_files:
            result_csv=data_path / filename
            pdf=pd.read_csv(result_csv)
            mu_reactants = 0
            mu_products = 0
            for reactant, stoichiometry in reactants.items():
                mu_reactants += pdf[f'{reactant}'].values[0]*stoichiometry
            for product, stoichiometry in products.items():
                mu_products += pdf[f'{product}'].values[0]*stoichiometry
            delta_G = mu_products - mu_reactants
            delta_G_list.append(delta_G)
        return {reaction_name: delta_G_list}
    deltaG={}
    F=96485
    reactants={'mu_ATP':1}
    products={'mu_ADP':1,'mu_Pi':1,'mu_H':1}
    deltaG_ATP=delta_G_func(reactants, products, reaction_name='ATP_hydrolysis')
    deltaG.update(deltaG_ATP)
    reactants={'mu_ATP':1,'mu_Nai':3,'mu_Ko':2,'u_Vm':F}
    products={'mu_ADP':1,'mu_Pi':1,'mu_H':1,'mu_Nao':3,'mu_Ki':2}
    deltaG_NKA=delta_G_func(reactants, products, reaction_name='NKA_m85mV')
    deltaG.update(deltaG_NKA)
    reactants={'mu_ATP':1,'mu_Nai':3,'mu_Ko':2,'u_Vm':F*75/85}
    products={'mu_ADP':1,'mu_Pi':1,'mu_H':1,'mu_Nao':3,'mu_Ki':2}
    deltaG_NKA=delta_G_func(reactants, products, reaction_name='NKA_m75mV')
    deltaG.update(deltaG_NKA)
    reactants={'mu_ATP':1,'mu_Nai':3,'mu_Ko':2,'u_Vm':F*-20/85}
    products={'mu_ADP':1,'mu_Pi':1,'mu_H':1,'mu_Nao':3,'mu_Ki':2}
    deltaG_NKA=delta_G_func(reactants, products, reaction_name='NKA_20mV')
    deltaG.update(deltaG_NKA)

    reactants={'mu_Nai':3,'mu_Ko':2}
    products={'mu_Nao':3,'mu_Ki':2}
    deltaG_NaK=delta_G_func(reactants, products, reaction_name='NaK')
    deltaG.update(deltaG_NaK)
    reactants={'u_Vm':F}
    products={}
    deltaG_Vm=delta_G_func(reactants, products, reaction_name='Vm_m85mV')
    deltaG.update(deltaG_Vm)
    reactants={'u_Vm':F*75/85}
    products={}
    deltaG_Vm=delta_G_func(reactants, products, reaction_name='Vm_m75mV')
    deltaG.update(deltaG_Vm)
    reactants={'u_Vm':F*-20/85}
    products={}
    deltaG_Vm=delta_G_func(reactants, products, reaction_name='Vm_20mV')
    deltaG.update(deltaG_Vm)
    eta=(np.array(deltaG['NaK'])+np.array(deltaG['Vm_m85mV']))/deltaG['ATP_hydrolysis']*-100.0
    gamma=np.array(deltaG['NaK'])/np.array(deltaG['Vm_m85mV'])*100.0
    deltaG.update({'eta_m85mV':eta,'gamma_m85mV':gamma})
    eta=(np.array(deltaG['NaK'])+np.array(deltaG['Vm_m75mV']))/deltaG['ATP_hydrolysis']*-100.0
    gamma=np.array(deltaG['NaK'])/np.array(deltaG['Vm_m75mV'])*100.0
    deltaG.update({'eta_m75mV':eta,'gamma_m75mV':gamma})
    eta=(np.array(deltaG['NaK'])+np.array(deltaG['Vm_20mV']))/deltaG['ATP_hydrolysis']*-100.0
    gamma=np.array(deltaG['NaK'])/np.array(deltaG['Vm_20mV'])*100.0
    deltaG.update({'eta_20mV':eta,'gamma_20mV':gamma})
    csv_file_name=data_path / f'deltaG_efficiency_{basefile}.csv'
    pd.DataFrame(dict([(k,pd.Series(v)) for k,v in deltaG.items()])).to_csv(csv_file_name, index=False)