import numpy as numpy
import json
import csv
from io import open
totalTime = 0
counter = 0

contain_x = []
contain_y = []
contain_z = []
tmp_x = 0.0
tmp_y = 0.0
tmp_z = 0.0

file_path = "walkingresearch-b7378-export.json"

with open(file_path, "r", encoding='UTF8') as json_file:
    json_data = json.load(json_file)
    #for time in json_data['RecordAccelerometer']['sample(A)1']['Totaltime'].values():
    #    totalTime = time

    for x in json_data['RecordAccelerometer']['sample(A)1']['x'].values():
        tmp_x = float(x)
        if tmp_x <= 0.001 and tmp_x >= -0.001:
            x = "0"
        contain_x.append(x)
    for y in json_data['RecordAccelerometer']['sample(A)1']['y'].values():
        tmp_y = float(y)
        if tmp_y <= 0.001 and tmp_y >= -0.001:
            y = "0"
        contain_y.append(y)
    for z in json_data['RecordAccelerometer']['sample(A)1']['z'].values():
        tmp_z = float(z)
        if tmp_z <= 0.001 and tmp_z >= -0.001:
            z = "0"
        contain_z.append(z)
json_file.close()

#1
with open('정상보행3.csv', 'w', newline='') as f:
    fieldnames = ['X', 'Y', 'Z', 'total_time(sec)']
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)
    thewriter.writeheader()
    length = len(contain_x)
    a = 100 * 610
    b = 100 * 910
    c = 100
    totalTime = (b-a)/c

    for i in range(a, b):
        if counter == 0:
            thewriter.writerow({'X' : contain_x[i], 'Y' : contain_y[i], 'Z' : contain_z[i], 'total_time(sec)' : totalTime})
            counter += 1
        else:
            thewriter.writerow({'X' : contain_x[i], 'Y' : contain_y[i], 'Z' : contain_z[i]})

f.close()
sum_time = 0.01