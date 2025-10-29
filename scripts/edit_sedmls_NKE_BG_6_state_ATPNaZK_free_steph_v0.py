import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sim_edit_func import  assemble_output
from edit_sedmls import edit_default, edit_Nai, edit_Ko, edit_ATP, edit_ADP, edit_Pi, edit_pH, edit_fig3a, edit_fig3b, edit_fig3c, edit_fig5
from pathlib import Path
from exp_conditions import write_json,read_json

parent_path = Path(__file__).parent.parent / 'cad' / 'models'
simulation_path = Path(__file__).parent.parent / 'cad' / 'models' / 'simulation'


def edit_NKE_BG_6_state_ATPNaZK_fixedV():
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
    ids=['_ss_steph_v0']
    sedmls={}
    model_name='NKE_BG_6_state_ATPNaZK_free_fixedV'
    sedmls['fig3a']=edit_fig3a(model_name,outputs,'fig3a'+ids[0],params)
    sedmls['fig3b']=edit_fig3b(model_name,outputs,'fig3b'+ids[0],params)
    sedmls['fig3c']=edit_fig3c(model_name,outputs,'fig3c'+ids[0],params)
    sedmls['fig5']=edit_fig5(model_name,outputs,'fig5'+ids[0],params)
    sedml_jsonfile =model_name + ids[0] + '_sedmls.json'
    write_json(simulation_path / sedml_jsonfile, sedmls)

def edit_NKE_BG_6_state_ATPNaZK_fixedV_withSS():
    component_name='NKE_BG_6_state_ATPNaZK_ss'
    # r1 to r6
    reaction_list=[]
    # '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','Nai','Nao','Ki','Ko','ATP','ADP','Pi'
    storage_list=[]
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
    ids=['_ss_steph_v0']
    sedmls={}
    model_name='NKE_BG_6_state_ATPNaZK_free_fixedV_withSS'
    sedmls['fig3a']=edit_fig3a(model_name,outputs,'fig3a'+ids[0],params)
    sedmls['fig3b']=edit_fig3b(model_name,outputs,'fig3b'+ids[0],params)
    sedmls['fig3c']=edit_fig3c(model_name,outputs,'fig3c'+ids[0],params)
    sedmls['fig5']=edit_fig5(model_name,outputs,'fig5'+ids[0],params)
    sedml_jsonfile =model_name + ids[0] + '_sedmls.json'
    write_json(simulation_path / sedml_jsonfile, sedmls)

if __name__ == "__main__":

    #edit_NKE_BG_6_state_ATPNaZK()
    edit_NKE_BG_6_state_ATPNaZK_fixedV()
    edit_NKE_BG_6_state_ATPNaZK_fixedV_withSS()