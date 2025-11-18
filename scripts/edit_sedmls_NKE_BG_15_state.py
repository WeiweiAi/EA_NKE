import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sim_edit_func import  assemble_output
from edit_sedmls import  edit_fig2a1, edit_fig2a2, edit_fig2a3, edit_fig2a4, edit_fig2b1, edit_fig2b2, edit_fig2b3,edit_default, edit_Nai, edit_Ko, edit_ATP, edit_ADP, edit_Pi, edit_pH, edit_fig3a, edit_fig3b, edit_fig3c, edit_fig5
from pathlib import Path
from exp_conditions import write_json

parent_path = Path(__file__).parent.parent / 'cad' / 'models'
simulation_path = Path(__file__).parent.parent / 'cad' / 'models' / 'simulation'


def edit_15state():
    component_name='NKE_BG_15_state'
    # r1 to r15
    reaction_list=['r1','r2','r3','r4','r5','r6','r7','r8','r9','r10','r11','r12','r13','r14','r15']
    # '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','Nai','Nao','Ki','Ko','ATP','ADP','Pi'
    storage_list=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','Nai','Nao','Ki','Ko','H','ATP','ADP','Pi']
    electrical_storage_list=['Vm']
    time='t'
    outputs=assemble_output(component_name,reaction_list,storage_list,electrical_storage_list,time)
    T_0=[0.6, 0.8, 1.0, 1.2]
    NKE_BG_15_state_sedmls={}
    model_name='NKE_BG_15_state'
    for T in T_0:
        params={'T_0':{'component':'NKE_BG_Env','name':'T_0','newValue':str(T)},
        }
        startTime=T-0.2
        endTime=6*T-0.2  
        numSteps=int((endTime - startTime)*1000)
        ids='_T'+str(int(T*1000))+'ms'             
        NKE_BG_15_state_sedmls[f'default'+ids]=edit_default(model_name,outputs,model_id_base=f'default'+ids,params=params,startTime=startTime,endTime=endTime,numSteps=numSteps)
        NKE_BG_15_state_sedmls[f'Nai'+ids]=edit_Nai(model_name,outputs,model_id_base=f'Nai'+ids,params=params,startTime=startTime,endTime=endTime,numSteps=numSteps)
        NKE_BG_15_state_sedmls[f'Ko'+ids]=edit_Ko(model_name,outputs,model_id_base=f'Ko'+ids,params=params,startTime=startTime,endTime=endTime,numSteps=numSteps)
        NKE_BG_15_state_sedmls[f'ATP'+ids]=edit_ATP(model_name,outputs,model_id_base=f'ATP'+ids,params=params,startTime=startTime,endTime=endTime,numSteps=numSteps)
        NKE_BG_15_state_sedmls[f'ADP'+ids]=edit_ADP(model_name,outputs,model_id_base=f'ADP'+ids,params=params,startTime=startTime,endTime=endTime,numSteps=numSteps)
        NKE_BG_15_state_sedmls[f'Pi'+ids]=edit_Pi(model_name,outputs,model_id_base=f'Pi'+ids,params=params,startTime=startTime,endTime=endTime,numSteps=numSteps)
        NKE_BG_15_state_sedmls[f'pH'+ids]=edit_pH(model_name,outputs,model_id_base=f'pH'+ids,params=params,startTime=startTime,endTime=endTime,numSteps=numSteps)
    sedml_jsonfile =model_name + '_sedmls.json'
    write_json(simulation_path / sedml_jsonfile, NKE_BG_15_state_sedmls)

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
    sedmls={}
    sedmls['fig2a1']=edit_fig2a1(model_name,outputs,'fig2a1')
    sedmls['fig2a2']=edit_fig2a2(model_name,outputs,'fig2a2')
    sedmls['fig2a3']=edit_fig2a3(model_name,outputs,'fig2a3')
    sedmls['fig2a4']=edit_fig2a4(model_name,outputs,'fig2a4')
    sedmls['fig2b1']=edit_fig2b1(model_name,outputs,'fig2b1')
    sedmls['fig2b2']=edit_fig2b2(model_name,outputs,'fig2b2')
    sedmls['fig2b3']=edit_fig2b3(model_name,outputs,'fig2b3')
    sedmls['fig3a']=edit_fig3a(model_name,outputs,'fig3a')
    sedmls['fig3b']=edit_fig3b(model_name,outputs,'fig3b')
    sedmls['fig3c']=edit_fig3c(model_name,outputs,'fig3c')
    sedml_jsonfile =model_name + '_sedmls.json'
    write_json(simulation_path / sedml_jsonfile, sedmls)

if __name__ == "__main__":

    edit_15state()
    edit_15state_fixedV()