import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sedCellMLpy'))
# add the parent folder and its subfolders to the system path

from sedCellMLpy.sedCollector import read_sedml
from sedCellMLpy.sedExecutor import exec_sed_doc
from pathlib import Path

parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ss_time={'fit_1':10,'fit_2':10,'fit_3':10,'fit_4':10}
files=['NKE_Hill_ss_ss_pe']
for file in files:
    full_path=parent_path + '/cad/models/{}.sedml'.format(file)
    print(full_path)
    doc=read_sedml(full_path)
    working_dir=Path(full_path).resolve().parent.as_posix()
    exec_sed_doc(doc, working_dir, working_dir, rel_out_path='./simulation', external_variables_info={},
                  external_variables_values=[],ss_time=ss_time,cost_type='AE')