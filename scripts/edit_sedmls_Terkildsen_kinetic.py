import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sim_edit_func import  assemble_output
from edit_sedmls import edit_default, edit_Nai, edit_Ko, edit_ATP, edit_ADP, edit_Pi, edit_pH
from pathlib import Path
from exp_conditions import write_json

parent_path = Path(__file__).parent.parent / 'cad' / 'models'
simulation_path = Path(__file__).parent.parent / 'cad' / 'models' / 'simulation'


def edit_Terkildsen_NaK_kinetic():
    component_name='environment'
    # r1 to r15
    reaction_list=['r1']
    # '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','Nai','Nao','Ki','Ko','ATP','ADP','Pi'
    storage_list=['Nai','Nao','Ki','Ko','H','ATP','ADP','Pi']
    electrical_storage_list=['Vm']
    time='t'
    outputs=assemble_output(component_name,reaction_list,storage_list,electrical_storage_list,time)

    NKE_BG_15_state_sedmls={}
    model_name='Terkildsen_NaK_kinetic_modular_V'
    NKE_BG_15_state_sedmls['default']=edit_default(model_name,outputs)
    NKE_BG_15_state_sedmls['Nai']=edit_Nai(model_name,outputs)
    NKE_BG_15_state_sedmls['Ko']=edit_Ko(model_name,outputs)
    NKE_BG_15_state_sedmls['ATP']=edit_ATP(model_name,outputs)
    NKE_BG_15_state_sedmls['ADP']=edit_ADP(model_name,outputs)
    NKE_BG_15_state_sedmls['Pi']=edit_Pi(model_name,outputs)
    NKE_BG_15_state_sedmls['pH']=edit_pH(model_name,outputs)
    sedml_jsonfile =model_name + '_sedmls.json'
    write_json(simulation_path / sedml_jsonfile, NKE_BG_15_state_sedmls)

if __name__ == "__main__":

    edit_Terkildsen_NaK_kinetic()