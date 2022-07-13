#!/usr/bin/env python
# coding: utf-8

# # 라이브러리 선언

# In[25]:


#입력 받기
import sys

#DB
import pymysql
from sqlalchemy import create_engine

#데이터 조작 및 숫자 연산
import pandas as pd
import numpy as np

# 분석모델
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

# 학습모델 저장 라이브러리
import joblib


# In[2]:


import function as fc


# In[ ]:





# ## 입력값 받기

# In[3]:


genderInput = sys.argv[1]## 3 여자 2 남자
ageInput = sys.argv[2]## 3 청년 2 중장년

# genderInput = 2
# ageInput = 3


# ## 학습모델 불러와서 예측

# In[4]:


#yn 예측 모델 불러오기
loaded_model = joblib.load('./model_method_yn.pkl')

predictYN = loaded_model.predict([[ageInput]])[0]


# In[5]:


#labelcode 예측 모델 불러오기
loaded_model = joblib.load('./model_method_label.pkl')

predict_labelcode = loaded_model.predict([[genderInput, predictYN]])[0]


# In[ ]:





# # price를 기준으로 분류하기

# ## 1.데이터 불러오기

# In[6]:


##db에서 불러오기
engine = create_engine('mysql+pymysql://root:1023@127.0.0.1:3306/dataDB', echo = False)
firstData = pd.read_sql_query('select * from final_total_data', engine)
secondData = pd.read_sql_query('select * from scoreInfo', engine)

##(연습) 임시로 csv로 가져와서 실습
# firstData = pd.read_csv("../../dataset/final_total_data.csv", sep="|")
# secondData = pd.read_csv("../../dataset/scoreInfo.csv",sep="|")


# In[7]:


joinKey=["index","name"]


# In[8]:


mergedData = pd.merge(left = firstData, right= secondData, on=joinKey, how="left")


# In[9]:


mergedData = fc.labelFun(mergedData)


# In[10]:


# 예측한 label코드에 해당하는 데이터만 조회
mergedData = mergedData.loc[mergedData.labelcode == predict_labelcode]


# In[12]:


# 17만원 이상인게 (702-694)개 이다 이것들 제외하고 스케일링 실시

experimentData = mergedData.loc[mergedData.price<170000]

testDf=experimentData.loc[:,["score_weighted","price"]]


# In[15]:


# 정규화 진행
scaler = MinMaxScaler()
data_scale = scaler.fit_transform(testDf)


# In[16]:


# K means 클러스터링 학습
from sklearn.cluster import KMeans


# In[ ]:





# In[17]:


# 그룹 수, random_state 설정
k=3
model = KMeans(n_clusters = k, random_state = 1)


# In[18]:


# 정규화된 데이터에 학습
model.fit(data_scale)


# In[19]:


# 클러스터링 결과 각 데이터가 몇 번째 그룹에 속하는지 저장
testDf['cluster'] = model.fit_predict(data_scale)


# In[20]:


temp = experimentData.loc[:,["index","name","labelcode"]]

priceCluster = pd.concat([temp, testDf], axis=1)

priceCluster

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

cheap

##가성비 추천 식당 리스트

cheapGood = priceCluster.loc[priceCluster.cluster==cheap].sort_values(by= ["score_weighted"], ascending = False)


print(list(cheapGood.name)[0])

premium = priceCluster.loc[priceCluster.cluster==expensive].sort_values(by= ["score_weighted"], ascending = False)

print(list(premium.name)[0])


# In[21]:


cheapGood


# # DB에 저장하기

# In[ ]:


cheapGood.to_sql('cheap', engine, if_exists='append',index=False)
premium.to_sql('premium', engine, if_exists='append',index=False)

pd.read_sql_table('cheap', engine)

