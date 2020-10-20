# Edit by Eliot Jang
# 2020-10-19 ~ 
import enum
import pandas as pd
import numpy as np
import json
import csv
from io import open

subject = list()
for i in range(65, 91):
    subject.append(chr(i))
for i in range(65, 84):
    subject.append('A' + chr(i))

zero = np.zeros((4000, 1), dtype=object)
normal_y_dataframe = pd.DataFrame(zero, columns=['data'])
normal_z_dataframe = pd.DataFrame(zero, columns=['data'])
normal_x_dataframe = pd.DataFrame(zero, columns=['data'])
elder_x_dataframe = pd.DataFrame(zero, columns=['data'])
elder_y_dataframe = pd.DataFrame(zero, columns=['data'])
elder_z_dataframe = pd.DataFrame(zero, columns=['data'])

normal_flat_start_index = 2500
normal_flat_end_index = 6500
elder_flat_start_index = 4000
elder_flat_end_index = 8000

check_old = 'label(elder)'
file_name = '평지데이터전처리-1021.csv'

def insert_to_dataframe(arr, str, elder_flag):
    series = pd.Series(arr)
    if str == 'x' and elder_flag == 0:
        normal_x_dataframe['data'] = series
    if str == 'y' and elder_flag == 0:
        normal_y_dataframe['data'] = series
    if str == 'z' and elder_flag == 0:
        normal_z_dataframe['data'] = series
    if str == 'x' and elder_flag == 1:
        elder_x_dataframe['data'] = series
    if str == 'y' and elder_flag == 1:
        elder_y_dataframe['data'] = series
    if str == 'z' and elder_flag == 1:
        elder_z_dataframe['data'] = series

def append_normal(file_path_name, subject_index):
    normal_x = []
    normal_y = []
    normal_z = []
    with open(file_path_name, "r", encoding='UTF8') as json_file:
        json_data = json.load(json_file)
        
        if subject_index < 3:
            if subject_index == 0:
                name = 'sample(A)'
            elif subject_index == 1:
                name = 'sample(B)'
            else:
                name = 'Sample(C)'
            index_count = 0
            for x in json_data['RecordAccelerometer'][name + '1']['x'].values():
                if (normal_flat_start_index <= index_count < normal_flat_end_index):
                    normal_x.append(float(x))
                index_count += 1
            index_count = 0
            for y in json_data['RecordAccelerometer'][name + '1']['y'].values():
                if (normal_flat_start_index <= index_count < normal_flat_end_index):
                    normal_y.append(float(y))
                index_count += 1
            index_count = 0
            for z in json_data['RecordAccelerometer'][name + '1']['z'].values():
                if (normal_flat_start_index <= index_count < normal_flat_end_index):
                    normal_z.append(float(z))  
                index_count += 1          

        else:
            index_count = 0
            for x in json_data['x'].values():
                if (normal_flat_start_index <= index_count < normal_flat_end_index):
                    normal_x.append(float(x))
                index_count += 1  
            index_count = 0
            for y in json_data['y'].values():
                if (normal_flat_start_index <= index_count < normal_flat_end_index):
                    normal_y.append(float(y))
                index_count += 1  
            index_count = 0
            for z in json_data['z'].values():
                if (normal_flat_start_index <= index_count < normal_flat_end_index):
                    normal_z.append(float(z))
                index_count += 1  
        
        insert_to_dataframe(normal_x, 'x', 0)
        insert_to_dataframe(normal_y, 'y', 0)
        insert_to_dataframe(normal_z, 'z', 0)
    json_file.close()

    with open(file_name, 'a', newline='') as f:
        fieldnames = ['user', 'x', 'y', 'z', check_old]
        thewriter = csv.DictWriter(f, fieldnames=fieldnames)
        thewriter.writerow({'user' : 'sample(' + subject[subject_index] + ')', 'x' : normal_x_dataframe, 'y' : normal_y_dataframe, 'z' : normal_z_dataframe, check_old : '0'})
    f.close()    

