# 2020-09-22 ~ 
import numpy as numpy
import json
import csv
from io import open

file_path = "walkingresearch-b7378-export.json"
init_counter = 1 # 초기화할 생각이 있으면 0으로 설정.
tmp_x = 0.0
tmp_y = 0.0
tmp_z = 0.0
contain_x = []
contain_y = []
contain_z = []
name = "sample(A)"

with open(file_path, "r", encoding='UTF8') as json_file:
    json_data = json.load(json_file)

    for x in json_data['RecordAccelerometer'][name + '2']['x'].values():
        #tmp_x = float(x)
        #if tmp_x <= 0.001 and tmp_x >= -0.001:
        #    x = "0"
        contain_x.append(float(x))
    for y in json_data['RecordAccelerometer'][name + '2']['y'].values():
        #tmp_y = float(y)
        #if tmp_y <= 0.001 and tmp_y >= -0.001:
        #    y = "0"
        contain_y.append(float(y))
    for z in json_data['RecordAccelerometer'][name + '2']['z'].values():
        #tmp_z = float(z)
        #if tmp_z <= 0.001 and tmp_z >= -0.001:
        #    z = "0"
        contain_z.append(float(z))
json_file.close()

with open('전처리.csv', 'a', newline='') as f:
    fieldnames = ['user', 'x', 'y', 'z', 'label(elder)']
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)

    if init_counter == 0:
        thewriter.writeheader()

    thewriter.writerow({'user' : name, 'x' : contain_x, 'y' : contain_y, 'z' : contain_z, 'label(elder)' : '1'})

f.close()