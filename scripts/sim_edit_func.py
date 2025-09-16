import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sedmlEditor.sedDict import create_dict_sedDocment, add_sedTask2dict,add_peTask2dict
from sedmlEditor.sedEditor import create_sedDocment,write_sedml, validate_sedml
from pathlib import Path

"""
Algorithms parameters refer to sedCellMLpy/sedCollector.py

"""

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

def dict_algorithm_cvode_timecourse():
    """"
    This function returns a dictionary for the CVODE algorithm used in the timecourse example

    Returns:
        dict_algorithm: dictionary for the CVODE algorithm
    
    """
    # You can set more algorithm parameters if needed. 
    dict_algorithmParameter={'kisaoID':'KISAO:0000209', 'name':'rtol','value':'1e-07'} 
    dict_algorithmParameter1={'kisaoID':'KISAO:0000467', 'name':'max_step','value':'0.001'} 
    dict_algorithmParameter2={'kisaoID':'KISAO:0000415', 'name':'max_step_number','value':'5000'}     
    # Add the algorithm parameters to listOfAlgorithmParameters
    dict_algorithm={'kisaoID':'KISAO:0000019','name':'CVODE','listOfAlgorithmParameters':[dict_algorithmParameter,dict_algorithmParameter1,dict_algorithmParameter2]} 
    return dict_algorithm

def dict_algorithm_cvode_oneStep():
    """"
    This function returns a dictionary for the CVODE algorithm used in the oneStep example

    Returns:
        dict_algorithm: dictionary for the CVODE algorithm
    
    """
    dict_algorithmParameter={'kisaoID':'KISAO:0000209', 'name':'rtol','value':'1e-07'} 
    dict_algorithmParameter1={'kisaoID':'KISAO:0000467', 'name':'max_step','value':'0.0001'} 
    dict_algorithmParameter2={'kisaoID':'KISAO:0000415', 'name':'max_step_number','value':'500000'} 
    # You can set more algorithm parameters if needed. 
    # Add the algorithm parameters to listOfAlgorithmParameters
    dict_algorithm={'kisaoID':'KISAO:0000019','name':'CVODE','listOfAlgorithmParameters':[dict_algorithmParameter,dict_algorithmParameter1,dict_algorithmParameter2]} 
    return dict_algorithm

def dict_algorithm_opt():

    # This is to set the tolerance for least square when using local optimization algorithm, default is 1e-8
    dict_algorithmParameter_opt={'kisaoID':'KISAO:0000597','name':'tol','value':'1e-6'} 
    # This is to set the maximum number of iterations when using local optimization algorithm, default is 1000
    dict_algorithmParameter_opt2={'kisaoID':'KISAO:0000486','name':'maxiter','value':'2000'}
    # This is to set optimization algorithm as genetic algorithm, and scipy.differential_evolution is used to implement the algorithm
    dict_algorithm_opt={'kisaoID':'KISAO:0000520','name':'evolutionary algorithm', 'listOfAlgorithmParameters':[dict_algorithmParameter_opt,dict_algorithmParameter_opt2]}
    return dict_algorithm_opt

def sedtask(file_path,model_name, model_id_base,changes_list,outputs,dict_algorithm,startTime, endTime, numSteps):

    """"
    This function writes a sedml file for the UniformTimeCourse simulation tasks of a cellml model
    Assume the sedml file is saved in the same folder with the cellml model
    Assume the outputs and simulation settings are the same for all tasks

    Parameters:
        file_path: :obj:`pathlib.Path`
            the path to the folder where the sedml file will be saved
        model_name: str
            the name of the cellml model file
        model_id_base: str
            the base name of the model id in the sedml file
        changes_list: list of dictionaries
            the list of changes to the model, each change is a dictionary and corresponds to one task
        outputs: dict
            the dictionary for the outputs of the model
        dict_algorithm: dict
            the dictionary for the algorithm used in the simulation
        startTime: float
            the start time of the simulation
        endTime: float
            the end time of the simulation
        numSteps: int
            the number of steps in the simulation

    Returns:
        sedFilename: the name of the sedml file

    side effects:
        a sedml file is created    
    """
    dict_sedDocument=create_dict_sedDocment()
    # This is the sedml file (relative) path and name, assuming in the same folder with the CellML model file
    sedFilename = model_name+'_'+model_id_base+'_V2.sedml' 
    full_path = Path(file_path / sedFilename).as_posix() 
    # This is the model file name, assuming in the same folder with the sedml file
    model_source = model_name + '.cellml'  
    # The following is the simulation setting
    simSetting={'type':'UniformTimeCourse','algorithm':dict_algorithm,'initialTime':0,'outputStartTime':startTime,'outputEndTime':endTime,'numberOfSteps':numSteps}
    for i in range(len(changes_list)):   
        model_id = model_name+'_'+model_id_base+'_'+str(i) # This is the model id in the sedml, could be different from the model file name        
        # This is to modify the model parameters if needed
        changes=changes_list[i] 
        # The following is to add the task information to the dictionary
        add_sedTask2dict(dict_sedDocument, model_id, model_source,changes,simSetting,outputs)
    try:
        doc=create_sedDocment(dict_sedDocument)
    except ValueError as err:
        print(err)
    write_sedml(doc,full_path)
    print(validate_sedml(full_path))
    # doc=read_sedml(full_path) # Must read the sedml file again to avoid the error in the next step
    return full_path

def sedtask_oneStep(file_path, model_name, model_id_base,changes_dict,outputs,dict_algorithm, stepSize):
    """
    This function writes a sedml file for the oneStep simulation tasks of a cellml model
    Assume the sedml file is saved in the same folder with the cellml model
    Assume the outputs and simulation settings are the same for all tasks

    Parameters:
        file_path: :obj:`pathlib.Path`
            the path to the folder where the sedml file will be saved
        model_name: str
            the name of the cellml model file
        model_id_base: str
            the base name of the model id in the sedml file
        changes_list: list of dictionaries
            the list of changes to the model, each change is a dictionary and corresponds to one task
        outputs: dict
            the dictionary for the outputs of the model
        dict_algorithm: dict 
            the dictionary for the algorithm used in the simulation
        stepSize: float
            the step size of the simulation

    Returns:
        sedFilename: the name of the sedml file

    side effects:
        a sedml file is created
    
    """
    dict_sedDocument=create_dict_sedDocment()
    # This is the sedml file (relative) path and name, assuming in the same folder with the CellML model file
    sedFilename = model_name+'_'+model_id_base+'_V2.sedml' 
    full_path = Path(file_path / sedFilename).as_posix()
    # This is the model file name, assuming in the same folder with the sedml file
    model_source = model_name + '.cellml'
    # The following is the simulation setting
    simSetting={'type':'OneStep','algorithm':dict_algorithm,'step':stepSize}
    for i in range(len(changes_dict)):
        model_id = model_name+'_'+model_id_base+'_'+str(i) # This is the model id in the sedml, could be different from the model file name               
        # This is to modify the model parameters if needed
        changes=changes_dict[i] 
        # The following is to add the task information to the dictionary
        add_sedTask2dict(dict_sedDocument, model_id, model_source,changes,simSetting,outputs)
    try:
        doc=create_sedDocment(dict_sedDocument)
    except ValueError as err:
        print(err)
    write_sedml(doc,full_path)
    print(validate_sedml(full_path))
    #doc=read_sedml(full_path) # Must read the sedml file again to avoid the error in the next step
    return full_path

def map_datafile(fid,datafile, observables=[],experimentalConditions=[], time=None, data_summary='data_summary', ):
    """"
    This function maps the data in a data file to the observables and experimental conditions specified in the sedml file

    Parameters:
        fid: str
            the id of the data file in the sedml file
        datafile: str
            the path to the data file relative to the sedml file
        observables: list of lists
            the list of observables, each observable is a list: 
            [column_name,startIndex,endIndex,component,name,weight]
            column_name: str, the name of the column in the data file
            startIndex: int or None, the start index of the column in the data file
            endIndex: int or None, the end index of the column in the data file
            component: str, the component of the observable in the CellML model
            name: str,the name of the observable in the CellML model
            weight: str or float, the weight of the observable, default is 1
        experimentalConditions: list of lists
            the list of experimental conditions, each experimental condition is a list:
            [column_name,startIndex,endIndex,index_value,component,name]
            column_name: str, the name of the column in the data file
            startIndex: int or None, the start index of the column in the data file
            endIndex: int or None, the end index of the column in the data file
            index_value: str or None, the index value of the value in the data file
            component: str, the component of the experimental condition variable in the CellML model
            name: str, the name of the experimental condition variable in the CellML model
        time: dict
            time={'column_name':'t','startIndex':0,'endIndex':None,'component':'NKE_BG_Env','name':'t'}
            default is None
        data_summary: str
            the summary of the data file

    Returns:
        experimentData_files: dict
            the dictionary for the data files in the sedml file
        time_map: tuple
            the tuple for the time in the sedml file, (fid,'time')
        observables_map: list of tuples
            the list for the observables mapping in the sedml file
            simplemath str: 'abs','-',''
            each tuple is (fid,datasourceID,'')
        experimentalConditions_map: list of tuples
            the list for the experimental conditions mapping in the sedml file
            each tuple is (fid,datasourceID)
    """
    experimentData_files={fid:{'data_summary':data_summary,'data_file':datafile,'observables':{},'experimentalConditions':{}}}

    if time is not None:
        experimentData_files[fid]['time'] = {'time': time}
        time_map=(fid,'time')
    else:
        time_map=None
    observables_map=[]
    experimentalConditions_map=[]
    for observable in observables:
        datasourceID=observable[0]
        experimentData_files[fid]['observables'][datasourceID] = {'column_name': observable[0], 'startIndex': observable[1], 'endIndex': observable[2], 'component': observable[3], 'name': observable[4], 'weight': observable[5]}
        observables_map.append((fid,datasourceID,''))
    for exp in experimentalConditions:
        datasourceID=exp[0]
        experimentData_files[fid]['experimentalConditions'][datasourceID] = {'column_name': exp[0], 'startIndex': exp[1], 'endIndex': exp[2], 'index_value': exp[3], 'component': exp[4], 'name': exp[5]}
        experimentalConditions_map.append((fid,datasourceID))
    return experimentData_files,time_map,observables_map,experimentalConditions_map

def get_adjustableParameters(adjustables, experimentReferences=['fit_1'],scale='linear'):
    """

    This function specifies the adjustable parameters in the sedml file

    Parameters:
        adjustables: list of lists
            The list of adjustable parameters, each adjustable parameter is a list:
            [component, name, lowerBound, upperBound, initialValue,  experimentReferences]
            component: str, the component of the adjustable parameter in the CellML model
            name: str, the name of the adjustable parameter in the CellML model
            lowerBound: float, the lower bound of the adjustable parameter
            upperBound: float, the upper bound of the adjustable parameter
            initialValue: float, the initial value of the adjustable parameter
            experimentReferences: list of str, the list of experiment references
        scale: str, the scale method of the adjustable parameter, default is linear, can be linear, log or log10

    Returns:
        adjustableParameters: dict
            The dictionary for the adjustable parameters in the sedml file
    
    """
    adjustableParameters={}
    for adjustable in adjustables:
        parameterId=adjustable[0]+'_'+adjustable[1]
        adjustableParameters[parameterId]={'component':adjustable[0],'name':adjustable[1],'lowerBound':adjustable[2],'upperBound':adjustable[3],'initialValue':adjustable[4],'scale':scale,'experimentReferences':experimentReferences}
    return adjustableParameters

def pe_task(file_path, model_name, model_id_base, changes_list, experimentData_files,adjustableParameters,fitExperiments,dict_algorithm_opt):
    dict_sedDocument=create_dict_sedDocment()
    model_id = model_name+ '_'+model_id_base# This is the model id in the sedml, could be different from the model file name
    sedFilename = model_id+'_pe.sedml' 
    # This is the sedml file (relative) path and name, assuming in the same folder with the CellML model file   
    full_path = Path(file_path / sedFilename).as_posix() 
    # This is the model id in the sedml file, which is also the task id and output id
    model_names=[model_id]
    # This is the model file name, assuming in the same folder with the sedml file
    model_sources=[model_name+'.cellml']
    # ******************** This is to modify the model parameters if needed ********************
    changes=changes_list[0]   
    try:            
        add_peTask2dict(dict_sedDocument, model_names, model_sources,changes,experimentData_files, adjustableParameters,fitExperiments,dict_algorithm_opt)
    except ValueError as err:
        print(err)
        exit()
    try:
        doc=create_sedDocment(dict_sedDocument)
    except ValueError as err:
        print(err)
        exit()
    write_sedml(doc,full_path)
    print(validate_sedml(full_path))
    # doc=read_sedml(full_path) # Must read the sedml file again to avoid the error in the next step
    return full_path