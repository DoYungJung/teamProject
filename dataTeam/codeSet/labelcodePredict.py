#!/usr/bin/env python
# coding: utf-8

# # 라이브러리 선언

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
from sklearn import datasets, tree
from sklearn import svm
from sklearn.metrics import accuracy_score

# 학습모델 저장 라이브러리
import joblib


# In[2]:


import function as fc


# ## 1.데이터 불러오기

# In[3]:


##db에서 불러오기
#engine = create_engine('mysql+pymysql://root:1023@127.0.0.1:3306/dataDB')
# mergeAreaTotal = pd.read_sql_query('select * from mergeAreaTotal', engine)

##(연습) 임시로 csv로 가져와서 실습
mergeAreaTotal = pd.read_csv("../../dataset/mergeAreaTotal.csv", sep = "|")
labelcodeAddData = fc.labelFun(mergeAreaTotal).loc[:, ["index", "name","tenCen","twoCen","threeCen","fourCen","fiveCen",
                                                       "sixCen","womanRatio","manRatio", "labelcode" ] ]


# ## 2.데이터 분리

# In[4]:


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

labelcodeAddData["prefer1"] = np.where( (labelcodeAddData.young_new==1)&(labelcodeAddData.old_new==1)&(labelcodeAddData.index%2 ==0) , 3 ,
                                      np.where( (labelcodeAddData.young_new==1)&(labelcodeAddData.old_new==1)&(labelcodeAddData.index%2 ==1) , 2 ,
                                      np.where(  (labelcodeAddData.young_new==1)&(labelcodeAddData.old_new==0) , 3 , 
                                      np.where ( (labelcodeAddData.young_new==0)&(labelcodeAddData.old_new==1) , 2  , 1  ))))
                                                            
labelcodeAddData["prefer2"] = np.where((labelcodeAddData.woman==1 )& (labelcodeAddData.man ==1), 4,
                                       np.where((labelcodeAddData.woman==1) & (labelcodeAddData.man ==0),3,
                                                np.where((labelcodeAddData.woman==0) & (labelcodeAddData.man ==1), 2, 1)))

refinedData = labelcodeAddData.loc[:, ["labelcode","prefer1", "prefer2" ]]

groupKey=["labelcode","prefer1"]
gnCntData1 = refinedData.groupby(groupKey)["prefer1"].agg(["count"]).reset_index(drop=False)


# In[5]:


mergedData = pd.merge(left=refinedData, right= gnCntData1, how="left", on=groupKey).rename(columns = {"count":"YN"})


# ### 특성 선정

# In[6]:


corrDf_label = mergedData.loc[:,["labelcode","prefer2","YN"]].corr()

corrDf_label


# In[7]:


stdCorr = 0.25


# In[8]:


features = list(mergedData.corr().loc[ (abs(mergedData.corr().labelcode) >= stdCorr) & (mergedData.corr().labelcode !=1)].index)


# In[9]:


features


# In[10]:


label = ["labelcode"]


# In[11]:


trainingData_features,testData_features,trainingData_label,testData_label=train_test_split(mergedData.loc[:,features],
                mergedData.loc[:,label],
                test_size=0.3, random_state=1)

print(trainingData_features.shape)
print(testData_features.shape)
print(trainingData_label.shape)
print(testData_label.shape)


# ## 3.모델 생성 및 학습
# 

# In[12]:


model_method_SVC =svm.SVC(random_state=1)
model_method_KN = KNeighborsClassifier(n_neighbors=3)
model_method_DT = DecisionTreeClassifier()

model_svc = model_method_SVC.fit(trainingData_features,trainingData_label)
model_knn = model_method_KN.fit(trainingData_features,trainingData_label)
model_Dt = model_method_DT.fit(trainingData_features, trainingData_label)


# ## 4.모델 예측
# 

# In[13]:


predictValue_svc = model_svc.predict(testData_features)
predictValue_kn = model_knn.predict(testData_features)
predictValue_Dt = model_Dt.predict(testData_features)


# ## 5.데이터 정리

# In[14]:


testDataAll = mergedData.loc[testData_label.index ]


# In[15]:


testDataAll["PREDICT_SVC"] = predictValue_svc
testDataAll["PREDICT_KNN"] = predictValue_kn
testDataAll["PREDICT_Dt"] = predictValue_Dt


# In[16]:


testDataAll


# In[17]:


accuracy_score(y_true = testDataAll.labelcode,
               y_pred= testDataAll.PREDICT_SVC)


# In[18]:


accuracy_score(y_true = testDataAll.labelcode,
               y_pred= testDataAll.PREDICT_KNN)


# In[19]:


accuracy_score(y_true = testDataAll.labelcode,
               y_pred= testDataAll.PREDICT_Dt)


# In[ ]:





# ## 6.학습 데이터 저장

# In[21]:


# 모델 저장
joblib.dump(model_Dt, './model_method_label.pkl')


# In[22]:


# 모델 불러오기
loaded_model = joblib.load('./model_method_label.pkl')

loaded_model

# loaded_model.predict(넣을값)


# In[ ]:




