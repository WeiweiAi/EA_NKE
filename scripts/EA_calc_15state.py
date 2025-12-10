from pathlib import Path
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from EA_calc import calc_EA,calc_EA_summary, calc_delta_G

data_path = Path(__file__).parent.parent / 'cad' / 'models' / 'simulation'
def NKE_BG_15_state_EA_calculation():
    # calculate the energy and activity of the bond graph model
    # 15 reactions r1-r15
    reaction_list=['r1','r2','r3','r4','r5','r6','r7','r8','r9','r10','r11','r12','r13','r14','r15']
    T_0=[0.6, 0.8, 1.0, 1.2]
    for T in T_0:
        ids='_T'+str(int(T*1000))+'ms'
        basefile=[f'report_task_NKE_BG_15_state_Nai'+ids,
                  f'report_task_NKE_BG_15_state_Ko'+ids,
                  f'report_task_NKE_BG_15_state_ATP'+ids,
                  f'report_task_NKE_BG_15_state_ADP'+ids,
                  f'report_task_NKE_BG_15_state_Pi'+ids,
                  f'report_task_NKE_BG_15_state_pH'+ids,
                  f'report_task_NKE_BG_15_state_default'+ids]
        for bf in basefile:
            storage_list=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','Nai','Nao','Ki','Ko','ATP','ADP','Pi','H']
            calc_EA(data_path, bf, reaction_list, storage_list)
            storage_list=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
            calc_EA_summary(data_path, bf, reaction_list, storage_list)

def NKE_Terkildsen_SS_EA_calculation():
    # 1 reaction r1
    reaction_list=['r1']

    T_0=[0.6, 0.8, 1.0, 1.2]
    for T in T_0:
        ids='_T'+str(int(T*1000))+'ms'
        basefile=[f'report_task_Terkildsen_NaK_kinetic_modular_V_Nai'+ids,
                    f'report_task_Terkildsen_NaK_kinetic_modular_V_Ko'+ids,
                    f'report_task_Terkildsen_NaK_kinetic_modular_V_ATP'+ids,
                    f'report_task_Terkildsen_NaK_kinetic_modular_V_ADP'+ids,
                    f'report_task_Terkildsen_NaK_kinetic_modular_V_Pi'+ids,
                    f'report_task_Terkildsen_NaK_kinetic_modular_V_pH'+ids,
                    f'report_task_Terkildsen_NaK_kinetic_modular_V_default'+ids]
        for bf in basefile:
            storage_list=['Nai','Nao','Ki','Ko','ATP','ADP','Pi','H']
            calc_EA(data_path, bf, reaction_list, storage_list)
            storage_list=[]
            calc_EA_summary(data_path, bf, reaction_list, storage_list)

def NKE_BG_15_state_deltaG_calculation():
    # calculate the energy and activity of the bond graph model
    T_0=[0.6]
    for T in T_0:
        ids='_T'+str(int(T*1000))+'ms'
        basefile=[f'report_task_NKE_BG_15_state_Nai'+ids,
                  f'report_task_NKE_BG_15_state_Ko'+ids,
                  f'report_task_NKE_BG_15_state_ATP'+ids,
                  f'report_task_NKE_BG_15_state_ADP'+ids,
                  f'report_task_NKE_BG_15_state_Pi'+ids,
                  f'report_task_NKE_BG_15_state_pH'+ids,
                  f'report_task_NKE_BG_15_state_default'+ids]
        for bf in basefile:
            calc_delta_G(data_path, bf)

if __name__ == "__main__":
    NKE_BG_15_state_EA_calculation()
    NKE_Terkildsen_SS_EA_calculation()
    NKE_BG_15_state_deltaG_calculation()