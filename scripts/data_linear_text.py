
import csv
from pathlib import Path
import os
from tracemalloc import start
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_path = Path(__file__).parent.parent / 'cad' / 'models'
simulation_path = Path(__file__).parent.parent / 'cad' / 'models' / 'simulation'
path_=os.path.join(current_dir, '../cad/data/')

filename = path_ + 'faber_rudy_modified_version_2000_with_corrected_ICaT_data_1000.csv'
timeColumn = int(0)
valueColumn = int(1)
timeUnits = 'second'
unitsName = 'volt'
dV_unitsName = 'volt_per_sec'
numberOfRepeats = int(1)
every = int(1)

# Read in the data
time = [0]
data = [-85]
slopes=[0]
previousTime=0.0
previousValue=0
start_index=5001
T=1000
T_end=start_index+T*10

with open(filename, "r") as f:
    reader = csv.reader(f, delimiter=",")
    for i, line in enumerate(reader):
        if i % every == 0 and i>=start_index and i <= T_end:
            try:
                currentTime = float(line[timeColumn])  # convert ms to s
                currentValue = float(line[valueColumn])  # convert mV to V
                previousTime=time[-1]
                previousValue=data[-1]
                slope=(currentValue-previousValue)/(currentTime-previousTime)
                if i==start_index:
                    time.append(currentTime)
                    data.append(currentValue)
                    slopes.append(slope)                     
                elif i < T_end:                    
                    if abs(currentValue-previousValue)>=5 and (currentTime-previousTime)<=2:
                        time.append(currentTime)
                        data.append(currentValue)
                        slopes.append(slope)
                    elif abs(currentValue-previousValue)>=3 and(currentTime-previousTime)>20:
                        time.append(currentTime)
                        data.append(currentValue)
                        slopes.append(slope) 
                else: 
                    time.append(currentTime)
                    data.append(-85)
                    slope=(-85-previousValue)/(currentTime-previousTime)
                    slopes.append(slope)
            except ValueError:
                break

# save processed data to new csv file: time, data, slopes
output_filename = path_ + 'processed_faber_rudy_data_1000.csv'
with open(output_filename, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['time', 'data', 'slope'])
    for t, d, s in zip([x/1000 for x in time], [x/1000 for x in data], slopes):
        writer.writerow([t, d, s])

# plot the data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv(output_filename)
time = df['time'].values
data = df['data'].values
slope = df['slope'].values

fig, ax = plt.subplots()
ax.plot(time, data)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Membrane Potential (mV)')
ax.set_title('Processed Faber-Rudy Data')
plt.show()

output_txt_filename = path_ + 'faber_rudy_data_1000.txt'
with open(output_txt_filename, "w") as f:
    n_points = len(time)
    for i in range(n_points):
        f.writelines(f'        var V_{i}: volt {{init: {data[i]}}};\n')
    for i in range(1, n_points):
        if  i == n_points - 1:
            f.writelines(f'        var dV_{i}: volt_per_sec;\n')
        else:
            f.writelines(f'        var dV_{i}: volt_per_sec {{init: {slopes[i]}}};\n')
    f.writelines('        var dV: volt_per_sec;\n')
    f.writelines(f'        var t{1}: second {{init: 0}};\n')
    for i in range(2,n_points-1):
            f.writelines(f'        var t{i}: second;\n')
    f.writelines('        var T_cardiac: second;\n')
    f.writelines(f'        var T_0: second {{init: {time[-1]-time[1]}}};\n\n')

    for i in range(2, n_points):
        if i == n_points - 1:
            f.writelines(f'        dV_{i}      = (V_{i}-V_{i-1})/(T_0-t{i-1});\n')
    f.writelines('        T_cardiac = t-T_0*floor(t/T_0);\n')
    for i in range(2, n_points-1):
        f.writelines(f'        t{i}        = t{i-1}+(V_{i}-V_{i-1})/dV_{i};\n')

    f.writelines('        dV = sel\n')
    for i in range(1,n_points-1):
        if i< n_points -2:
            f.writelines(f'            case (T_cardiac > t{i}) and (T_cardiac <= t{i+1}) and (t>T_0):\n')
            f.writelines(f'                dV_{i+1};\n')
        else:
            f.writelines(f'            case (T_cardiac >= t{i}) and (T_cardiac <= T_0) and (t>T_0):\n')
            f.writelines(f'                dV_{i+1};\n')
        
    f.writelines('            otherwise:\n')
    f.writelines('                0{volt_per_sec};\n')
    f.writelines('        endsel;\n')