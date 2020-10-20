# Edit by Eliot Jang
# 2020-10-19 ~ 
import numpy as numpy
import json
import csv
from io import open

# 초기화한 이후에는 init_counter를 1로 설정해야함.
init_counter = 1
tmp_x = 0.0
tmp_y = 0.0
tmp_z = 0.0
contain_x1 = []
contain_y1 = []
contain_z1 = []
contain_x2 = []
contain_y2 = []
contain_z2 = []

normal_flat_start_index = 2500
normal_flat_end_index = 6500
elder_flat_start_index = 4000
elder_flat_end_index = 8000

# 알파벳 D전까지는 계속 수정해야함
# name = 'sample(C)'

def append_normal(file_path_name):
    with open(file_path_name, "r", encoding='UTF8') as json_file:
        json_data = json.load(json_file)
        index_count = 0
        # 알파벳 D전까지는 ['RecordAccelerometer'][name + '1'] 필요
        for x in json_data['x'].values():
            if (normal_flat_start_index <= index_count < normal_flat_end_index):
                contain_x1.append(float(x))
            index_count += 1
        index_count = 0
        for y in json_data['y'].values():
            if (normal_flat_start_index <= index_count < normal_flat_end_index):
                contain_y1.append(float(y))
            index_count += 1
        index_count = 0
        for z in json_data['z'].values():
            if (normal_flat_start_index <= index_count < normal_flat_end_index):
                contain_z1.append(float(z))
            index_count += 1
    json_file.close()

def append_elder(file_path_name):
    with open(file_path_name, "r", encoding='UTF8') as json_file:
        json_data = json.load(json_file)
        index_count = 0
        # 알파벳 D전까지는 ['RecordAccelerometer'][name + '2'] 필요
        for x in json_data['x'].values():
            if(elder_flat_start_index <= index_count < elder_flat_end_index):
                contain_x2.append(float(x))
            index_count += 1
        index_count = 0
        for y in json_data['y'].values():
            if(elder_flat_start_index <= index_count < elder_flat_end_index):
                contain_y2.append(float(y))
            index_count += 1
        index_count = 0
        for z in json_data['z'].values():
            if(elder_flat_start_index <= index_count < elder_flat_end_index):
                contain_z2.append(float(z))
            index_count += 1
    json_file.close()

'''알파벳 AI이부후터는 정상보행과 노인체험복의 파일명이 같으므로 한번한번씩 번갈아가면서 실행시켜야함'''
# json파일에 있는 실험자의 닉네임을 기입해야함.
name = "sample(AS)"

check_old = 'label(elder)'
# json 파일이름의 알파벳 변경 필요
# 알파벳 AI이후부터는 정상보행인지 노인체험복인지에 따라 주석처리 필요
append_normal("1walkingresearch2-sample(AS)-export.json")
append_elder("2walkingresearch2-sample(AS)-export.json")

# 날짜에 맞는 파일이름 설정 필요
with open('전처리1019-testing.csv', 'a', newline='') as f:
    fieldnames = ['user', 'x', 'y', 'z', check_old]
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)

    if init_counter == 0:
        thewriter.writeheader()
    
    # 알파벳 D전까지는 정상인지 노인인지에 따라 주석처리 필요
    # 알파벳 AI이후부터는 정상인지 노인인지에 따라 주석처리 필요
    thewriter.writerow({'user' : name, 'x' : contain_x1, 'y' : contain_y1, 'z' : contain_z1, check_old : '0'})
    thewriter.writerow({'user' : name, 'x' : contain_x2, 'y' : contain_y2, 'z' : contain_z2, check_old : '1'})

f.close()
