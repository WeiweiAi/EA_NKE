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

def run_simulation(full_path):
    doc=read_sedml(full_path)
    working_dir=Path(full_path).resolve().parent
    exec_sed_doc(doc, working_dir, working_dir, rel_out_path='./simulation', external_variables_info={},
                  external_variables_values=[],ss_time={},cost_type=None)


if __name__ == "__main__":
    sedml_jsonfiles=['NKE_BG_15_state_sedmls.json','NKE_BG_15_state_fixedV_sedmls.json','NKE_BG_6_state_ATPNaZK_fit_fixedV_sedmls.json','NKE_BG_6_state_ATPNaZK_fit_sedmls.json']
    
    for sedml_jsonfile in sedml_jsonfiles:
        sedml_jsonfile = sedml_jsonfile
        full_path = simulation_path / sedml_jsonfile
        sedml_dict = read_json(full_path)
        for sedml_file in sedml_dict.values():
            run_simulation(sedml_file)
