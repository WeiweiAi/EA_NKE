import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sedmlEditor.sedDict import create_dict_sedDocment, add_sedTask2dict
from sedmlEditor.sedEditor import create_sedDocment,write_sedml, validate_sedml, read_sedml
from pathlib import Path

parent_path = Path(__file__).parent.parent / 'cad' / 'models'

def sedtask():

    # Convert the model to CellML 2.0 if needed
    model_name='NKE_BG_15_state'
    model_ids_=['_pulse_cond_0']
    dict_sedDocument=create_dict_sedDocment()
    # This is the sedml file (relative) path and name, assuming in the same folder with the CellML model file
    sedFilename = model_name+model_ids_[0]+'_V2.sedml' 
    full_path = Path(parent_path / sedFilename).as_posix()

    c_Nai=15.0 #mM   4–16 mM https://doi.org/10.1161/01.CIR.0000016701.85760.97
    c_Nao=140.0 #mM  ∼140 mM https://doi.org/10.1016/S0008-6363(02)00656-9
    c_Ki=145 #mM 140-150 https://doi.org/10.1159/000446268
    c_Ko=5.4 #mM 3.5-5.0

    c_ATP=6.95 #mM
    c_ADP=0.035 #mM
    pH=7.4
    c_H=10**(-pH)*1000 #mM
    c_Pi=0.8 #mM

    for i in range(len(model_ids_)):
        model_id_=model_ids_[i]
        # ********** The following is to create a dictionary for the sedml file **********
       
        
        # model_name='Boron_acid_EA'
        model_id = model_name+model_id_ # This is the model id in the sedml, could be different from the model file name        

        # ********** The following is to add the task information to the dictionary **********

        # Note: the following is an example, you can modify it to add more tasks
        # Note: the valid sedml id should start with a letter, and only contain letters, numbers, and underscores
        # This is the model file name, assuming in the same folder with the sedml file
        model_source = model_name + '.cellml' 
        # This is to modify the model parameters if needed
        changes={'c_Nai':{'component':'NKE_BG_Env','name':'c_Nai','newValue':str(c_Nai)},
                 'c_Nao':{'component':'NKE_BG_Env','name':'c_Nao','newValue':str(c_Nao)},
                 'c_Ki':{'component':'NKE_BG_Env','name':'c_Ki','newValue':str(c_Ki)},
                 'c_Ko':{'component':'NKE_BG_Env','name':'c_Ko','newValue':str(c_Ko)},
                 'c_H':{'component':'NKE_BG_Env','name':'c_H','newValue':str(c_H)},
                 'c_ADP':{'component':'NKE_BG_Env','name':'c_ADP','newValue':str(c_ADP)},
                 'c_ATP':{'component':'NKE_BG_Env','name':'c_ATP','newValue':str(c_ATP)},
                 'c_Pi':{'component':'NKE_BG_Env','name':'c_Pi','newValue':str(c_Pi)}
                 } 
        # the format is {'id':{'component':str,'name':str,'newValue':str}}
        # Example: changes={'V_m':{'component':'main','name':'V_m','newValue':'-0.055'}

        # This is the output of the simulation, and the key is part of the output id
        # The value is a dictionary with the following keys: 'component', 'name', 'scale'
        # component is the component name in the CellML model where the output variable is defined
        # name is the variable name of the outputs
        # scale is the scaling factor for the output variable
        outputs={'t':{'component':'NKE_BG_15_state','name':'t','scale':1},
                 'mu_r1_0':{'component':'NKE_BG_15_state','name':'mu_r1_0','scale':1},
                 'mu_r1_1':{'component':'NKE_BG_15_state','name':'mu_r1_1','scale':1},
                 'mu_r2_0':{'component':'NKE_BG_15_state','name':'mu_r2_0','scale':1},
                 'mu_r2_1':{'component':'NKE_BG_15_state','name':'mu_r2_1','scale':1},
                 'mu_r3_0':{'component':'NKE_BG_15_state','name':'mu_r3_0','scale':1},
                 'mu_r3_1':{'component':'NKE_BG_15_state','name':'mu_r3_1','scale':1},
                 'mu_r4_0':{'component':'NKE_BG_15_state','name':'mu_r4_0','scale':1},
                 'mu_r4_1':{'component':'NKE_BG_15_state','name':'mu_r4_1','scale':1},
                 'mu_r5_0':{'component':'NKE_BG_15_state','name':'mu_r5_0','scale':1},
                 'mu_r5_1':{'component':'NKE_BG_15_state','name':'mu_r5_1','scale':1},
                 'mu_r6_0':{'component':'NKE_BG_15_state','name':'mu_r6_0','scale':1},
                 'mu_r6_1':{'component':'NKE_BG_15_state','name':'mu_r6_1','scale':1},
                 'mu_r7_0':{'component':'NKE_BG_15_state','name':'mu_r7_0','scale':1},
                 'mu_r7_1':{'component':'NKE_BG_15_state','name':'mu_r7_1','scale':1},
                 'mu_r8_0':{'component':'NKE_BG_15_state','name':'mu_r8_0','scale':1},
                 'mu_r8_1':{'component':'NKE_BG_15_state','name':'mu_r8_1','scale':1},
                 'mu_r9_0':{'component':'NKE_BG_15_state','name':'mu_r9_0','scale':1},
                 'mu_r9_1':{'component':'NKE_BG_15_state','name':'mu_r9_1','scale':1},
                 'mu_r10_0':{'component':'NKE_BG_15_state','name':'mu_r10_0','scale':1},
                 'mu_r10_1':{'component':'NKE_BG_15_state','name':'mu_r10_1','scale':1},
                 'mu_r11_0':{'component':'NKE_BG_15_state','name':'mu_r11_0','scale':1},
                 'mu_r11_1':{'component':'NKE_BG_15_state','name':'mu_r11_1','scale':1},
                 'mu_r12_0':{'component':'NKE_BG_15_state','name':'mu_r12_0','scale':1},
                 'mu_r12_1':{'component':'NKE_BG_15_state','name':'mu_r12_1','scale':1},
                 'mu_r13_0':{'component':'NKE_BG_15_state','name':'mu_r13_0','scale':1},
                 'mu_r13_1':{'component':'NKE_BG_15_state','name':'mu_r13_1','scale':1},
                 'mu_r14_0':{'component':'NKE_BG_15_state','name':'mu_r14_0','scale':1},
                 'mu_r14_1':{'component':'NKE_BG_15_state','name':'mu_r14_1','scale':1},
                 'mu_r15_0':{'component':'NKE_BG_15_state','name':'mu_r15_0','scale':1},
                 'mu_r15_1':{'component':'NKE_BG_15_state','name':'mu_r15_1','scale':1},
                 'v_r1':{'component':'NKE_BG_15_state','name':'v_r1','scale':1},
                 'v_r2':{'component':'NKE_BG_15_state','name':'v_r2','scale':1},
                 'v_r3':{'component':'NKE_BG_15_state','name':'v_r3','scale':1},
                 'v_r4':{'component':'NKE_BG_15_state','name':'v_r4','scale':1},
                 'v_r5':{'component':'NKE_BG_15_state','name':'v_r5','scale':1},
                 'v_r6':{'component':'NKE_BG_15_state','name':'v_r6','scale':1},
                 'v_r7':{'component':'NKE_BG_15_state','name':'v_r7','scale':1},
                 'v_r8':{'component':'NKE_BG_15_state','name':'v_r8','scale':1},
                 'v_r9':{'component':'NKE_BG_15_state','name':'v_r9','scale':1},
                 'v_r10':{'component':'NKE_BG_15_state','name':'v_r10','scale':1},
                 'v_r11':{'component':'NKE_BG_15_state','name':'v_r11','scale':1},
                 'v_r12':{'component':'NKE_BG_15_state','name':'v_r12','scale':1},
                 'v_r13':{'component':'NKE_BG_15_state','name':'v_r13','scale':1},
                 'v_r14':{'component':'NKE_BG_15_state','name':'v_r14','scale':1},
                 'v_r15':{'component':'NKE_BG_15_state','name':'v_r15','scale':1},
                 'mu_H':{'component':'NKE_BG_15_state','name':'mu_H','scale':1},
                 'mu_Ko':{'component':'NKE_BG_15_state','name':'mu_Ko','scale':1},
                 'mu_Ki':{'component':'NKE_BG_15_state','name':'mu_Ki','scale':1},
                 'mu_Nao':{'component':'NKE_BG_15_state','name':'mu_Nao','scale':1},
                 'mu_Nai':{'component':'NKE_BG_15_state','name':'mu_Nai','scale':1},
                 'mu_ATP':{'component':'NKE_BG_15_state','name':'mu_ATP','scale':1},
                 'mu_ADP':{'component':'NKE_BG_15_state','name':'mu_ADP','scale':1},
                 'mu_Pi':{'component':'NKE_BG_15_state','name':'mu_Pi','scale':1},
                 'v_H':{'component':'NKE_BG_15_state','name':'v_H','scale':1},
                 'v_Ko':{'component':'NKE_BG_15_state','name':'v_Ko','scale':1},
                 'v_Ki':{'component':'NKE_BG_15_state','name':'v_Ki','scale':1},
                 'v_Nao':{'component':'NKE_BG_15_state','name':'v_Nao','scale':1},
                 'v_Nai':{'component':'NKE_BG_15_state','name':'v_Nai','scale':1},
                 'v_ATP':{'component':'NKE_BG_15_state','name':'v_ATP','scale':1},
                 'v_ADP':{'component':'NKE_BG_15_state','name':'v_ADP','scale':1},
                 'v_Pi':{'component':'NKE_BG_15_state','name':'v_Pi','scale':1},
                 'mu_1':{'component':'NKE_BG_15_state','name':'mu_1','scale':1},
                 'mu_2':{'component':'NKE_BG_15_state','name':'mu_2','scale':1},
                 'mu_3':{'component':'NKE_BG_15_state','name':'mu_3','scale':1},
                 'mu_4':{'component':'NKE_BG_15_state','name':'mu_4','scale':1},
                 'mu_5':{'component':'NKE_BG_15_state','name':'mu_5','scale':1},
                 'mu_6':{'component':'NKE_BG_15_state','name':'mu_6','scale':1},
                 'mu_7':{'component':'NKE_BG_15_state','name':'mu_7','scale':1},
                 'mu_8':{'component':'NKE_BG_15_state','name':'mu_8','scale':1},
                 'mu_9':{'component':'NKE_BG_15_state','name':'mu_9','scale':1},
                 'mu_10':{'component':'NKE_BG_15_state','name':'mu_10','scale':1},
                 'mu_11':{'component':'NKE_BG_15_state','name':'mu_11','scale':1},
                 'mu_12':{'component':'NKE_BG_15_state','name':'mu_12','scale':1},
                 'mu_13':{'component':'NKE_BG_15_state','name':'mu_13','scale':1},
                 'mu_14':{'component':'NKE_BG_15_state','name':'mu_14','scale':1},
                 'mu_15':{'component':'NKE_BG_15_state','name':'mu_15','scale':1},
                 'v_1':{'component':'NKE_BG_15_state','name':'v_1','scale':1},
                 'v_2':{'component':'NKE_BG_15_state','name':'v_2','scale':1},
                 'v_3':{'component':'NKE_BG_15_state','name':'v_3','scale':1},
                 'v_4':{'component':'NKE_BG_15_state','name':'v_4','scale':1},
                 'v_5':{'component':'NKE_BG_15_state','name':'v_5','scale':1},
                 'v_6':{'component':'NKE_BG_15_state','name':'v_6','scale':1},
                 'v_7':{'component':'NKE_BG_15_state','name':'v_7','scale':1},
                 'v_8':{'component':'NKE_BG_15_state','name':'v_8','scale':1},
                 'v_9':{'component':'NKE_BG_15_state','name':'v_9','scale':1},
                 'v_10':{'component':'NKE_BG_15_state','name':'v_10','scale':1},
                 'v_11':{'component':'NKE_BG_15_state','name':'v_11','scale':1},
                 'v_12':{'component':'NKE_BG_15_state','name':'v_12','scale':1},
                 'v_13':{'component':'NKE_BG_15_state','name':'v_13','scale':1},
                 'v_14':{'component':'NKE_BG_15_state','name':'v_14','scale':1},
                 'v_15':{'component':'NKE_BG_15_state','name':'v_15','scale':1},
                 'u_Vm':{'component':'NKE_BG_15_state','name':'u_Vm','scale':1},
                 'i_Vm':{'component':'NKE_BG_15_state','name':'i_Vm','scale':1}, 
                 'q_0_Nai':{'component':'NKE_BG_15_state','name':'q_0_Nai','scale':1}, 
                 'q_0_Nao':{'component':'NKE_BG_15_state','name':'q_0_Nao','scale':1},
                 'q_0_Ki':{'component':'NKE_BG_15_state','name':'q_0_Ki','scale':1},
                 'q_0_Ko':{'component':'NKE_BG_15_state','name':'q_0_Ko','scale':1},
                 'q_0_H':{'component':'NKE_BG_15_state','name':'q_0_H','scale':1},
                 'q_0_ATP':{'component':'NKE_BG_15_state','name':'q_0_ATP','scale':1},
                 'q_0_ADP':{'component':'NKE_BG_15_state','name':'q_0_ADP','scale':1},
                 'q_0_Pi':{'component':'NKE_BG_15_state','name':'q_0_Pi','scale':1}
                 }
        # You can add more outputs if needed

        # The following is the simulation setting
        # This is to set the maximum step size for the simulation
        dict_algorithmParameter={'kisaoID':'KISAO:0000209', 'name':'rtol','value':'1e-7'} 
        dict_algorithmParameter1={'kisaoID':'KISAO:0000467', 'name':'max_step','value':'0.001'} 
        dict_algorithmParameter2={'kisaoID':'KISAO:0000415', 'name':'max_step_number','value':'5000'} 
        # You can set more algorithm parameters if needed. You can refer to get_KISAO_parameters() in src/simulator.py file to get the parameters for the specific algorithm
        # Add the algorithm parameters to listOfAlgorithmParameters
        # You can choose one of the simulation algorithms specified by KISAO_ALGORITHMS in src/simulator.py file
        dict_algorithm={'kisaoID':'KISAO:0000019','name':'CVODE','listOfAlgorithmParameters':[dict_algorithmParameter,dict_algorithmParameter1,dict_algorithmParameter2]} 
        # This is the simulation setting
        # You can choose one of the following simulation types: 'UniformTimeCourse', 'OneStep'
        simSetting={'type':'UniformTimeCourse','algorithm':dict_algorithm,'initialTime':0,'outputStartTime':0.05,'outputEndTime':6.1,'numberOfSteps':6050}
        # simSetting={'type':'OneStep','algorithm':dict_algorithm,'step':0.1}


        # The following is to add the task information to the dictionary
        add_sedTask2dict(dict_sedDocument, model_id, model_source,changes,simSetting,outputs)

        # You can repeat the above steps to add more tasks with DIFFERENT model names.

    # ********** The following is to create the sedml file, no need to modify **********
    try:
        doc=create_sedDocment(dict_sedDocument)
    except ValueError as err:
        print(err)
    write_sedml(doc,full_path)
    print(validate_sedml(full_path))
    doc=read_sedml(full_path) # Must read the sedml file again to avoid the error in the next step

sedtask()