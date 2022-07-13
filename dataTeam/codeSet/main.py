#!/usr/bin/env python
# coding: utf-8

# # 라이브러리 선언

# In[1]:


#입력 받기
import sys

#DB
import pymysql
from sqlalchemy import create_engine

#데이터 조작 및 숫자 연산
import pandas as pd
import numpy as np

# 분석모델
from sklearn.cluster import KMeans # K means 클러스터링 학습
from sklearn.preprocessing import MinMaxScaler

# 학습모델 저장 라이브러리
import joblib

#tiem
import time
from datetime import datetime


# In[2]:


import function as fc


# In[3]:


from multiprocessing import Lock # for using Lock method(acquire(), release())


# In[4]:


lock = Lock()

## 입력값 받기

genderInput = sys.argv[1]## 3 여자 2 남자
ageInput = sys.argv[2]## 3 청년 2 중장년

# genderInput = 2
# ageInput = 3

## 학습모델 불러와서 예측

#favorite_count 예측 모델 불러오기
loaded_model = joblib.load('./model_method_favorite_count.pkl')

predict_favorite_count = loaded_model.predict([[ageInput]])[0]

#labelcode 예측 모델 불러오기
loaded_model = joblib.load('./model_method_label.pkl')

predict_labelcode = loaded_model.predict([[genderInput, predict_favorite_count]])[0]

# price를 기준으로 분류하기

## 1.데이터 불러오기

##db에서 불러오기
engine = create_engine('mysql+pymysql://root:1023@127.0.0.1:3306/dataTeam', echo = False)

firstData = pd.read_sql_query('select * from final_total_data', engine)
secondData = pd.read_sql_query('select * from scoreInfo', engine)


joinKey=["index","name"]

mergedData = pd.merge(left = firstData, right= secondData, on=joinKey, how="left")

mergedData = fc.labelFun(mergedData)

# 예측한 label코드에 해당하는 데이터만 조회
mergedData = mergedData.loc[mergedData.labelcode == predict_labelcode]

# 17만원 이상인게 (702-694)개 이다 이것들 제외하고 스케일링 실시

exceptedData = mergedData.loc[mergedData.price<170000]

refinedData=exceptedData.loc[:,["score_weighted","price"]]

# 정규화 진행
scaler = MinMaxScaler()
data_scale = scaler.fit_transform(refinedData)



# In[11]:


#labelcode 예측 모델 불러오기
loaded_model = joblib.load('./price_Kmeans_model.pkl')


# In[12]:


# # 클러스터링 결과 각 데이터가 몇 번째 그룹에 속하는지 저장
refinedData['cluster'] = loaded_model.fit_predict(data_scale)


# In[13]:


# # 그룹 수, random_state 설정
# model = KMeans(n_clusters = 3, random_state = 1)

# # 정규화된 데이터에 학습
# model.fit(data_scale)

temp = exceptedData.loc[:,["index","name","labelcode"]]

priceCluster = pd.concat([temp, refinedData], axis=1)

clusterZero = priceCluster.loc[priceCluster.cluster==0]
clusteroOne = priceCluster.loc[priceCluster.cluster==1]
clusteroTwo = priceCluster.loc[priceCluster.cluster==2]

zero = list(clusterZero.sort_values(by=["score_weighted"], ascending=False).score_weighted)[0]
one = list(clusteroOne.sort_values(by=["score_weighted"], ascending=False).score_weighted)[0]
two = list(clusteroTwo.sort_values(by=["score_weighted"], ascending=False).score_weighted)[0]

priceList = [[zero,0],[one,1],[two,2]]


for i in range(0, len(priceList)):
    for j in range(i, len(priceList)):
        if(priceList[i][0]< priceList[j][0]):
            temp = priceList[i]
            priceList[i] = priceList[j]
            priceList[j] = temp

scoreList = [priceList[0],priceList[1]]

scoreList

first = priceCluster.loc[priceCluster.cluster==scoreList[0][1]]
second = priceCluster.loc[priceCluster.cluster==scoreList[1][1]]

expensive = 0
cheap = 0

if(list(first.price)[0] > list(second.price)[0]):
    expensive = scoreList[0][1]
    cheap = scoreList[1][1]
else:  
    expensive = scoreList[1][1]
    cheap = scoreList[0][1]


##가성비 추천 식당 리스트

cheapGood = priceCluster.loc[priceCluster.cluster==cheap].sort_values(by= ["score_weighted"], ascending = False)


print(list(cheapGood.name)[0])

premium = priceCluster.loc[priceCluster.cluster==expensive].sort_values(by= ["score_weighted"], ascending = False)

print(list(premium.name)[0])

cheapGood = pd.merge(cheapGood, firstData, on = ["index", "name","price"] , how = "left").loc[:, ["index","name","gubun","price","menu1","menu2","menu3","menu4","address","phone","openingHour","detailInfo"] ]

premium = pd.merge(premium, firstData, on = ["index", "name","price"] , how = "left").loc[:, ["index","name","gubun","price","menu1","menu2","menu3","menu4","address","phone","openingHour","detailInfo"] ]



now= datetime.now()

premium_history = premium.copy()

premium_history["hisotry"] = now.strftime('%Y-%m-%d')

cheapGood_history = cheapGood.copy()

cheapGood_history["history"] = now.strftime('%Y-%m-%d')


# In[4]:


# DB에 저장하기

##web Engine 
engine2 = create_engine('mysql+pymysql://root:1023@127.0.0.1:3306/webTeam', echo = False)

try:
    lock.acquire()
    cheapGood.to_sql('history_cheapGood', engine, if_exists='append',index=False)
    time.sleep(0.3)
    premium.to_sql('history_premium', engine, if_exists='append',index=False)
    time.sleep(0.3)



    cheapGood.to_sql('cheapGood', engine2, if_exists='replace',index=False)
    time.sleep(0.3)
    premium.to_sql('premium', engine2, if_exists='replace',index=False)
    lock.release()

except Exception as e:
    print(e)


# In[ ]:




