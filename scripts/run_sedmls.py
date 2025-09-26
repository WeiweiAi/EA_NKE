import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pathlib import Path
from exp_conditions import read_json
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sedCellMLpy'))
from sedCellMLpy.sedCollector import read_sedml
from sedCellMLpy.sedExecutor import exec_sed_doc

parent_path = Path(__file__).parent.parent / 'cad' / 'models'
simulation_path = Path(__file__).parent.parent / 'cad' / 'models' / 'simulation'

def run_simulation(full_path,rel_out_path='./simulation', external_variables_info={},
                  external_variables_values=[],ss_time={},cost_type=None):
    doc=read_sedml(Path(full_path).as_posix())
    working_dir=Path(full_path).resolve().parent.as_posix()
    exec_sed_doc(doc, working_dir, working_dir, rel_out_path=rel_out_path, external_variables_info=external_variables_info,
                  external_variables_values=external_variables_values,ss_time=ss_time,cost_type=cost_type)

def run_sim_jsons (sedml_jsonfiles):
    for sedml_jsonfile in sedml_jsonfiles:
        full_path = simulation_path / sedml_jsonfile
        sedml_dict = read_json(full_path)
        for sedml_file in sedml_dict.values():
            run_simulation(parent_path / sedml_file)
   
