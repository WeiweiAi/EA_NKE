import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sim_edit_func import sedtask, assemble_output,sedtask_oneStep,dict_algorithm_cvode_timecourse,dict_algorithm_cvode_oneStep
from pathlib import Path
from exp_conditions import read_json,write_json

parent_path = Path(__file__).parent.parent / 'cad' / 'models'
simulation_path = Path(__file__).parent.parent / 'cad' / 'models' / 'simulation'

dict_algorithm_timecourse=dict_algorithm_cvode_timecourse()
dict_algorithm_oneStep=dict_algorithm_cvode_oneStep()

def get_conditions(changes):
    conditions={}
    for key, change in changes[0].items():
        conditions[key]={}
        conditions[key]['component'] = change['component']
        conditions[key]['name'] = change['name']
        conditions[key]['scale'] = 1
    return conditions

def edit_fig3a(model_name,outputs,params=None,dict_algorithm_oneStep=dict_algorithm_oneStep):
    model_id_base = 'fig3a'
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

def edit_fig3b(model_name,outputs,params=None,dict_algorithm_oneStep=dict_algorithm_oneStep):
    model_id_base = 'fig3b'
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

def edit_fig3c(model_name,outputs,params=None,dict_algorithm_oneStep=dict_algorithm_oneStep):
    model_id_base = 'fig3c'
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

def edit_fig5(model_name,outputs,params=None,dict_algorithm_oneStep=dict_algorithm_oneStep):
    model_id_base = 'fig5'
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

def edit_default(model_name,outputs,params=None,dict_algorithm_timecourse=dict_algorithm_timecourse):
    model_id_base = 'default'
    json_path = simulation_path / f'NKE_BG_Env_default.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    startTime, endTime, numSteps =0.05, 0.85, 800
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_timecourse,startTime, endTime, numSteps)
    return sedml_file

def edit_Nai(model_name,outputs,params=None,dict_algorithm_timecourse=dict_algorithm_timecourse):
    model_id_base = 'Nai'
    json_path = simulation_path / f'NKE_BG_Env_Nai.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    startTime, endTime, numSteps =0.05, 6.25, 6200
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_timecourse,startTime, endTime, numSteps)
    return sedml_file

def edit_Ko(model_name,outputs,params=None,dict_algorithm_timecourse=dict_algorithm_timecourse):
    model_id_base = 'Ko'
    json_path = simulation_path / f'NKE_BG_Env_Ko.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    startTime, endTime, numSteps =0.05, 6.25, 6200
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_timecourse,startTime, endTime, numSteps)
    return sedml_file

def edit_ATP(model_name,outputs,params=None,dict_algorithm_timecourse=dict_algorithm_timecourse):
    model_id_base = 'ATP'
    json_path = simulation_path / f'NKE_BG_Env_ATP.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    startTime, endTime, numSteps =0.05, 6.25, 6200
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_timecourse,startTime, endTime, numSteps)
    return sedml_file

def edit_ADP(model_name,outputs,params=None,dict_algorithm_timecourse=dict_algorithm_timecourse):
    model_id_base = 'ADP'
    json_path = simulation_path / f'NKE_BG_Env_ADP.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    startTime, endTime, numSteps =0.05, 6.25, 6200
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_timecourse,startTime, endTime, numSteps)
    return sedml_file

def edit_Pi(model_name,outputs,params=None,dict_algorithm_timecourse=dict_algorithm_timecourse):
    model_id_base = 'Pi'
    json_path = simulation_path / f'NKE_BG_Env_Pi.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    startTime, endTime, numSteps =0.05, 6.25, 6200
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_timecourse,startTime, endTime, numSteps)
    return sedml_file

def edit_pH(model_name,outputs,params=None,dict_algorithm_timecourse=dict_algorithm_timecourse):
    model_id_base = 'pH'
    json_path = simulation_path / f'NKE_BG_Env_pH.json'
    changes=read_json(json_path)
    conditions=get_conditions(changes)
    outputs.update(conditions)
    startTime, endTime, numSteps =0.05, 6.25, 6200
    if params is not None:
        for change in changes:
            change.update(params)
    sedml_file=sedtask(parent_path,model_name, model_id_base,changes,outputs,dict_algorithm_timecourse,startTime, endTime, numSteps)
    return sedml_file

def edit_15state_fixedV():
    component_name='NKE_BG_15_state'
    # r1 to r15
    reaction_list=['r1','r2','r3','r4','r5','r6','r7','r8','r9','r10','r11','r12','r13','r14','r15']
    # '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','Nai','Nao','Ki','Ko','ATP','ADP','Pi'
    storage_list=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','Nai','Nao','Ki','Ko','H','ATP','ADP','Pi']
    electrical_storage_list=['Vm']
    time='t'
    outputs=assemble_output(component_name,reaction_list,storage_list,electrical_storage_list,time)
    model_name='NKE_BG_15_state_fixedV'
    NKE_BG_15_state_sedmls={}
    NKE_BG_15_state_sedmls['fig3a']=edit_fig3a(model_name,outputs)
    NKE_BG_15_state_sedmls['fig3b']=edit_fig3b(model_name,outputs)
    NKE_BG_15_state_sedmls['fig3c']=edit_fig3c(model_name,outputs)
    NKE_BG_15_state_sedmls['fig5']=edit_fig5(model_name,outputs)
    sedml_jsonfile =model_name + '_sedmls.json'
    write_json(simulation_path / sedml_jsonfile, NKE_BG_15_state_sedmls)

def edit_15state():
    component_name='NKE_BG_15_state'
    # r1 to r15
    reaction_list=['r1','r2','r3','r4','r5','r6','r7','r8','r9','r10','r11','r12','r13','r14','r15']
    # '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','Nai','Nao','Ki','Ko','ATP','ADP','Pi'
    storage_list=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','Nai','Nao','Ki','Ko','H','ATP','ADP','Pi']
    electrical_storage_list=['Vm']
    time='t'
    outputs=assemble_output(component_name,reaction_list,storage_list,electrical_storage_list,time)

    NKE_BG_15_state_sedmls={}
    model_name='NKE_BG_15_state'
    NKE_BG_15_state_sedmls['default']=edit_default(model_name,outputs)
    NKE_BG_15_state_sedmls['Nai']=edit_Nai(model_name,outputs)
    NKE_BG_15_state_sedmls['Ko']=edit_Ko(model_name,outputs)
    NKE_BG_15_state_sedmls['ATP']=edit_ATP(model_name,outputs)
    NKE_BG_15_state_sedmls['ADP']=edit_ADP(model_name,outputs)
    NKE_BG_15_state_sedmls['Pi']=edit_Pi(model_name,outputs)
    NKE_BG_15_state_sedmls['pH']=edit_pH(model_name,outputs)
    sedml_jsonfile =model_name + '_sedmls.json'
    write_json(simulation_path / sedml_jsonfile, NKE_BG_15_state_sedmls)

def edit_NKE_BG_6_state_ATPNaZK_fit_fixedV():
    component_name='NKE_BG_6_state_ATPNaZK'
    reaction_list=['r1','r5','r6','r8','r11','r13']
    storage_list=['3','6','7','11','13','14','Nai','Nao','Ki','Ko','H','ATP','ADP','Pi']
    electrical_storage_list=['Vm']
    time='t'
    outputs=assemble_output(component_name,reaction_list,storage_list,electrical_storage_list,time)
    model_name='NKE_BG_6_state_ATPNaZK_fit_fixedV'
    params={'K_6':{'component':'NKE_BG_param','name':'K_6','newValue':'3.3542462204899834'},
            'K_13':{'component':'NKE_BG_param','name':'K_13','newValue':'0.012064412240299305'},
            'kappa_r1':{'component':'NKE_BG_param','name':'kappa_r1','newValue':'1416.6810796350792'},
            'kappa_r5':{'component':'NKE_BG_param','name':'kappa_r5','newValue':'58916.26284656346'},
            'kappa_r6':{'component':'NKE_BG_param','name':'kappa_r6','newValue':'778.9637159873732'},
            'kappa_r8':{'component':'NKE_BG_param','name':'kappa_r8','newValue':'651.3921716357278'},
            'kappa_r11':{'component':'NKE_BG_param','name':'kappa_r11','newValue':'34493.73551226611'},
            'kappa_r13':{'component':'NKE_BG_param','name':'kappa_r13','newValue':'5591.590510363911'}}
    NKE_BG_6_state_ATPNaZK_sedmls={}
    NKE_BG_6_state_ATPNaZK_sedmls['fig3a']=edit_fig3a(model_name,outputs,params)
    NKE_BG_6_state_ATPNaZK_sedmls['fig3b']=edit_fig3b(model_name,outputs,params)
    NKE_BG_6_state_ATPNaZK_sedmls['fig3c']=edit_fig3c(model_name,outputs,params)
    NKE_BG_6_state_ATPNaZK_sedmls['fig5']=edit_fig5(model_name,outputs,params)
    sedml_jsonfile =model_name + '_sedmls.json'
    write_json(simulation_path / sedml_jsonfile, NKE_BG_6_state_ATPNaZK_sedmls)

def edit_NKE_BG_6_state_ATPNaZK_fit():
    component_name='NKE_BG_6_state_ATPNaZK'
    reaction_list=['r1','r5','r6','r8','r11','r13']
    storage_list=['3','6','7','11','13','14','Nai','Nao','Ki','Ko','H','ATP','ADP','Pi']
    electrical_storage_list=['Vm']
    time='t'
    outputs=assemble_output(component_name,reaction_list,storage_list,electrical_storage_list,time)
    params={'K_6':{'component':'NKE_BG_param','name':'K_6','newValue':'3.3542462204899834'},
            'K_13':{'component':'NKE_BG_param','name':'K_13','newValue':'0.012064412240299305'},
            'kappa_r1':{'component':'NKE_BG_param','name':'kappa_r1','newValue':'1416.6810796350792'},
            'kappa_r5':{'component':'NKE_BG_param','name':'kappa_r5','newValue':'58916.26284656346'},
            'kappa_r6':{'component':'NKE_BG_param','name':'kappa_r6','newValue':'778.9637159873732'},
            'kappa_r8':{'component':'NKE_BG_param','name':'kappa_r8','newValue':'651.3921716357278'},
            'kappa_r11':{'component':'NKE_BG_param','name':'kappa_r11','newValue':'34493.73551226611'},
            'kappa_r13':{'component':'NKE_BG_param','name':'kappa_r13','newValue':'5591.590510363911'}}
    NKE_BG_6_state_ATPNaZK_sedmls={}
    model_name='NKE_BG_6_state_ATPNaZK_fit'
    NKE_BG_6_state_ATPNaZK_sedmls['default']=edit_default(model_name,outputs,params)
    NKE_BG_6_state_ATPNaZK_sedmls['Nai']=edit_Nai(model_name,outputs,params)
    NKE_BG_6_state_ATPNaZK_sedmls['Ko']=edit_Ko(model_name,outputs,params)
    NKE_BG_6_state_ATPNaZK_sedmls['ATP']=edit_ATP(model_name,outputs,params)
    NKE_BG_6_state_ATPNaZK_sedmls['ADP']=edit_ADP(model_name,outputs,params)
    NKE_BG_6_state_ATPNaZK_sedmls['Pi']=edit_Pi(model_name,outputs,params)
    NKE_BG_6_state_ATPNaZK_sedmls['pH']=edit_pH(model_name,outputs,params)
    sedml_jsonfile =model_name + '_sedmls.json'
    write_json(simulation_path / sedml_jsonfile, NKE_BG_6_state_ATPNaZK_sedmls)

def edit_NKE_Hill_ss_fixedV():
    component_name='NKE_BG_Env'
    reaction_list=[]
    storage_list=['Nai','Nao','Ki','Ko','H','ATP','ADP','Pi']
    electrical_storage_list=['Vm']
    outputs=assemble_output(component_name,reaction_list,storage_list,electrical_storage_list,time=None)
    outputs['v_NKE']={'component':component_name,'name':'v_NKE','scale':1}
    model_name='NKE_Hill_ss'
    component_name='NKE_BG_Env'
    params_jsonfile=parent_path/'pe_task_NKE_Hill_ss_ss.json'
    params=read_json(params_jsonfile)['best']
    # change the values in params to strings
    for key in params:
        params[key]['newValue']=str(params[key]['newValue'])
        params[key]['component']=component_name
    NKE_Hill_ss_sedmls={}
    NKE_Hill_ss_sedmls['fig3a']=edit_fig3a(model_name,outputs,params)
    NKE_Hill_ss_sedmls['fig3b']=edit_fig3b(model_name,outputs,params)
    NKE_Hill_ss_sedmls['fig3c']=edit_fig3c(model_name,outputs,params)
    NKE_Hill_ss_sedmls['fig5']=edit_fig5(model_name,outputs,params)
    sedml_jsonfile =model_name + '_sedmls.json'
    write_json(simulation_path / sedml_jsonfile, NKE_Hill_ss_sedmls)

if __name__ == "__main__":
    """
    edit_NKE_BG_6_state_ATPNaZK_fit_fixedV()
    edit_NKE_BG_6_state_ATPNaZK_fit()
    edit_15state()
    edit_15state_fixedV()
    """
    edit_NKE_Hill_ss_fixedV()