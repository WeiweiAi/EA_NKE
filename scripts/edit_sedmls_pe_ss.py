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


def edit_NKE_BG_6_state_ATPNaZK_ss():
    file_path=parent_path
    model_name='NKE_BG_6_state_ATPNaZK_fixedV'
    model_id_base='ss_v2'
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
    obs=[['v_ss',None,None,'NKE_BG_6_state_ATPNaZK','v_r1',1]]
    exps=[['c_Nai',None,None,None,'NKE_BG_Env','c_Nai'],
          ['c_Nao',None,None,None,'NKE_BG_Env','c_Nao'],
          ['c_Ki',None,None,None,'NKE_BG_Env','c_Ki'],
          ['c_Ko',None,None,None,'NKE_BG_Env','c_Ko'],
          ['c_ATP',None,None,None,'NKE_BG_Env','c_ATP'],
          ['c_ADP',None,None,None,'NKE_BG_Env','c_ADP'],
          ['c_Pi',None,None,None,'NKE_BG_Env','c_Pi'],
          ['pH',None,None,None,'NKE_BG_Env','pH'],
          ['u_0_Vm',None,None,None,'NKE_BG_Env','u_0_Vm'],
          ['T',None,None,None,'NKE_BG_Env','T']
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
    adjustables=[['NKE_BG_param','kappa_r1',1e-4,1e6,10787],
                 ['NKE_BG_param','kappa_r2',1e-3,1e4,15],
                 ['NKE_BG_param','kappa_r3',1e-4,1e4,2.3],
                 ['NKE_BG_param','kappa_r4',1e-2,1e7,172042],
                 ['NKE_BG_param','kappa_r5',1e-3,1e5,597],
                 ['NKE_BG_param','kappa_r6',1e-3,1e5,300],
                 ['NKE_BG_param','K_1',1e-5,2,0.0124],
                 ['NKE_BG_param','K_4',1e-3,1e5,100]
                 ]    
    adjustableParameters=get_adjustableParameters(adjustables)
    full_path = pe_task(file_path, model_name, model_id_base, changes_list, experimentData_files,adjustableParameters,fitExperiments,dict_algorithm_opt_)
    return full_path

def edit_NKE_BG_4_state_ATPNaZK_ss():
    file_path=parent_path
    model_name='NKE_BG_4_state_ATPNaZK_fixedV'
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
    obs=[['v_ss',None,None,'NKE_BG_4_state_ATPNaZK','v_r1',1]]
    exps=[['c_Nai',None,None,None,'NKE_BG_Env','c_Nai'],
          ['c_Nao',None,None,None,'NKE_BG_Env','c_Nao'],
          ['c_Ki',None,None,None,'NKE_BG_Env','c_Ki'],
          ['c_Ko',None,None,None,'NKE_BG_Env','c_Ko'],
          ['c_ATP',None,None,None,'NKE_BG_Env','c_ATP'],
          ['c_ADP',None,None,None,'NKE_BG_Env','c_ADP'],
          ['c_Pi',None,None,None,'NKE_BG_Env','c_Pi'],
          ['pH',None,None,None,'NKE_BG_Env','pH'],
          ['u_0_Vm',None,None,None,'NKE_BG_Env','u_0_Vm'],
          ['T',None,None,None,'NKE_BG_Env','T']
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
    adjustables=[['NKE_BG_param','kappa_r1',1e-4,1e6,10787],
                 ['NKE_BG_param','kappa_r2',1e-4,1e4,2.3],
                 ['NKE_BG_param','kappa_r3',1e-2,1e7,172042],
                 ['NKE_BG_param','kappa_r4',1e-3,1e5,300],
                 ['NKE_BG_param','K_1',1e-5,10,0.0124],
                 ]    
    adjustableParameters=get_adjustableParameters(adjustables)
    full_path = pe_task(file_path, model_name, model_id_base, changes_list, experimentData_files,adjustableParameters,fitExperiments,dict_algorithm_opt_)
    return full_path

def edit_NKE_BG_4_state_ATPNaZK_ss_free():
    file_path=parent_path
    model_name='NKE_BG_4_state_ATPNaZK_free_fixedV'
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
    obs=[['v_ss',None,None,'NKE_BG_4_state_ATPNaZK','v_r1',1]]
    exps=[['c_Nai',None,None,None,'NKE_BG_Env','c_Nai'],
          ['c_Nao',None,None,None,'NKE_BG_Env','c_Nao'],
          ['c_Ki',None,None,None,'NKE_BG_Env','c_Ki'],
          ['c_Ko',None,None,None,'NKE_BG_Env','c_Ko'],
          ['c_ATP',None,None,None,'NKE_BG_Env','c_ATP'],
          ['c_ADP',None,None,None,'NKE_BG_Env','c_ADP'],
          ['c_Pi',None,None,None,'NKE_BG_Env','c_Pi'],
          ['pH',None,None,None,'NKE_BG_Env','pH'],
          ['u_0_Vm',None,None,None,'NKE_BG_Env','u_0_Vm'],
          ['T',None,None,None,'NKE_BG_Env','T']
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
    adjustables=[['NKE_BG_param','kappa_r1',1e-4,1e6,10787],
                 ['NKE_BG_param','kappa_r2',1e-4,1e4,2.3],
                 ['NKE_BG_param','kappa_r3',1e-2,1e7,172042],
                 ['NKE_BG_param','kappa_r4',1e-3,1e5,300],
                 ['NKE_BG_param','K_1',1e-4,1,0.0124],
                 ['NKE_BG_param','K_2',10,1e5,2000],
                 ['NKE_BG_param','K_3',1e-2,1e4,100],
                 ['NKE_BG_param','K_4',1e3,1e6,6e4]
                 ]    
    adjustableParameters=get_adjustableParameters(adjustables)
    full_path = pe_task(file_path, model_name, model_id_base, changes_list, experimentData_files,adjustableParameters,fitExperiments,dict_algorithm_opt_)
    return full_path

def edit_NKE_BG_4_state_ATPNaZK_SS():
    file_path=parent_path
    model_name='NKE_BG_4_state_ATPNaZK_fixedV_SS'
    model_id_base=''
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
    obs=[['v_ss',None,None,'NKE_BG_4_state_ATPNaZK_ss','v_NKE',1]]
    exps=[['c_Nai',None,None,None,'NKE_BG_Env','c_Nai'],
          ['c_Nao',None,None,None,'NKE_BG_Env','c_Nao'],
          ['c_Ki',None,None,None,'NKE_BG_Env','c_Ki'],
          ['c_Ko',None,None,None,'NKE_BG_Env','c_Ko'],
          ['c_ATP',None,None,None,'NKE_BG_Env','c_ATP'],
          ['c_ADP',None,None,None,'NKE_BG_Env','c_ADP'],
          ['c_Pi',None,None,None,'NKE_BG_Env','c_Pi'],
          ['pH',None,None,None,'NKE_BG_Env','pH'],
          ['u_0_Vm',None,None,None,'NKE_BG_Env','u_0_Vm'],
          ['T',None,None,None,'NKE_BG_Env','T']
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
    adjustables=[['NKE_BG_param','kappa_r1',1e-4,1e6,10787],
                 ['NKE_BG_param','kappa_r2',1e-4,1e4,2.3],
                 ['NKE_BG_param','kappa_r3',1e-2,1e7,172042],
                 ['NKE_BG_param','kappa_r4',1e-3,1e5,300],
                 ['NKE_BG_param','K_1',1e-5,10,0.0124],
                 ]    
    adjustableParameters=get_adjustableParameters(adjustables)
    full_path = pe_task(file_path, model_name, model_id_base, changes_list, experimentData_files,adjustableParameters,fitExperiments,dict_algorithm_opt_)
    return full_path

def edit_NKE_BG_4_state_ATPNaZK_SS_free():
    file_path=parent_path
    model_name='NKE_BG_4_state_ATPNaZK_free_fixedV_SS'
    model_id_base=''
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
    obs=[['v_ss',None,None,'NKE_BG_4_state_ATPNaZK_ss','v_NKE',1]]
    exps=[['c_Nai',None,None,None,'NKE_BG_Env','c_Nai'],
          ['c_Nao',None,None,None,'NKE_BG_Env','c_Nao'],
          ['c_Ki',None,None,None,'NKE_BG_Env','c_Ki'],
          ['c_Ko',None,None,None,'NKE_BG_Env','c_Ko'],
          ['c_ATP',None,None,None,'NKE_BG_Env','c_ATP'],
          ['c_ADP',None,None,None,'NKE_BG_Env','c_ADP'],
          ['c_Pi',None,None,None,'NKE_BG_Env','c_Pi'],
          ['pH',None,None,None,'NKE_BG_Env','pH'],
          ['u_0_Vm',None,None,None,'NKE_BG_Env','u_0_Vm'],
          ['T',None,None,None,'NKE_BG_Env','T']
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
    adjustables=[['NKE_BG_param','kappa_r1',1e-6,1e9,10787],
                 ['NKE_BG_param','kappa_r2',1e-6,1e9,2.3],
                 ['NKE_BG_param','kappa_r3',1e-6,1e9,172042],
                 ['NKE_BG_param','kappa_r4',1e-15,1e-5,1e-7],
                 ['NKE_BG_param','K_1',1e-6,1e9,0.0124],
                 ['NKE_BG_param','K_2',1e-6,1e9,2000],
                 ['NKE_BG_param','K_3',1e-6,1e9,100],
                 ['NKE_BG_param','K_4',1e-15,1e-5,1e-7]
                 ]    
    adjustableParameters=get_adjustableParameters(adjustables)
    full_path = pe_task(file_path, model_name, model_id_base, changes_list, experimentData_files,adjustableParameters,fitExperiments,dict_algorithm_opt_)
    return full_path
def edit_NKE_BG_4_state_ATPNaZK_SS_free_fit1():
    file_path=parent_path
    model_name='NKE_BG_4_state_ATPNaZK_free_fixedV_SS'
    model_id_base='fit_1'
    changes_list=[{}]
    fitExperiments={}
    experimentData_files={}
    fileId_observable='cond_Nai'
    data_observables_Nai='../data/Terkildsen_NaK_kinetic_Nai_cond.csv'
    obs=[['v_ss',None,None,'NKE_BG_4_state_ATPNaZK_ss','v_NKE',1]]
    exps=[['c_Nai',None,None,None,'NKE_BG_Env','c_Nai'],
          ['c_Nao',None,None,None,'NKE_BG_Env','c_Nao'],
          ['c_Ki',None,None,None,'NKE_BG_Env','c_Ki'],
          ['c_Ko',None,None,None,'NKE_BG_Env','c_Ko'],
          ['c_ATP',None,None,None,'NKE_BG_Env','c_ATP'],
          ['c_ADP',None,None,None,'NKE_BG_Env','c_ADP'],
          ['c_Pi',None,None,None,'NKE_BG_Env','c_Pi'],
          ['pH',None,None,None,'NKE_BG_Env','pH'],
          ['u_0_Vm',None,None,None,'NKE_BG_Env','u_0_Vm'],
          ['T',None,None,None,'NKE_BG_Env','T']
          ]     
    experimentData_files_1,time_map,observables_map_1,experimentalConditions_map_1=map_datafile(fileId_observable,data_observables_Nai, obs,exps)
    experimentData_files.update(experimentData_files_1)
    fitting_type='steadyState'
    fitExperiments['fit_1']={'type':fitting_type,'algorithm':dict_algorithm_oneStep,'experimentalConditions':experimentalConditions_map_1,'observables':observables_map_1} 
    fit_refs=['fit_1']
    adjustables=[['NKE_BG_param','kappa_r1',1e-6,1e9,10787],
                 ['NKE_BG_param','kappa_r2',1e-6,1e9,2.3],
                 ['NKE_BG_param','kappa_r3',1e-6,1e9,172042],
                 ['NKE_BG_param','kappa_r4',1e-15,1e-5,1e-7],
                 ['NKE_BG_param','K_1',1e-6,1e9,0.0124],
                 ['NKE_BG_param','K_2',1e-6,1e9,2000],
                 ['NKE_BG_param','K_3',1e-6,1e9,100],
                 ['NKE_BG_param','K_4',1e-15,1e-5,1e-7]
                 ]    
    adjustableParameters=get_adjustableParameters(adjustables)
    full_path = pe_task(file_path, model_name, model_id_base, changes_list, experimentData_files,adjustableParameters,fitExperiments,dict_algorithm_opt_)
    return full_path

def edit_NKE_BG_4_state_ATPNaZK_SS_free_fit2():
    file_path=parent_path
    model_name='NKE_BG_4_state_ATPNaZK_free_fixedV_SS'
    model_id_base='fit_2'
    changes_list=[{}]
    fitExperiments={}
    experimentData_files={}
    fileId_observable2='cond_Ke'
    data_observables_Ke='../data/Terkildsen_NaK_kinetic_Ke_cond.csv'
    obs=[['v_ss',None,None,'NKE_BG_4_state_ATPNaZK_ss','v_NKE',1]]
    exps=[['c_Nai',None,None,None,'NKE_BG_Env','c_Nai'],
          ['c_Nao',None,None,None,'NKE_BG_Env','c_Nao'],
          ['c_Ki',None,None,None,'NKE_BG_Env','c_Ki'],
          ['c_Ko',None,None,None,'NKE_BG_Env','c_Ko'],
          ['c_ATP',None,None,None,'NKE_BG_Env','c_ATP'],
          ['c_ADP',None,None,None,'NKE_BG_Env','c_ADP'],
          ['c_Pi',None,None,None,'NKE_BG_Env','c_Pi'],
          ['pH',None,None,None,'NKE_BG_Env','pH'],
          ['u_0_Vm',None,None,None,'NKE_BG_Env','u_0_Vm'],
          ['T',None,None,None,'NKE_BG_Env','T']
          ]     
    experimentData_files_2,time_map,observables_map_2,experimentalConditions_map_2=map_datafile(fileId_observable2,data_observables_Ke, obs,exps)
    experimentData_files.update(experimentData_files_2)
    fitting_type='steadyState'
    fitExperiments['fit_2']={'type':fitting_type,'algorithm':dict_algorithm_oneStep,'experimentalConditions':experimentalConditions_map_2,'observables':observables_map_2} 
    fit_refs=['fit_2']
    adjustables=[['NKE_BG_param','kappa_r1',1e-6,1e9,10787],
                 ['NKE_BG_param','kappa_r2',1e-6,1e9,2.3],
                 ['NKE_BG_param','kappa_r3',1e-6,1e9,172042],
                 ['NKE_BG_param','kappa_r4',1e-15,1e-5,1e-7],
                 ['NKE_BG_param','K_1',1e-6,1e9,0.0124],
                 ['NKE_BG_param','K_2',1e-6,1e9,2000],
                 ['NKE_BG_param','K_3',1e-6,1e9,100],
                 ['NKE_BG_param','K_4',1e-15,1e-5,1e-7]
                 ]    
    adjustableParameters=get_adjustableParameters(adjustables)
    full_path = pe_task(file_path, model_name, model_id_base, changes_list, experimentData_files,adjustableParameters,fitExperiments,dict_algorithm_opt_)
    return full_path

def edit_NKE_BG_4_state_ATPNaZK_SS_free_fit3():
    file_path=parent_path
    model_name='NKE_BG_4_state_ATPNaZK_free_fixedV_SS'
    model_id_base='fit_3'
    changes_list=[{}]
    fitExperiments={}
    experimentData_files={}
    fileId_observable3='cond_ATP'
    data_observables_ATP='../data/Terkildsen_NaK_kinetic_ATP_cond.csv'
    obs=[['v_ss',None,None,'NKE_BG_4_state_ATPNaZK_ss','v_NKE',1]]
    exps=[['c_Nai',None,None,None,'NKE_BG_Env','c_Nai'],
          ['c_Nao',None,None,None,'NKE_BG_Env','c_Nao'],
          ['c_Ki',None,None,None,'NKE_BG_Env','c_Ki'],
          ['c_Ko',None,None,None,'NKE_BG_Env','c_Ko'],
          ['c_ATP',None,None,None,'NKE_BG_Env','c_ATP'],
          ['c_ADP',None,None,None,'NKE_BG_Env','c_ADP'],
          ['c_Pi',None,None,None,'NKE_BG_Env','c_Pi'],
          ['pH',None,None,None,'NKE_BG_Env','pH'],
          ['u_0_Vm',None,None,None,'NKE_BG_Env','u_0_Vm'],
          ['T',None,None,None,'NKE_BG_Env','T']
          ]     
    experimentData_files_3,time_map,observables_map_3,experimentalConditions_map_3=map_datafile(fileId_observable3,data_observables_ATP, obs,exps)
    experimentData_files.update(experimentData_files_3)
    fitting_type='steadyState'
    fitExperiments['fit_3']={'type':fitting_type,'algorithm':dict_algorithm_oneStep,'experimentalConditions':experimentalConditions_map_3,'observables':observables_map_3} 
    
    fit_refs=['fit_3']
    adjustables=[['NKE_BG_param','kappa_r1',1e-6,1e9,10787],
                 ['NKE_BG_param','kappa_r2',1e-6,1e9,2.3],
                 ['NKE_BG_param','kappa_r3',1e-6,1e9,172042],
                 ['NKE_BG_param','kappa_r4',1e-15,1e-5,1e-7],
                 ['NKE_BG_param','K_1',1e-6,1e9,0.0124],
                 ['NKE_BG_param','K_2',1e-6,1e9,2000],
                 ['NKE_BG_param','K_3',1e-6,1e9,100],
                 ['NKE_BG_param','K_4',1e-15,1e-5,1e-7]
                 ]   
    adjustableParameters=get_adjustableParameters(adjustables)
    full_path = pe_task(file_path, model_name, model_id_base, changes_list, experimentData_files,adjustableParameters,fitExperiments,dict_algorithm_opt_)
    return full_path

def edit_NKE_BG_4_state_ATPNaZK_SS_free_fit4():
    file_path=parent_path
    model_name='NKE_BG_4_state_ATPNaZK_free_fixedV_SS'
    model_id_base='fit_4'
    changes_list=[{}]
    fitExperiments={}
    experimentData_files={}
    fileId_observable4='cond_volt'
    data_observables_volt='../data/Terkildsen_NaK_kinetic_volt_cond.csv'
    obs=[['v_ss',None,None,'NKE_BG_4_state_ATPNaZK_ss','v_NKE',1]]
    exps=[['c_Nai',None,None,None,'NKE_BG_Env','c_Nai'],
          ['c_Nao',None,None,None,'NKE_BG_Env','c_Nao'],
          ['c_Ki',None,None,None,'NKE_BG_Env','c_Ki'],
          ['c_Ko',None,None,None,'NKE_BG_Env','c_Ko'],
          ['c_ATP',None,None,None,'NKE_BG_Env','c_ATP'],
          ['c_ADP',None,None,None,'NKE_BG_Env','c_ADP'],
          ['c_Pi',None,None,None,'NKE_BG_Env','c_Pi'],
          ['pH',None,None,None,'NKE_BG_Env','pH'],
          ['u_0_Vm',None,None,None,'NKE_BG_Env','u_0_Vm'],
          ['T',None,None,None,'NKE_BG_Env','T']
          ]     
    experimentData_files_4,time_map,observables_map_4,experimentalConditions_map_4=map_datafile(fileId_observable4,data_observables_volt, obs,exps)
    experimentData_files.update(experimentData_files_4)
    fitting_type='steadyState'
    fitExperiments['fit_4']={'type':fitting_type,'algorithm':dict_algorithm_oneStep,'experimentalConditions':experimentalConditions_map_4,'observables':observables_map_4}
    fit_refs=['fit_4']
    adjustables=[['NKE_BG_param','kappa_r1',1e-6,1e9,10787],
                 ['NKE_BG_param','kappa_r2',1e-6,1e9,2.3],
                 ['NKE_BG_param','kappa_r3',1e-6,1e9,172042],
                 ['NKE_BG_param','kappa_r4',1e-15,1e-5,1e-7],
                 ['NKE_BG_param','K_1',1e-6,1e9,0.0124],
                 ['NKE_BG_param','K_2',1e-6,1e9,2000],
                 ['NKE_BG_param','K_3',1e-6,1e9,100],
                 ['NKE_BG_param','K_4',1e-15,1e-5,1e-7]
                 ]    
    adjustableParameters=get_adjustableParameters(adjustables)
    full_path = pe_task(file_path, model_name, model_id_base, changes_list, experimentData_files,adjustableParameters,fitExperiments,dict_algorithm_opt_)
    return full_path

def edit_NKE_BG_6_state_ATP_Na_ss():
    file_path=parent_path
    model_name='NKE_BG_6_state_ATP_Na_fixedV'
    model_id_base='ss_v2'
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
    obs=[['v_ss',None,None,'NKE_BG_6_state_ATP_Na','v_r1',1]]
    exps=[['c_Nai',None,None,None,'NKE_BG_Env','c_Nai'],
          ['c_Nao',None,None,None,'NKE_BG_Env','c_Nao'],
          ['c_Ki',None,None,None,'NKE_BG_Env','c_Ki'],
          ['c_Ko',None,None,None,'NKE_BG_Env','c_Ko'],
          ['c_ATP',None,None,None,'NKE_BG_Env','c_ATP'],
          ['c_ADP',None,None,None,'NKE_BG_Env','c_ADP'],
          ['c_Pi',None,None,None,'NKE_BG_Env','c_Pi'],
          ['pH',None,None,None,'NKE_BG_Env','pH'],
          ['u_0_Vm',None,None,None,'NKE_BG_Env','u_0_Vm'],
          ['T',None,None,None,'NKE_BG_Env','T']
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
    adjustables=[['NKE_BG_param','kappa_r1',1e-4,1e3,1],
                 ['NKE_BG_param','kappa_r2',1e2,1e8,1e5],
                 ['NKE_BG_param','kappa_r3',0.1,1e4,1000],
                 ['NKE_BG_param','kappa_r4',1,1e7,172042],
                 ['NKE_BG_param','kappa_r5',1,1e5,597],
                 ['NKE_BG_param','kappa_r6',1,1e5,300],
                 ['NKE_BG_param','K_1',1e-5,2,0.08]
                 ]    
    adjustableParameters=get_adjustableParameters(adjustables)    
    
    full_path = pe_task(file_path, model_name, model_id_base, changes_list, experimentData_files,adjustableParameters,fitExperiments,dict_algorithm_opt_)
    return full_path

def edit_NKE_BG_6_state_ATPNa_ss():
    file_path=parent_path
    model_name='NKE_BG_6_state_ATPNa_fixedV'
    model_id_base='ss_v2'
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
    obs=[['v_ss',None,None,'NKE_BG_6_state_ATPNa','v_r1',1]]
    exps=[['c_Nai',None,None,None,'NKE_BG_Env','c_Nai'],
          ['c_Nao',None,None,None,'NKE_BG_Env','c_Nao'],
          ['c_Ki',None,None,None,'NKE_BG_Env','c_Ki'],
          ['c_Ko',None,None,None,'NKE_BG_Env','c_Ko'],
          ['c_ATP',None,None,None,'NKE_BG_Env','c_ATP'],
          ['c_ADP',None,None,None,'NKE_BG_Env','c_ADP'],
          ['c_Pi',None,None,None,'NKE_BG_Env','c_Pi'],
          ['pH',None,None,None,'NKE_BG_Env','pH'],
          ['u_0_Vm',None,None,None,'NKE_BG_Env','u_0_Vm'],
          ['T',None,None,None,'NKE_BG_Env','T']
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
    adjustables=[['NKE_BG_param','kappa_r1',1e-4,1e6,10787],
                 ['NKE_BG_param','kappa_r2',1e-3,1e4,15],
                 ['NKE_BG_param','kappa_r3',1e-4,1e4,2.3],
                 ['NKE_BG_param','kappa_r4',1e-2,1e7,172042],
                 ['NKE_BG_param','kappa_r5',1e-3,1e5,597],
                 ['NKE_BG_param','kappa_r6',1e-3,1e5,300],
                 ['NKE_BG_param','K_1',1e-5,2,0.0124],
                 ['NKE_BG_param','K_4',1e-3,1e5,100]
                 ]    
    adjustableParameters=get_adjustableParameters(adjustables)    
    
    full_path = pe_task(file_path, model_name, model_id_base, changes_list, experimentData_files,adjustableParameters,fitExperiments,dict_algorithm_opt_)
    return full_path

if __name__ == "__main__":
    
  # NKE_BG_6_state_ATPNaZK_pe_ss=edit_NKE_BG_6_state_ATPNaZK_ss()
  # NKE_BG_6_state_ATPNa_pe_ss=edit_NKE_BG_6_state_ATPNa_ss()
  # NKE_BG_6_state_ATP_Na_pe_ss=edit_NKE_BG_6_state_ATP_Na_ss()
   NKE_BG_4_state_ATPNaZK_pe_ss=edit_NKE_BG_4_state_ATPNaZK_ss()
   NKE_BG_4_state_ATPNaZK_pe_ss_free=edit_NKE_BG_4_state_ATPNaZK_ss_free()
   NKE_BG_4_state_ATPNaZK_pe_SS=edit_NKE_BG_4_state_ATPNaZK_SS()
   NKE_BG_4_state_ATPNaZK_pe_SS_free=edit_NKE_BG_4_state_ATPNaZK_SS_free()
   NKE_BG_4_state_ATPNaZK_pe_SS_free_fit1=edit_NKE_BG_4_state_ATPNaZK_SS_free_fit1()
   NKE_BG_4_state_ATPNaZK_pe_SS_free_fit2=edit_NKE_BG_4_state_ATPNaZK_SS_free_fit2()
   NKE_BG_4_state_ATPNaZK_pe_SS_free_fit3=edit_NKE_BG_4_state_ATPNaZK_SS_free_fit3()
   NKE_BG_4_state_ATPNaZK_pe_SS_free_fit4=edit_NKE_BG_4_state_ATPNaZK_SS_free_fit4()   

