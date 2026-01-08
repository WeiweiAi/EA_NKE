import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sim_edit_func import  assemble_output
from edit_sedmls import edit_fig3a_steady, edit_fig3b_steady, edit_fig3c_steady, edit_fig2a1, edit_fig2a2, edit_fig2a3, edit_fig2a4, edit_fig2b1, edit_fig2b2, edit_fig2b3, edit_fig3a, edit_fig3b, edit_fig3c,edit_default, edit_Nai, edit_Ko, edit_ATP, edit_ADP, edit_Pi, edit_pH
from pathlib import Path
from exp_conditions import write_json

parent_path = Path(__file__).parent.parent / 'cad' / 'models'
simulation_path = Path(__file__).parent.parent / 'cad' / 'models' / 'simulation'

def edit_NKE_BG_6_state_ATPNaZK_free_fixedV():
    component_name='NKE_BG_6_state_ATPNaZK'
    # r1 to r6
    reaction_list=['r1','r2','r3','r4','r5','r6']
    # '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','Nai','Nao','Ki','Ko','ATP','ADP','Pi'
    storage_list=['1','2','3','4','5','6','Nai','Nao','Ki','Ko','H','ATP','ADP','Pi']
    electrical_storage_list=['Vm']
    time='t'
    outputs=assemble_output(component_name,reaction_list,storage_list,electrical_storage_list,time)
    params={'K_1':{'component':'NKE_BG_param','name':'K_1','newValue':'0.01672750157200864'},
            'K_2':{'component':'NKE_BG_param','name':'K_2','newValue':'4477.021060951143'},
            'K_3':{'component':'NKE_BG_param','name':'K_3','newValue':'46639.870922646594'},
            'K_4':{'component':'NKE_BG_param','name':'K_4','newValue':'720.5754433721395'},
            'K_5':{'component':'NKE_BG_param','name':'K_5','newValue':'1.6068992551751866'},
            'K_6':{'component':'NKE_BG_param','name':'K_6','newValue':'30254.315059094864'},
            'kappa_r1':{'component':'NKE_BG_param','name':'kappa_r1','newValue':'2838.887577221678'},
            'kappa_r2':{'component':'NKE_BG_param','name':'kappa_r2','newValue':'51.10219437844171'},
            'kappa_r3':{'component':'NKE_BG_param','name':'kappa_r3','newValue':'469.3484263577967'},
            'kappa_r4':{'component':'NKE_BG_param','name':'kappa_r4','newValue':'619068.2941716437'},
            'kappa_r5':{'component':'NKE_BG_param','name':'kappa_r5','newValue':'35.86695382215395'},
            'kappa_r6':{'component':'NKE_BG_param','name':'kappa_r6','newValue':'868.3565212763533'}}
    sedmls={}
    model_name='NKE_BG_6_state_ATPNaZK_free_fixedV'
    sedmls['fig2a1']=edit_fig2a1(model_name,outputs,'fig2a1',params)
    sedmls['fig2a2']=edit_fig2a2(model_name,outputs,'fig2a2',params)
    sedmls['fig2a3']=edit_fig2a3(model_name,outputs,'fig2a3',params)
    sedmls['fig2a4']=edit_fig2a4(model_name,outputs,'fig2a4',params)
    sedmls['fig2b1']=edit_fig2b1(model_name,outputs,'fig2b1',params)
    sedmls['fig2b2']=edit_fig2b2(model_name,outputs,'fig2b2',params)
    sedmls['fig2b3']=edit_fig2b3(model_name,outputs,'fig2b3',params)
    sedmls['fig3a']=edit_fig3a(model_name,outputs,'fig3a',params)
    sedmls['fig3b']=edit_fig3b(model_name,outputs,'fig3b',params)
    sedmls['fig3c']=edit_fig3c(model_name,outputs,'fig3c',params)
    sedml_jsonfile =model_name  + '_sedmls.json'
    write_json(simulation_path / sedml_jsonfile, sedmls)

def edit_NKE_BG_6_state_ATPNaZK_free_fixedV_SS():
    component_name='NKE_BG_6_state_ATPNaZK_ss'
    # r1 to r6
    reaction_list=['r1']
    # '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','Nai','Nao','Ki','Ko','ATP','ADP','Pi'
    storage_list=['Nai','Nao','Ki','Ko','H','ATP','ADP','Pi']
    electrical_storage_list=['Vm']
    outputs=assemble_output(component_name,reaction_list,storage_list,electrical_storage_list,None)
    outputs.update({'v_NKE':{'component':'NKE_BG_6_state_ATPNaZK_ss','name':'v_NKE','scale':1}})
    params={'K_1':{'component':'NKE_BG_param','name':'K_1','newValue':'0.01672750157200864'},
            'K_2':{'component':'NKE_BG_param','name':'K_2','newValue':'4477.021060951143'},
            'K_3':{'component':'NKE_BG_param','name':'K_3','newValue':'46639.870922646594'},
            'K_4':{'component':'NKE_BG_param','name':'K_4','newValue':'720.5754433721395'},
            'K_5':{'component':'NKE_BG_param','name':'K_5','newValue':'1.6068992551751866'},
            'K_6':{'component':'NKE_BG_param','name':'K_6','newValue':'30254.315059094864'},
            'kappa_r1':{'component':'NKE_BG_param','name':'kappa_r1','newValue':'2838.887577221678'},
            'kappa_r2':{'component':'NKE_BG_param','name':'kappa_r2','newValue':'51.10219437844171'},
            'kappa_r3':{'component':'NKE_BG_param','name':'kappa_r3','newValue':'469.3484263577967'},
            'kappa_r4':{'component':'NKE_BG_param','name':'kappa_r4','newValue':'619068.2941716437'},
            'kappa_r5':{'component':'NKE_BG_param','name':'kappa_r5','newValue':'35.86695382215395'},
            'kappa_r6':{'component':'NKE_BG_param','name':'kappa_r6','newValue':'868.3565212763533'}}
    sedmls={}
    model_name='NKE_BG_6_state_ATPNaZK_free_fixedV_SS'
    sedmls['fig2a1']=edit_fig2a1(model_name,outputs,'fig2a1',params)
    sedmls['fig2a2']=edit_fig2a2(model_name,outputs,'fig2a2',params)
    sedmls['fig2a3']=edit_fig2a3(model_name,outputs,'fig2a3',params)
    sedmls['fig2a4']=edit_fig2a4(model_name,outputs,'fig2a4',params)
    sedmls['fig2b1']=edit_fig2b1(model_name,outputs,'fig2b1',params)
    sedmls['fig2b2']=edit_fig2b2(model_name,outputs,'fig2b2',params)
    sedmls['fig2b3']=edit_fig2b3(model_name,outputs,'fig2b3',params)
    sedmls['fig3a']=edit_fig3a_steady(model_name,outputs,'fig3a',params)
    sedmls['fig3b']=edit_fig3b_steady(model_name,outputs,'fig3b',params)
    sedmls['fig3c']=edit_fig3c_steady(model_name,outputs,'fig3c',params)
    sedml_jsonfile =model_name  + '_sedmls.json'
    write_json(simulation_path / sedml_jsonfile, sedmls)

def edit_NKE_BG_6_state_ATPNaZK_free():
    component_name='NKE_BG_6_state_ATPNaZK'
    # r1 to r6
    reaction_list=['r1','r2','r3','r4','r5','r6']
    # '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','Nai','Nao','Ki','Ko','ATP','ADP','Pi'
    storage_list=['1','2','3','4','5','6','Nai','Nao','Ki','Ko','H','ATP','ADP','Pi']
    electrical_storage_list=['Vm']
    time='t'
    outputs=assemble_output(component_name,reaction_list,storage_list,electrical_storage_list,time)
    params={'K_1':{'component':'NKE_BG_param','name':'K_1','newValue':'0.01672750157200864'},
            'K_2':{'component':'NKE_BG_param','name':'K_2','newValue':'4477.021060951143'},
            'K_3':{'component':'NKE_BG_param','name':'K_3','newValue':'46639.870922646594'},
            'K_4':{'component':'NKE_BG_param','name':'K_4','newValue':'720.5754433721395'},
            'K_5':{'component':'NKE_BG_param','name':'K_5','newValue':'1.6068992551751866'},
            'K_6':{'component':'NKE_BG_param','name':'K_6','newValue':'30254.315059094864'},
            'kappa_r1':{'component':'NKE_BG_param','name':'kappa_r1','newValue':'2838.887577221678'},
            'kappa_r2':{'component':'NKE_BG_param','name':'kappa_r2','newValue':'51.10219437844171'},
            'kappa_r3':{'component':'NKE_BG_param','name':'kappa_r3','newValue':'469.3484263577967'},
            'kappa_r4':{'component':'NKE_BG_param','name':'kappa_r4','newValue':'619068.2941716437'},
            'kappa_r5':{'component':'NKE_BG_param','name':'kappa_r5','newValue':'35.86695382215395'},
            'kappa_r6':{'component':'NKE_BG_param','name':'kappa_r6','newValue':'868.3565212763533'}}
    sedmls={}
    model_name='NKE_BG_6_state_ATPNaZK_free'
    T_0=[0.6, 0.8, 1.0, 1.2]
    for T in T_0:
        params={'T_0':{'component':'NKE_BG_Env','name':'T_0','newValue':str(T)},
        }
        startTime=T-0.2
        endTime=6*T-0.2  
        numSteps=int((endTime - startTime)*1000)
        ids='_T'+str(int(T*1000))+'ms'             
        sedmls[f'default'+ids]=edit_default(model_name,outputs,model_id_base=f'default'+ids,params=params,startTime=startTime,endTime=endTime,numSteps=numSteps)
        sedmls[f'Nai'+ids]=edit_Nai(model_name,outputs,model_id_base=f'Nai'+ids,params=params,startTime=startTime,endTime=endTime,numSteps=numSteps)
        sedmls[f'Ko'+ids]=edit_Ko(model_name,outputs,model_id_base=f'Ko'+ids,params=params,startTime=startTime,endTime=endTime,numSteps=numSteps)
        sedmls[f'ATP'+ids]=edit_ATP(model_name,outputs,model_id_base=f'ATP'+ids,params=params,startTime=startTime,endTime=endTime,numSteps=numSteps)
        sedmls[f'ADP'+ids]=edit_ADP(model_name,outputs,model_id_base=f'ADP'+ids,params=params,startTime=startTime,endTime=endTime,numSteps=numSteps)
        sedmls[f'Pi'+ids]=edit_Pi(model_name,outputs,model_id_base=f'Pi'+ids,params=params,startTime=startTime,endTime=endTime,numSteps=numSteps)
        sedmls[f'pH'+ids]=edit_pH(model_name,outputs,model_id_base=f'pH'+ids,params=params,startTime=startTime,endTime=endTime,numSteps=numSteps)
    sedml_jsonfile =model_name + '_sedmls.json'
    write_json(simulation_path / sedml_jsonfile, sedmls)

def edit_NKE_BG_6_state_ATPNaZK_free_SS():
    component_name='NKE_BG_6_state_ATPNaZK_ss'
    # r1 to r6
    reaction_list=['r1']
    # '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','Nai','Nao','Ki','Ko','ATP','ADP','Pi'
    storage_list=['Nai','Nao','Ki','Ko','H','ATP','ADP','Pi']
    electrical_storage_list=['Vm']
    time='t'
    outputs=assemble_output(component_name,reaction_list,storage_list,electrical_storage_list,time)
    outputs.update({'v_NKE':{'component':'NKE_BG_6_state_ATPNaZK_ss','name':'v_NKE','scale':1}})
    params={'K_1':{'component':'NKE_BG_param','name':'K_1','newValue':'0.01672750157200864'},
            'K_2':{'component':'NKE_BG_param','name':'K_2','newValue':'4477.021060951143'},
            'K_3':{'component':'NKE_BG_param','name':'K_3','newValue':'46639.870922646594'},
            'K_4':{'component':'NKE_BG_param','name':'K_4','newValue':'720.5754433721395'},
            'K_5':{'component':'NKE_BG_param','name':'K_5','newValue':'1.6068992551751866'},
            'K_6':{'component':'NKE_BG_param','name':'K_6','newValue':'30254.315059094864'},
            'kappa_r1':{'component':'NKE_BG_param','name':'kappa_r1','newValue':'2838.887577221678'},
            'kappa_r2':{'component':'NKE_BG_param','name':'kappa_r2','newValue':'51.10219437844171'},
            'kappa_r3':{'component':'NKE_BG_param','name':'kappa_r3','newValue':'469.3484263577967'},
            'kappa_r4':{'component':'NKE_BG_param','name':'kappa_r4','newValue':'619068.2941716437'},
            'kappa_r5':{'component':'NKE_BG_param','name':'kappa_r5','newValue':'35.86695382215395'},
            'kappa_r6':{'component':'NKE_BG_param','name':'kappa_r6','newValue':'868.3565212763533'}}
    sedmls={}
    model_name='NKE_BG_6_state_ATPNaZK_free_SS'
    T_0=[0.6, 0.8, 1.0, 1.2]
    for T in T_0:
        params={'T_0':{'component':'NKE_BG_Env','name':'T_0','newValue':str(T)},
        }
        startTime=T-0.2
        endTime=6*T-0.2  
        numSteps=int((endTime - startTime)*1000)
        ids='_T'+str(int(T*1000))+'ms'             
        sedmls[f'default'+ids]=edit_default(model_name,outputs,model_id_base=f'default'+ids,params=params,startTime=startTime,endTime=endTime,numSteps=numSteps)
        sedmls[f'Nai'+ids]=edit_Nai(model_name,outputs,model_id_base=f'Nai'+ids,params=params,startTime=startTime,endTime=endTime,numSteps=numSteps)
        sedmls[f'Ko'+ids]=edit_Ko(model_name,outputs,model_id_base=f'Ko'+ids,params=params,startTime=startTime,endTime=endTime,numSteps=numSteps)
        sedmls[f'ATP'+ids]=edit_ATP(model_name,outputs,model_id_base=f'ATP'+ids,params=params,startTime=startTime,endTime=endTime,numSteps=numSteps)
        sedmls[f'ADP'+ids]=edit_ADP(model_name,outputs,model_id_base=f'ADP'+ids,params=params,startTime=startTime,endTime=endTime,numSteps=numSteps)
        sedmls[f'Pi'+ids]=edit_Pi(model_name,outputs,model_id_base=f'Pi'+ids,params=params,startTime=startTime,endTime=endTime,numSteps=numSteps)
        sedmls[f'pH'+ids]=edit_pH(model_name,outputs,model_id_base=f'pH'+ids,params=params,startTime=startTime,endTime=endTime,numSteps=numSteps)
    sedml_jsonfile =model_name + '_sedmls.json'
    write_json(simulation_path / sedml_jsonfile, sedmls)

if __name__ == "__main__":

    edit_NKE_BG_6_state_ATPNaZK_free_fixedV()
    edit_NKE_BG_6_state_ATPNaZK_free_SS()
    edit_NKE_BG_6_state_ATPNaZK_free()
    edit_NKE_BG_6_state_ATPNaZK_free_fixedV_SS()