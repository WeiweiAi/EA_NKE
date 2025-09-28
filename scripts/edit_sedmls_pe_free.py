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

def edit_NKE_BG_6_state_ATPNaZK():
    file_path=parent_path
    model_name='NKE_BG_6_state_ATPNaZK_free'
    model_id_base='pulseV'
    json_path = simulation_path / 'NKE_BG_Env_default.json'
    changes_list=read_json(json_path)
    fitExperiments={}
    fid='fid_1'
    datafile='./simulation/report_task_NKE_BG_15_state_default_0.csv'
    observables=[['i_Vm',None,None,'NKE_BG_6_state_ATPNaZK','i_Vm',1]]
    experimentConditions=[]
    time={'column_name':'t','startIndex':0,'endIndex':None,'component':'NKE_BG_Env','name':'t'}  
    experimentData_files,time_map,observables_map,experimentalConditions_map=map_datafile(fid,datafile, observables,experimentConditions, time)
    
    fitting_type='timeCourse' # the type of the fit experiment, which could be 'steadyState', or 'timeCourse'
    if time_map is not None:
        fitExperiments['fit_1']={'type':fitting_type,'algorithm':dict_algorithm_timecourse,'experimentalConditions':experimentalConditions_map,'observables':observables_map,'time':time_map}
    else:
        fitExperiments['fit_1']={'type':fitting_type,'algorithm':dict_algorithm_timecourse,'experimentalConditions':experimentalConditions_map,'observables':observables_map}

    adjustables=[['NKE_BG_param','kappa_r1',1e-2,1e5,10787],
                 ['NKE_BG_param','kappa_r2',1e-3,1e3,15],
                 ['NKE_BG_param','kappa_r3',1e-2,1e3,2.3],
                 ['NKE_BG_param','kappa_r4',1e-2,1e6,172042],
                 ['NKE_BG_param','kappa_r5',1e-3,1e4,597],
                 ['NKE_BG_param','kappa_r6',1e-3,1e4,300],
                 ['NKE_BG_param','K_1',1e-4,1,0.0124],
                 ['NKE_BG_param','K_2',1e-2,1e4,92],
                 ['NKE_BG_param','K_3',10,1e5,2000],
                 ['NKE_BG_param','K_4',1e-2,1e4,100],
                 ['NKE_BG_param','K_5',1e-3,10,0.32],
                 ['NKE_BG_param','K_6',1e3,1e6,6e4]
                 ]    
    adjustableParameters=get_adjustableParameters(adjustables)    
    
    full_path = pe_task(file_path, model_name, model_id_base, changes_list, experimentData_files,adjustableParameters,fitExperiments,dict_algorithm_opt_)
    return full_path

def edit_NKE_BG_6_state_ATPNaZK_ss():
    file_path=parent_path
    model_name='NKE_BG_6_state_ATPNaZK_free_fixedV'
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
    adjustables=[['NKE_BG_param','kappa_r1',1e-2,1e5,10787],
                 ['NKE_BG_param','kappa_r2',1e-3,1e3,15],
                 ['NKE_BG_param','kappa_r3',1e-2,1e3,2.3],
                 ['NKE_BG_param','kappa_r4',1e-2,1e6,172042],
                 ['NKE_BG_param','kappa_r5',1e-3,1e4,597],
                 ['NKE_BG_param','kappa_r6',1e-3,1e4,300],
                 ['NKE_BG_param','K_1',1e-4,1,0.0124],
                 ['NKE_BG_param','K_2',1e-2,1e4,92],
                 ['NKE_BG_param','K_3',10,1e5,2000],
                 ['NKE_BG_param','K_4',1e-2,1e4,100],
                 ['NKE_BG_param','K_5',1e-3,10,0.32],
                 ['NKE_BG_param','K_6',1e3,1e6,6e4]
                 ]    
    adjustableParameters=get_adjustableParameters(adjustables)
    full_path = pe_task(file_path, model_name, model_id_base, changes_list, experimentData_files,adjustableParameters,fitExperiments,dict_algorithm_opt_)
    return full_path


def edit_NKE_BG_6_state_ATP_Na():
    file_path=parent_path
    model_name='NKE_BG_6_state_ATP_Na_free'
    model_id_base='pulseV'
    json_path = simulation_path / 'NKE_BG_Env_default.json'
    changes_list=read_json(json_path)
    fitExperiments={}
    fid='fid_1'
    datafile='./simulation/report_task_NKE_BG_15_state_default_0.csv'
    observables=[['i_Vm',None,None,'NKE_BG_6_state_ATP_Na','i_Vm',1]]
    experimentConditions=[]
    time={'column_name':'t','startIndex':0,'endIndex':None,'component':'NKE_BG_Env','name':'t'}  
    experimentData_files,time_map,observables_map,experimentalConditions_map=map_datafile(fid,datafile, observables,experimentConditions, time)
    
    fitting_type='timeCourse' # the type of the fit experiment, which could be 'steadyState', or 'timeCourse'
    if time_map is not None:
        fitExperiments['fit_1']={'type':fitting_type,'algorithm':dict_algorithm_timecourse,'experimentalConditions':experimentalConditions_map,'observables':observables_map,'time':time_map}
    else:
        fitExperiments['fit_1']={'type':fitting_type,'algorithm':dict_algorithm_timecourse,'experimentalConditions':experimentalConditions_map,'observables':observables_map}

    adjustables=[['NKE_BG_param','kappa_r1',1e-3,1e2,1],
                 ['NKE_BG_param','kappa_r2',1e3,1e7,1e5],
                 ['NKE_BG_param','kappa_r3',1e1,1e4,1000],
                 ['NKE_BG_param','kappa_r4',10,1e6,172042],
                 ['NKE_BG_param','kappa_r5',10,1e4,597],
                 ['NKE_BG_param','kappa_r6',10,1e4,300],
                 ['NKE_BG_param','K_1',1e-4,100,1],
                 ['NKE_BG_param','K_2',1e2,1e7,1e4],
                 ['NKE_BG_param','K_3',10,1e6,7000],
                 ['NKE_BG_param','K_4',1,1e4,400],
                 ['NKE_BG_param','K_5',1e-4,100,1],
                 ['NKE_BG_param','K_6',1e3,1e8,4e6]
                 ]    
    adjustableParameters=get_adjustableParameters(adjustables)    
    
    full_path = pe_task(file_path, model_name, model_id_base, changes_list, experimentData_files,adjustableParameters,fitExperiments,dict_algorithm_opt_)
    return full_path

def edit_NKE_BG_6_state_ATP_Na_ss():
    file_path=parent_path
    model_name='NKE_BG_6_state_ATP_Na_free_fixedV'
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
    adjustables=[['NKE_BG_param','kappa_r1',1e-3,1e2,1],
                 ['NKE_BG_param','kappa_r2',1e3,1e7,1e5],
                 ['NKE_BG_param','kappa_r3',1e1,1e4,1000],
                 ['NKE_BG_param','kappa_r4',10,1e6,172042],
                 ['NKE_BG_param','kappa_r5',10,1e4,597],
                 ['NKE_BG_param','kappa_r6',10,1e4,300],
                 ['NKE_BG_param','K_1',1e-4,100,1],
                 ['NKE_BG_param','K_2',1e2,1e7,1e4],
                 ['NKE_BG_param','K_3',10,1e6,7000],
                 ['NKE_BG_param','K_4',1,1e4,400],
                 ['NKE_BG_param','K_5',1e-4,100,1],
                 ['NKE_BG_param','K_6',1e3,1e8,4e6]
                 ]    
    adjustableParameters=get_adjustableParameters(adjustables)    
    
    full_path = pe_task(file_path, model_name, model_id_base, changes_list, experimentData_files,adjustableParameters,fitExperiments,dict_algorithm_opt_)
    return full_path

def edit_NKE_BG_6_state_ATPNa():
    file_path=parent_path
    model_name='NKE_BG_6_state_ATPNa_free'
    model_id_base='pulseV'
    json_path = simulation_path / 'NKE_BG_Env_default.json'
    changes_list=read_json(json_path)
    fitExperiments={}
    fid='fid_1'
    datafile='./simulation/report_task_NKE_BG_15_state_default_0.csv'
    observables=[['i_Vm',None,None,'NKE_BG_6_state_ATPNa','i_Vm',1]]
    experimentConditions=[]
    time={'column_name':'t','startIndex':0,'endIndex':None,'component':'NKE_BG_Env','name':'t'}  
    experimentData_files,time_map,observables_map,experimentalConditions_map=map_datafile(fid,datafile, observables,experimentConditions, time)
    
    fitting_type='timeCourse' # the type of the fit experiment, which could be 'steadyState', or 'timeCourse'
    if time_map is not None:
        fitExperiments['fit_1']={'type':fitting_type,'algorithm':dict_algorithm_timecourse,'experimentalConditions':experimentalConditions_map,'observables':observables_map,'time':time_map}
    else:
        fitExperiments['fit_1']={'type':fitting_type,'algorithm':dict_algorithm_timecourse,'experimentalConditions':experimentalConditions_map,'observables':observables_map}

    adjustables=[['NKE_BG_param','kappa_r1',1e-2,1e5,10787],
                 ['NKE_BG_param','kappa_r2',1e-3,1e3,15],
                 ['NKE_BG_param','kappa_r3',1e-2,1e3,2.3],
                 ['NKE_BG_param','kappa_r4',1e-2,1e6,172042],
                 ['NKE_BG_param','kappa_r5',1e-3,1e4,597],
                 ['NKE_BG_param','kappa_r6',1e-3,1e4,300],
                 ['NKE_BG_param','K_1',1e-4,1,0.0124],
                 ['NKE_BG_param','K_2',1e-2,1e4,92],
                 ['NKE_BG_param','K_3',10,1e5,2000],
                 ['NKE_BG_param','K_4',1e-2,1e4,100],
                 ['NKE_BG_param','K_5',1e-3,10,0.32],
                 ['NKE_BG_param','K_6',1e3,1e6,6e4]
                 ]    
    adjustableParameters=get_adjustableParameters(adjustables)    
    
    full_path = pe_task(file_path, model_name, model_id_base, changes_list, experimentData_files,adjustableParameters,fitExperiments,dict_algorithm_opt_)
    return full_path

def edit_NKE_BG_6_state_ATPNa_ss():
    file_path=parent_path
    model_name='NKE_BG_6_state_ATPNa_free_fixedV'
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
    adjustables=[['NKE_BG_param','kappa_r1',1e-2,1e5,10787],
                 ['NKE_BG_param','kappa_r2',1e-3,1e3,15],
                 ['NKE_BG_param','kappa_r3',1e-2,1e3,2.3],
                 ['NKE_BG_param','kappa_r4',1e-2,1e6,172042],
                 ['NKE_BG_param','kappa_r5',1e-3,1e4,597],
                 ['NKE_BG_param','kappa_r6',1e-3,1e4,300],
                 ['NKE_BG_param','K_1',1e-4,1,0.0124],
                 ['NKE_BG_param','K_2',1e-2,1e4,92],
                 ['NKE_BG_param','K_3',10,1e5,2000],
                 ['NKE_BG_param','K_4',1e-2,1e4,100],
                 ['NKE_BG_param','K_5',1e-3,10,0.32],
                 ['NKE_BG_param','K_6',1e3,1e6,6e4]
                 ]    
    adjustableParameters=get_adjustableParameters(adjustables)    
    
    full_path = pe_task(file_path, model_name, model_id_base, changes_list, experimentData_files,adjustableParameters,fitExperiments,dict_algorithm_opt_)
    return full_path

if __name__ == "__main__":
    
   NKE_BG_6_state_ATPNaZK_pe_pulseV=edit_NKE_BG_6_state_ATPNaZK()
   NKE_BG_6_state_ATP_Na_pe_pulseV=edit_NKE_BG_6_state_ATP_Na()
   NKE_BG_6_state_ATPNa_pe_pulseV=edit_NKE_BG_6_state_ATPNa()
   NKE_BG_6_state_ATPNaZK_pe_ss=edit_NKE_BG_6_state_ATPNaZK_ss()
   NKE_BG_6_state_ATPNa_pe_ss=edit_NKE_BG_6_state_ATPNa_ss()
   NKE_BG_6_state_ATP_Na_pe_ss=edit_NKE_BG_6_state_ATP_Na_ss()


