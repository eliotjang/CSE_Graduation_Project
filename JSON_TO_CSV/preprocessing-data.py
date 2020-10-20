# Edit by Eliot Jang
# 2020-10-07 ~ 2020-10-19
import numpy as numpy
import json
import csv
from io import open

# 초기화한 이후에는 init_counter를 1로 설정해야함.
init_counter = 1
contain_x1 = []
contain_y1 = []
contain_z1 = []
contain_x2 = []
contain_y2 = []
contain_z2 = []

# 알파벳 D전까지는 계속 수정해야함
# name = 'sample(C)'

def append_normal(file_path_name):
    with open(file_path_name, "r", encoding='UTF8') as json_file:
        json_data = json.load(json_file)
        # 알파벳 D전까지는 ['RecordAccelerometer'][name + '1'] 필요
        for x in json_data['x'].values():
                contain_x1.append(float(x))
        for y in json_data['y'].values():
                contain_y1.append(float(y))
        for z in json_data['z'].values():
                contain_z1.append(float(z))
    json_file.close()

def append_elder(file_path_name):
    with open(file_path_name, "r", encoding='UTF8') as json_file:
        json_data = json.load(json_file)
        # 알파벳 D전까지는 ['RecordAccelerometer'][name + '2'] 필요
        for x in json_data['x'].values():
                contain_x2.append(float(x))
        for y in json_data['y'].values():
                contain_y2.append(float(y))
        for z in json_data['z'].values():
                contain_z2.append(float(z))
    json_file.close()

# json파일에 있는 실험자의 닉네임을 기입해야함.
name = "sample(AS)"

check_old = 'label(elder)'
# json 파일이름의 알파벳 변경 필요
append_normal('AS1.json')
#append_normal('AN1-2.json')
append_elder('AS2.json')
#append_elder('AE2-2.json')


# 날짜에 맞는 파일이름 설정 필요
with open('전체데이터전처리-1021.csv', 'a', newline='') as f:
    fieldnames = ['user', 'x', 'y', 'z', check_old]
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)

    if init_counter == 0:
        thewriter.writeheader()
    
    # 알파벳 D전까지는 정상인지 노인인지에 따라 주석처리 필요
    thewriter.writerow({'user' : name, 'x' : contain_x1, 'y' : contain_y1, 'z' : contain_z1, check_old : '0'})
    thewriter.writerow({'user' : name, 'x' : contain_x2, 'y' : contain_y2, 'z' : contain_z2, check_old : '1'})

f.close()
