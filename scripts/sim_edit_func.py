import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sedmlEditor.sedDict import create_dict_sedDocment, add_sedTask2dict
from sedmlEditor.sedEditor import create_sedDocment,write_sedml, validate_sedml, read_sedml
from pathlib import Path

parent_path = Path(__file__).parent.parent / 'cad' / 'models'

def assemble_output(component_name,reaction_list,storage_list,electrical_storage_list,time):
    outputs={}
    outputs[time]={'component':component_name,'name':time,'scale':1}
    for reaction in reaction_list:
        outputs['mu_'+reaction+'_0']={'component':component_name,'name':'mu_'+reaction+'_0','scale':1}
        outputs['mu_'+reaction+'_1']={'component':component_name,'name':'mu_'+reaction+'_1','scale':1}
        outputs['v_'+reaction]={'component':component_name,'name':'v_'+reaction,'scale':1}
        outputs['kappa_'+reaction]={'component':component_name,'name':'kappa_'+reaction,'scale':1}
    for storage in storage_list:
        outputs['mu_'+storage]={'component':component_name,'name':'mu_'+storage,'scale':1}
        outputs['v_'+storage]={'component':component_name,'name':'v_'+storage,'scale':1}
        outputs['K_'+storage]={'component':component_name,'name':'K_'+storage,'scale':1}
    for storage in electrical_storage_list:
        outputs['u_'+storage]={'component':component_name,'name':'u_'+storage,'scale':1}
        outputs['i_'+storage]={'component':component_name,'name':'i_'+storage,'scale':1}
    return outputs


def sedtask(parent_path,model_name, model_id_base,changes_dict,outputs,startTime, endTime, numSteps):
    # Convert the model to CellML 2.0 if needed
    dict_sedDocument=create_dict_sedDocment()
    # This is the sedml file (relative) path and name, assuming in the same folder with the CellML model file
    sedFilename = model_name+'_'+model_id_base+'_V2.sedml' 
    full_path = Path(parent_path / sedFilename).as_posix()
    
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
    simSetting={'type':'UniformTimeCourse','algorithm':dict_algorithm,'initialTime':0,'outputStartTime':startTime,'outputEndTime':endTime,'numberOfSteps':numSteps}
    # simSetting={'type':'OneStep','algorithm':dict_algorithm,'step':0.1}
    for i in range(len(changes_dict)):
        model_id_=model_id_base+'_'+str(i)
        # ********** The following is to create a dictionary for the sedml file **********        
        model_id = model_name+'_'+model_id_ # This is the model id in the sedml, could be different from the model file name        

        # ********** The following is to add the task information to the dictionary **********
        # This is the model file name, assuming in the same folder with the sedml file
        model_source = model_name + '.cellml' 
        # This is to modify the model parameters if needed
        changes=changes_dict[i] 
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
    return full_path

def sedtask_oneStep(parent_path, model_name, model_id_base,changes_dict,outputs_15state,stepSize):
    # Convert the model to CellML 2.0 if needed
    dict_sedDocument=create_dict_sedDocment()
    # This is the sedml file (relative) path and name, assuming in the same folder with the CellML model file
    sedFilename = model_name+'_'+model_id_base+'_V2.sedml' 
    full_path = Path(parent_path / sedFilename).as_posix()
    
    outputs=outputs_15state
    # The following is the simulation setting
    # This is to set the maximum step size for the simulation
    dict_algorithmParameter={'kisaoID':'KISAO:0000209', 'name':'rtol','value':'1e-07'} 
    dict_algorithmParameter1={'kisaoID':'KISAO:0000467', 'name':'max_step','value':'0.0001'} 
    dict_algorithmParameter2={'kisaoID':'KISAO:0000415', 'name':'max_step_number','value':'500000'} 
    # You can set more algorithm parameters if needed. You can refer to get_KISAO_parameters() in src/simulator.py file to get the parameters for the specific algorithm
    # Add the algorithm parameters to listOfAlgorithmParameters
    # You can choose one of the simulation algorithms specified by KISAO_ALGORITHMS in src/simulator.py file
    dict_algorithm={'kisaoID':'KISAO:0000019','name':'CVODE','listOfAlgorithmParameters':[dict_algorithmParameter,dict_algorithmParameter1,dict_algorithmParameter2]} 
    # This is the simulation setting
    # You can choose one of the following simulation types: 'UniformTimeCourse', 'OneStep'
    simSetting={'type':'OneStep','algorithm':dict_algorithm,'step':stepSize}
    # simSetting={'type':'OneStep','algorithm':dict_algorithm,'step':0.1}
    for i in range(len(changes_dict)):
        model_id_=model_id_base+'_'+str(i)
        # ********** The following is to create a dictionary for the sedml file **********        
        model_id = model_name+'_'+model_id_ # This is the model id in the sedml, could be different from the model file name        

        # ********** The following is to add the task information to the dictionary **********
        # This is the model file name, assuming in the same folder with the sedml file
        model_source = model_name + '.cellml' 
        # This is to modify the model parameters if needed
        changes=changes_dict[i] 
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
    return full_path