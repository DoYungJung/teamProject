#!/usr/bin/env python
# coding: utf-8

# # 가격별 클러스터링 모델

# ## 라이브러리 선언

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
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

# 시각화 라이브러리
import matplotlib.pyplot as plt

# 학습모델 저장 라이브러리
import joblib

# 만든 함수 불러오기
import function as fc


# ## 데이터 불러오기

# In[2]:


##db에서 불러오기
engine = create_engine('mysql+pymysql://root:1023@127.0.0.1:3306/dataTeam', echo = False)
firstData = pd.read_sql_query('select * from final_total_data', engine)
secondData = pd.read_sql_query('select * from scoreInfo', engine)


# In[3]:


joinKey=["index","name"]


# In[4]:


mergedData = pd.merge(left = firstData, right= secondData, on=joinKey, how="left")


# In[5]:


mergedData = fc.labelFun(mergedData)


# ## 데이터 분리

# In[6]:


# 17만원 이상인게 (702-694)개 이다 이것들 제외하고 스케일링 실시

exceptedData = mergedData.loc[mergedData.price<170000]

refinedData  =exceptedData.loc[:,["score_weighted","price"]]

# 정규화 진행
scaler = MinMaxScaler()
data_scale = scaler.fit_transform(refinedData)


# ## 모델 선언 및 features만 활용하여 자율학습 예측

# In[7]:


# 그룹 수, random_state 설정
k=3
model = KMeans(n_clusters = k, random_state = 1)


# In[8]:


# 클러스터링 결과 각 데이터가 몇 번째 그룹에 속하는지 저장
refinedData['cluster'] = model.fit_predict(data_scale)


# In[9]:


model


# ## 시각화

# In[11]:


plt.figure(figsize = (8, 8))

for i in range(k):
    plt.scatter(refinedData.loc[refinedData['cluster'] == i, "price"], refinedData.loc[refinedData['cluster'] == i, "score_weighted"], 
                label = 'cluster ' + str(i))

plt.legend()
plt.title('K = %d results'%k , size = 15)
plt.xlabel('price', size = 12)
plt.ylabel('score_weighted', size = 12)
plt.show()


# ## 학습모델 저장

# In[12]:


# 모델 저장
joblib.dump(model, './price_Kmeans_model.pkl')


# In[ ]:





# In[ ]:




