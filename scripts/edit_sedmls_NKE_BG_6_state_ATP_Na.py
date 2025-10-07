import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.edit_sedmls_NKE_BG_6_state_ATPNa import edit_NKE_BG_6_state_ATPNa, edit_NKE_BG_6_state_ATPNa_fixedV
from sim_edit_func import  assemble_output
from edit_sedmls import edit_default, edit_Nai, edit_Ko, edit_ATP, edit_ADP, edit_Pi, edit_pH, edit_fig3a, edit_fig3b, edit_fig3c, edit_fig5
from pathlib import Path
from exp_conditions import write_json,read_json

parent_path = Path(__file__).parent.parent / 'cad' / 'models'
simulation_path = Path(__file__).parent.parent / 'cad' / 'models' / 'simulation'


def edit_NKE_BG_6_state_ATP_Na():
    component_name='NKE_BG_6_state_ATP_Na'
    # r1 to r6
    reaction_list=['r1','r2','r3','r4','r5','r6']
    # '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','Nai','Nao','Ki','Ko','ATP','ADP','Pi'
    storage_list=['1','2','3','4','5','6','Nai','Nao','Ki','Ko','H','ATP','ADP','Pi']
    electrical_storage_list=['Vm']
    time='t'
    outputs=assemble_output(component_name,reaction_list,storage_list,electrical_storage_list,time)
    newparams=['pe_task_NKE_BG_6_state_ATP_Na_pulseV.json','pe_task_NKE_BG_6_state_ATP_Na_fixedV_ss.json']
    ids=['_time','_ss']
    for newparam in newparams:
        newparam_json=simulation_path/newparam
        params=read_json(newparam_json)['best']
        sedmls={}
        model_name='NKE_BG_6_state_ATP_Na'
        sedmls['default']=edit_default(model_name,outputs,'default'+ids[newparams.index(newparam)],params)
        sedmls['Nai']=edit_Nai(model_name,outputs,'Nai'+ids[newparams.index(newparam)],params)
        sedmls['Ko']=edit_Ko(model_name,outputs,'Ko'+ids[newparams.index(newparam)],params)
        sedmls['ATP']=edit_ATP(model_name,outputs,'ATP'+ids[newparams.index(newparam)],params)
        sedmls['ADP']=edit_ADP(model_name,outputs,'ADP'+ids[newparams.index(newparam)],params)
        sedmls['Pi']=edit_Pi(model_name,outputs,'Pi'+ids[newparams.index(newparam)],params)
        sedmls['pH']=edit_pH(model_name,outputs,'pH'+ids[newparams.index(newparam)],params)
        sedml_jsonfile =model_name + ids[newparams.index(newparam)] + '_sedmls.json'
        write_json(simulation_path / sedml_jsonfile, sedmls)   

def edit_NKE_BG_6_state_ATP_Na_fixedV():
    component_name='NKE_BG_6_state_ATP_Na'
    # r1 to r6
    reaction_list=['r1','r2','r3','r4','r5','r6']
    # '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','Nai','Nao','Ki','Ko','ATP','ADP','Pi'
    storage_list=['1','2','3','4','5','6','Nai','Nao','Ki','Ko','H','ATP','ADP','Pi']
    electrical_storage_list=['Vm']
    time='t'
    outputs=assemble_output(component_name,reaction_list,storage_list,electrical_storage_list,time)
    newparams=['pe_task_NKE_BG_6_state_ATP_Na_pulseV.json','pe_task_NKE_BG_6_state_ATP_Na_fixedV_ss.json']
    ids=['_time','_ss']
    for newparam in newparams:
        newparam_json=simulation_path/newparam
        params=read_json(newparam_json)['best']
        sedmls={}
        model_name='NKE_BG_6_state_ATP_Na_fixedV'
        sedmls['fig3a']=edit_fig3a(model_name,outputs,'fig3a'+ids[newparams.index(newparam)],params)
        sedmls['fig3b']=edit_fig3b(model_name,outputs,'fig3b'+ids[newparams.index(newparam)],params)
        sedmls['fig3c']=edit_fig3c(model_name,outputs,'fig3c'+ids[newparams.index(newparam)],params)
        sedmls['fig5']=edit_fig5(model_name,outputs,'fig5'+ids[newparams.index(newparam)],params)
        sedml_jsonfile =model_name + ids[newparams.index(newparam)] + '_sedmls.json'
        write_json(simulation_path / sedml_jsonfile, sedmls)
    
if __name__ == "__main__":

    edit_NKE_BG_6_state_ATP_Na()
    edit_NKE_BG_6_state_ATP_Na_fixedV()