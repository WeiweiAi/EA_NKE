import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sedCellMLpy')))
from pathlib import Path
from sedCellMLpy.sedCollector import read_sedml
from sedCellMLpy.sedExecutor import exec_parameterEstimationTask, exec_sed_doc# sedCellMLpy.sedExecutor 

if __name__ == "__main__":

    parent_path = Path(__file__).parent.parent / 'cad' / 'models'
    simulation_path = Path(__file__).parent.parent / 'cad' / 'models' / 'simulation'

    full_path= parent_path / 'NKE_BG_6_state_ATPNaZKV2_fixedV_ss_pe.sedml'
    ss_time={'fit_1':0.3,'fit_2':0.3,'fit_3':0.3,'fit_4':0.3}
    rel_out_path='./simulation'   
    doc=read_sedml(Path(full_path).as_posix())
    working_dir=Path(full_path).resolve().parent.as_posix()
    exec_sed_doc(doc, working_dir, working_dir, rel_out_path=rel_out_path, external_variables_info={},
                  external_variables_values=[],ss_time=ss_time,cost_type=None)