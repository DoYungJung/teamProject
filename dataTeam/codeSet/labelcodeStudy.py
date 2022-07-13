#!/usr/bin/env python
# coding: utf-8

# # 카테고리 분류 모델

# ## 라이브러리 선언

# In[1]:


##DB
import pymysql
from sqlalchemy import create_engine

#데이터 조작 및 숫자 연산
import pandas as pd
import numpy as np

# 분석모델
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm

# 분석평가지표
from sklearn.metrics import accuracy_score

# 시각화 라이브러리
from sklearn.tree import export_graphviz
import graphviz

# 학습모델 저장 라이브러리
import joblib

# 만든 함수 불러오기
import function as fc


# ## 데이터 불러오기

# In[2]:


#db에서 불러오기
engine = create_engine('mysql+pymysql://root:1023@127.0.0.1:3306/dataTeam')
mergeAreaTotal = pd.read_sql_query('select * from mergeAreaTotal', engine)


# In[3]:


labelcodeAddData = fc.labelFun(mergeAreaTotal).loc[:, ["index", "name","tenCen","twoCen","threeCen","fourCen","fiveCen",
                                                       "sixCen","womanRatio","manRatio", "labelcode" ] ]


# ## 1. 타입 통합 / 특성 숫자컬럼 추가

# In[4]:


### 10~30대 : 청년층 / 40~60대 : 중장년층
# young : 청년층 선호도 값의 합
# olde : 중장년층 선호도 값의 합
# youngMean : 전체 청년층 선호도의 평균
# oldMean : 전체 중장년층 선호도의 평균
# young_new : 청년층 평균보다 해당 가게의 선호도 값이 크면 1, 작으면 0
# old_new : 청년층 평균보다 해당 가게의 선호도 값이 크면 1, 작으면 0

### 남성 / 여성 선호도
# womanMean : 전체 여성 선호도의 평균
# manMean : 전체 남성 선호도의 평균
# man : 남성 평균보다 해당 가게의 선호도 값이 크면 1, 작으면 0
# woman : 여성 평균보다 해당 가게의 선호도 값이 크면 1, 작으면 0

labelcodeAddData["young"] = labelcodeAddData.tenCen+labelcodeAddData.twoCen+ labelcodeAddData.threeCen
labelcodeAddData["old"] =labelcodeAddData.fourCen+labelcodeAddData.fiveCen+labelcodeAddData.sixCen
youngMean = labelcodeAddData.young.mean()
oldMean = labelcodeAddData.old.mean()
labelcodeAddData["young_new"] = np.where(labelcodeAddData["young"]>youngMean, 1, 0)
labelcodeAddData["old_new"] = np.where(labelcodeAddData["old"]>oldMean, 1, 0)

womanMean = labelcodeAddData.womanRatio.mean()
manMean = labelcodeAddData.manRatio.mean()
labelcodeAddData["man"] = np.where(labelcodeAddData["manRatio"]>manMean, 1, 0)
labelcodeAddData["woman"] = np.where(labelcodeAddData["womanRatio"]>womanMean, 1, 0)


# In[5]:


### 새로운 features 생성
## prefer_generation_diff : 청년층과 중장년층의 선호도 비교
# 1 : 둘 다 비선호
# 2 : 중장년 선호
# 3 : 청년 선호
# 4 : 둘 다 선호
## prefer_gender_diff : 남성과 여성의 선호도 비교
# 1 : 둘 다 비선호
# 2 : 남성 선호
# 3 : 여성 선호
# 4 : 둘 다 선호

labelcodeAddData["prefer_generation_diff"] = np.where( (labelcodeAddData.young_new==1)&(labelcodeAddData.old_new==1) , 4,
                              np.where((labelcodeAddData.young_new==1)&(labelcodeAddData.old_new==0) , 3,
                              np.where( (labelcodeAddData.young_new==0)&(labelcodeAddData.old_new==1), 2,1)) )
                                                            