def append_elder(file_path_name, subject_index):
    elder_x = []
    elder_y = []
    elder_z = []    
    with open(file_path_name, "r", encoding='UTF8') as json_file:
        json_data = json.load(json_file)

        if subject_index < 3:
            if subject_index == 0:
                name = 'sample(A)'
            elif subject_index == 1:
                name = 'sample(B)'
            else:
                name = 'sample(C)'
            index_count = 0
            for x in json_data['RecordAccelerometer'][name + '2']['x'].values():
                if(elder_flat_start_index <= index_count < elder_flat_end_index):
                    elder_x.append(float(x))
                index_count += 1
            index_count = 0
            for y in json_data['RecordAccelerometer'][name + '2']['y'].values():
                if(elder_flat_start_index <= index_count < elder_flat_end_index):
                    elder_y.append(float(y))
                index_count += 1
            index_count = 0
            for z in json_data['RecordAccelerometer'][name + '2']['z'].values():
                if(elder_flat_start_index <= index_count < elder_flat_end_index):
                    elder_z.append(float(z))   
                index_count += 1

        else:
            index_count = 0
            for x in json_data['x'].values():
                if(elder_flat_start_index <= index_count < elder_flat_end_index):
                    elder_x.append(float(x))
                index_count += 1
            index_count = 0
            for y in json_data['y'].values():
                if(elder_flat_start_index <= index_count < elder_flat_end_index):
                    elder_y.append(float(y))
                index_count += 1
            index_count = 0
            for z in json_data['z'].values():
                if(elder_flat_start_index <= index_count < elder_flat_end_index):
                    elder_z.append(float(z))
                index_count += 1
        
        insert_to_dataframe(elder_x, 'x', 1)
        insert_to_dataframe(elder_y, 'y', 1)
        insert_to_dataframe(elder_z, 'z', 1)
    json_file.close()

    with open(file_name, 'a', newline='') as f:
        fieldnames = ['user', 'x', 'y', 'z', check_old]
        thewriter = csv.DictWriter(f, fieldnames=fieldnames)
        thewriter.writerow({'user' : 'sample(' + subject[subject_index] + ')', 'x' : elder_x_dataframe, 'y' : elder_y_dataframe, 'z' : elder_z_dataframe, check_old : '1'})
    f.close() 

def write_header():
    with open(file_name, 'w', newline='') as f:
        fieldnames = ['user', 'x', 'y', 'z', check_old]
        thewriter = csv.DictWriter(f, fieldnames=fieldnames)
        thewriter.writeheader()
    f.close() 

write_header()
append_normal('a1.json',0)
append_elder('a2.json',0)
append_normal('b1.json',1)
append_elder('b2.json',1)
append_normal('c1-1.json',2)
append_elder('c2-1.json',2)
append_normal('d1.json',3)
append_elder('d2.json',3)
append_normal('e1.json',4)
append_elder('e2-1.json',4)
append_normal('f1.json', 5)
append_elder('f2.json', 5)
append_normal('g1.json',6)
append_elder('g2.json',6)
append_normal('h1.json',7)
append_elder('h2.json',7)
append_normal('i1.json',8)
append_elder('i2.json',8)
append_normal('j1.json',9)
append_elder('j2.json',9)
append_normal('k1.json',10)
append_elder('k2.json',10)
append_normal('l1.json',11)
append_elder('l2.json',11)
append_normal('m1-1.json',12)
append_elder('m2.json',12)
append_normal('n1.json',13)
append_elder('n2-1.json',13)
append_normal('o1.json',14)
append_elder('o2.json',14)
append_normal('p1.json',15)
append_elder('p2.json',15)
append_normal('q1.json',16)
append_elder('q2.json',16)
append_normal('r1.json',17)
append_elder('r2.json',17)
append_normal('s1.json',18)
append_elder('s2.json',18)
append_normal('t1.json',19)
append_elder('t2.json',19)
append_normal('u1.json',20)
append_elder('u2.json',20)
append_normal('v1.json',21)
append_elder('v2.json',21)
append_normal('w1.json',22)
append_elder('w2.json',22)
append_normal('x1.json',23)
append_elder('x2.json',23)
append_normal('y1.json',24)
append_elder('y2.json',24)
append_normal('z1-1.json',25)
append_elder('z2.json',25)

append_normal('aa1.json',26)
append_normal('ab1-1.json',27)
append_elder('ab2-1.json',27)
append_normal('ac1.json',28)
append_elder('ac2.json',28)
append_normal('ad1.json',29)
append_elder('ad2.json',29)
append_normal('ae1.json',30)
append_elder('ae2-1.json',30)
append_normal('af1-1.json',31)
append_elder('af2.json',31)
append_normal('ag1.json',32)
append_elder('ag2.json',32)
append_normal('ah1-1.json',33)
append_elder('ah2.json',33)
append_normal('ai1.json',34)
append_elder('ai2.json',34)
append_normal('aj1.json',35)
append_elder('aj2.json',35)
append_normal('ak1.json',36)
append_elder('ak2.json',36)
append_normal('al1-1.json',37)
append_elder('al2.json',37)
append_normal('am1-1.json',38)
append_elder('am2.json',38)
append_normal('an1.json',39)
append_elder('an2.json',39)
append_normal('ao1.json',40)
append_elder('ao2.json',40)
append_normal('ap1.json',41)
append_elder('ap2.json',41)
append_normal('aq1.json',42)
append_elder('aq2.json',42)
append_normal('ar1.json',43)
append_elder('ar2.json',43)
append_normal('as1.json',44)
append_elder('as2.json',44)