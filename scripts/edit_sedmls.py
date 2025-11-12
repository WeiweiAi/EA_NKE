import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sim_edit_func import sedtask, assemble_output,sedtask_oneStep,dict_algorithm_cvode_timecourse,dict_algorithm_cvode_oneStep,get_conditions
from pathlib import Path
from exp_conditions import read_json,write_json

parent_path = Path(__file__).parent.parent / 'cad' / 'models'
simulation_path = Path(__file__).parent.parent / 'cad' / 'models' / 'simulation'

dict_algorithm_timecourse=dict_algorithm_cvode_timecourse()
dict_algorithm_oneStep=dict_algorithm_cvode_oneStep()

def edit_fig2a1(model_name,outputs,model_id_base = 'fig2a1',params=None,dict_algorithm_oneStep=dict_algorithm_oneStep):
    
    json_path = simulation_path / f'fig2a_cond_1.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    stepSize=10
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask_oneStep(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_oneStep,stepSize)
    return sedml_file

def edit_fig2a2(model_name,outputs,model_id_base = 'fig2a2',params=None,dict_algorithm_oneStep=dict_algorithm_oneStep):

    json_path = simulation_path / f'fig2a_cond_2.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    stepSize=10
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask_oneStep(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_oneStep,stepSize)
    return sedml_file
def edit_fig2a3(model_name,outputs,model_id_base = 'fig2a3',params=None,dict_algorithm_oneStep=dict_algorithm_oneStep):

    json_path = simulation_path / f'fig2a_cond_3.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    stepSize=10
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask_oneStep(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_oneStep,stepSize)
    return sedml_file

def edit_fig2a4(model_name,outputs,model_id_base = 'fig2a4',params=None,dict_algorithm_oneStep=dict_algorithm_oneStep):

    json_path = simulation_path / f'fig2a_cond_4.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    stepSize=10
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask_oneStep(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_oneStep,stepSize)
    return sedml_file

def edit_fig2b1(model_name,outputs,model_id_base = 'fig2b1',params=None,dict_algorithm_oneStep=dict_algorithm_oneStep):

    json_path = simulation_path / f'fig2b_cond_1.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    stepSize=10
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask_oneStep(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_oneStep,stepSize)
    return sedml_file

def edit_fig2b2(model_name,outputs,model_id_base = 'fig2b2',params=None,dict_algorithm_oneStep=dict_algorithm_oneStep):
    json_path = simulation_path / f'fig2b_cond_2.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    stepSize=10
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask_oneStep(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_oneStep,stepSize)
    return sedml_file
def edit_fig2b3(model_name,outputs,model_id_base = 'fig2b3',params=None,dict_algorithm_oneStep=dict_algorithm_oneStep):

    json_path = simulation_path / f'fig2b_cond_3.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    stepSize=10
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask_oneStep(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_oneStep,stepSize)
    return sedml_file
def edit_fig3a(model_name,outputs,model_id_base = 'fig3a',params=None,dict_algorithm_oneStep=dict_algorithm_oneStep):

    json_path = simulation_path / f'fig3a_cond.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    stepSize=10
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask_oneStep(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_oneStep,stepSize)
    return sedml_file

def edit_fig3a_steady(model_name,outputs,model_id_base = 'fig3a_steady',params=None,dict_algorithm_oneStep=dict_algorithm_oneStep):

    json_path = simulation_path / f'Terkildsen_NaK_kinetic_Nai_cond.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    stepSize=10
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask_oneStep(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_oneStep,stepSize)
    return sedml_file

def edit_fig3b(model_name,outputs,model_id_base = 'fig3b',params=None,dict_algorithm_oneStep=dict_algorithm_oneStep):

    json_path = simulation_path / f'fig3b_cond.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    stepSize=10
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask_oneStep(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_oneStep,stepSize)
    return sedml_file

def edit_fig3b_steady(model_name,outputs,model_id_base = 'fig3b_steady',params=None,dict_algorithm_oneStep=dict_algorithm_oneStep):

    json_path = simulation_path / f'Terkildsen_NaK_kinetic_Ke_cond.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    stepSize=10
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask_oneStep(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_oneStep,stepSize)
    return sedml_file

def edit_fig3c(model_name,outputs,model_id_base = 'fig3c',params=None,dict_algorithm_oneStep=dict_algorithm_oneStep):
    json_path = simulation_path / f'fig3c_cond.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    stepSize=10
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask_oneStep(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_oneStep,stepSize)
    return sedml_file

def edit_fig3c_steady(model_name,outputs,model_id_base = 'fig3c_steady',params=None,dict_algorithm_oneStep=dict_algorithm_oneStep):
    json_path = simulation_path / f'Terkildsen_NaK_kinetic_ATP_cond.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    stepSize=10
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask_oneStep(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_oneStep,stepSize)
    return sedml_file

def edit_fig5(model_name,outputs,model_id_base = 'fig5',params=None,dict_algorithm_oneStep=dict_algorithm_oneStep):
    json_path = simulation_path / f'Terkildsen_NaK_kinetic_volt_cond.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    stepSize=10
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask_oneStep(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_oneStep,stepSize)
    return sedml_file

def edit_default(model_name,outputs,model_id_base = 'default',params=None,dict_algorithm_timecourse=dict_algorithm_timecourse,startTime=0.5, endTime=5.5, numSteps=5000):
    json_path = simulation_path / f'NKE_BG_Env_default.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_timecourse,startTime, endTime, numSteps)
    return sedml_file

def edit_Nai(model_name,outputs,model_id_base = 'Nai',params=None,dict_algorithm_timecourse=dict_algorithm_timecourse,startTime=0.5, endTime=5.5, numSteps=5000):
    json_path = simulation_path / f'NKE_BG_Env_Nai.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_timecourse,startTime, endTime, numSteps)
    return sedml_file

def edit_Ko(model_name,outputs,model_id_base = 'Ko',params=None,dict_algorithm_timecourse=dict_algorithm_timecourse,startTime=0.5, endTime=5.5, numSteps=5000):
    json_path = simulation_path / f'NKE_BG_Env_Ko.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_timecourse,startTime, endTime, numSteps)
    return sedml_file

def edit_ATP(model_name,outputs,model_id_base = 'ATP',params=None,dict_algorithm_timecourse=dict_algorithm_timecourse,startTime=0.5, endTime=5.5, numSteps=5000):
    json_path = simulation_path / f'NKE_BG_Env_ATP.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_timecourse,startTime, endTime, numSteps)
    return sedml_file

def edit_ADP(model_name,outputs,model_id_base = 'ADP',params=None,dict_algorithm_timecourse=dict_algorithm_timecourse,startTime=0.5, endTime=5.5, numSteps=5000):
    json_path = simulation_path / f'NKE_BG_Env_ADP.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_timecourse,startTime, endTime, numSteps)
    return sedml_file

def edit_Pi(model_name,outputs,model_id_base = 'Pi',params=None,dict_algorithm_timecourse=dict_algorithm_timecourse,startTime=0.5, endTime=5.5, numSteps=5000):
    json_path = simulation_path / f'NKE_BG_Env_Pi.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_timecourse,startTime, endTime, numSteps)
    return sedml_file

def edit_pH(model_name,outputs,model_id_base = 'pH',params=None,dict_algorithm_timecourse=dict_algorithm_timecourse,startTime=0.5, endTime=5.5, numSteps=5000):
    json_path = simulation_path / f'NKE_BG_Env_pH.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_timecourse,startTime, endTime, numSteps)
    return sedml_file