labelcodeAddData["prefer_gender_diff"] = np.where((labelcodeAddData.woman==1 )& (labelcodeAddData.man ==1), 4,
                                       np.where((labelcodeAddData.woman==1) & (labelcodeAddData.man ==0),3,
                                                np.where((labelcodeAddData.woman==0) & (labelcodeAddData.man ==1), 2, 1)))


# In[6]:


refinedData = labelcodeAddData.loc[:, ["labelcode","prefer_generation_diff", "prefer_gender_diff" ]]

groupKey=["labelcode","prefer_generation_diff"]
gnCntData1 = refinedData.groupby(groupKey)["prefer_generation_diff"].agg(["count"]).reset_index(drop=False)


# In[7]:


mergedData = pd.merge(left=refinedData, right= gnCntData1, how="left", on=groupKey).rename(columns = {"count":"favorite_count"})


# ## 2. 특성 선정 / 데이터 분리

# ### 2-1. 특성 선정

# In[8]:


corrDf_label = mergedData.loc[:,["labelcode","prefer_gender_diff","favorite_count"]].corr()

corrDf_label


# In[9]:


stdCorr = 0.25


# In[10]:


features = list(mergedData.corr().loc[ (abs(mergedData.corr().labelcode) >= stdCorr) & (mergedData.corr().labelcode !=1)].index)


# In[11]:


features


# In[12]:


label = ["labelcode"]


# ### 2-2. 데이터 분리

# In[13]:


trainingData_features,testData_features,trainingData_label,testData_label=train_test_split(mergedData.loc[:,features],
                mergedData.loc[:,label],
                test_size=0.3, random_state=1)

print(trainingData_features.shape)
print(testData_features.shape)
print(trainingData_label.shape)
print(testData_label.shape)


# ## 3.모델 적용

# In[14]:


model_method_SVC =svm.SVC(random_state=1)
model_method_KN = KNeighborsClassifier(n_neighbors=3)
model_method_DT = DecisionTreeClassifier()

model_svc = model_method_SVC.fit(trainingData_features,trainingData_label)
model_knn = model_method_KN.fit(trainingData_features,trainingData_label)
model_Dt = model_method_DT.fit(trainingData_features, trainingData_label)


# In[15]:


model_Dt


# ## 4.모델 예측

# In[16]:


predictValue_svc = model_svc.predict(testData_features)
predictValue_kn = model_knn.predict(testData_features)
predictValue_Dt = model_Dt.predict(testData_features)


# In[17]:


predictValue_Dt


# ## 5.데이터 정리

# ### 5-1. 데이터 정리

# In[18]:


testDataAll = mergedData.loc[testData_label.index ]


# In[19]:


testDataAll["PREDICT_SVC"] = predictValue_svc
testDataAll["PREDICT_KNN"] = predictValue_kn
testDataAll["PREDICT_Dt"] = predictValue_Dt


# In[20]:


testDataAll


# ### 5-2. 결과 검증 (정확도 비교)

# In[21]:


# SVC 정확도
accuracy_score(y_true = testDataAll.labelcode,
               y_pred= testDataAll.PREDICT_SVC)


# In[22]:


# KNN 정확도
accuracy_score(y_true = testDataAll.labelcode,
               y_pred= testDataAll.PREDICT_KNN)


# In[23]:


# DT 정확도
accuracy_score(y_true = testDataAll.labelcode,
               y_pred= testDataAll.PREDICT_Dt)


# ### 5-3. 시각화

# In[24]:


dot_data_DT = export_graphviz(decision_tree=model_Dt,
                          rounded=True)


# In[25]:


### X[0] : trainingData_features_favorite_count
graph_DT = graphviz.Source(dot_data_DT, format="png")
graph_DT


# In[26]:


graph_DT.render("label_tree_DT", format="png")


# ## 6.학습 데이터 저장

# In[27]:


# 모델 저장
joblib.dump(model_Dt, './model_method_label.pkl')


# In[28]:


# 모델 불러오기
loaded_model = joblib.load('./model_method_label.pkl')

loaded_model

# loaded_model.predict(넣을값)


# In[ ]:




