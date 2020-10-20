# _*_ coding: utf-8 -*-
import pandas as pd
import numpy as np

length = 4000

df = pd.read_csv("전처리1019.csv")
data_z = df['z']
z = list(data_z.str.split(', '))
ar = np.zeros((length, 1), dtype=object) # 0으로 채워진 데이터 크기만큼의 배열 생성(2차원)
data1 = pd.DataFrame(ar, columns=['data']) # 0으로 채워진 데이터 프레임 생성

for i in range(len(z)):
    temp = []
    for j in range(len(z[i])): 
        if z[i][j].count('[') > 0:
            erase = z[i][j].lstrip('[')
        if z[i][j].count(']') > 0:
            erase = z[i][j].rstrip(']')
        temp.append(erase)
    t = pd.Series(temp) # 리스트를 Series로 변환
    data1['data'][i] = t # 데이터 프레임에 Series를 넣어줌.

print(data1.dtypes)
data1.to_csv("./filename.csv", mode='w')