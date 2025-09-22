from math import e
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sim_edit_func import pe_task, dict_algorithm_cvode_timecourse,dict_algorithm_cvode_oneStep,dict_algorithm_opt, map_datafile,get_adjustableParameters
from pathlib import Path
from exp_conditions import read_json
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sedCellMLpy'))

parent_path = Path(__file__).parent.parent / 'cad' / 'models'
simulation_path = Path(__file__).parent.parent / 'cad' / 'models' / 'simulation'
dict_algorithm_timecourse=dict_algorithm_cvode_timecourse()
dict_algorithm_oneStep=dict_algorithm_cvode_oneStep()
dict_algorithm_opt_=dict_algorithm_opt()

def edit_NKE_Hill_ss():
    file_path=parent_path
    model_name='NKE_Hill_ss'
    model_id_base='ss'
    changes_list=[{}]
    fitExperiments={}
    experimentData_files={}
    fileId_observable='cond_Nai'
    fileId_observable2='cond_Ke'
    fileId_observable3='cond_ATP'
    fileId_observable4='cond_volt'
    data_observables_Nai='../data/Terkildsen_NaK_kinetic_Nai_cond.csv'
    data_observables_Ke='../data/Terkildsen_NaK_kinetic_Ke_cond.csv'
    data_observables_ATP='../data/Terkildsen_NaK_kinetic_ATP_cond.csv'
    data_observables_volt='../data/Terkildsen_NaK_kinetic_volt_cond.csv'
    componentName='NKE_Hill_ss'
    obs=[['v_ss',None,None,componentName,'v_NKE',1]]
    exps=[['c_Nai',None,None,None,componentName,'c_Nai'],
          ['c_Nao',None,None,None,componentName,'c_Nao'],
          ['c_Ki',None,None,None,componentName,'c_Ki'],
          ['c_Ko',None,None,None,componentName,'c_Ko'],
          ['c_ATP',None,None,None,componentName,'c_ATP'],
          ['c_ADP',None,None,None,componentName,'c_ADP'],
          ['c_Pi',None,None,None,componentName,'c_Pi'],
          ['pH',None,None,None,componentName,'pH'],
          ['u_0_Vm',None,None,None,componentName,'u_0_Vm'],
          ['T',None,None,None,componentName,'T']
          ]     
    experimentData_files_1,time_map,observables_map_1,experimentalConditions_map_1=map_datafile(fileId_observable,data_observables_Nai, obs,exps)
    experimentData_files_2,time_map,observables_map_2,experimentalConditions_map_2=map_datafile(fileId_observable2,data_observables_Ke, obs,exps)
    experimentData_files_3,time_map,observables_map_3,experimentalConditions_map_3=map_datafile(fileId_observable3,data_observables_ATP, obs,exps)
    experimentData_files_4,time_map,observables_map_4,experimentalConditions_map_4=map_datafile(fileId_observable4,data_observables_volt, obs,exps)
    experimentData_files.update(experimentData_files_1)
    experimentData_files.update(experimentData_files_2)
    experimentData_files.update(experimentData_files_3)
    experimentData_files.update(experimentData_files_4)
    fitting_type='steadyState'
    fitExperiments['fit_1']={'type':fitting_type,'algorithm':dict_algorithm_oneStep,'experimentalConditions':experimentalConditions_map_1,'observables':observables_map_1} 
    fitExperiments['fit_2']={'type':fitting_type,'algorithm':dict_algorithm_oneStep,'experimentalConditions':experimentalConditions_map_2,'observables':observables_map_2} 
    fitExperiments['fit_3']={'type':fitting_type,'algorithm':dict_algorithm_oneStep,'experimentalConditions':experimentalConditions_map_3,'observables':observables_map_3} 
    fitExperiments['fit_4']={'type':fitting_type,'algorithm':dict_algorithm_oneStep,'experimentalConditions':experimentalConditions_map_4,'observables':observables_map_4}
    
    fit_refs=['fit_1','fit_2','fit_3','fit_4']
    adjustables=[[componentName,'k_m_NKE',1e-4,1e3,1],
                 [componentName,'K_Nai_NKE',1e-9,1,1e-6],
                 [componentName,'K_Nao_NKE',1,1e4,150],
                 [componentName,'K_Ki_NKE',1,1e4,2300],
                 [componentName,'K_Ko_NKE',1e-5,10,1]
                 ]    
    adjustableParameters=get_adjustableParameters(adjustables,fit_refs)    
    
    full_path = pe_task(file_path, model_name, model_id_base, changes_list, experimentData_files,adjustableParameters,fitExperiments,dict_algorithm_opt_)
    return full_path


if __name__ == "__main__":
    
    NKE_Hill_ss=edit_NKE_Hill_ss()


