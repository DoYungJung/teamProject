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
from sklearn import datasets, tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

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


corrDf_yn = mergedData.loc[:,[ "prefer1", "prefer2","YN"]].corr()


# In[7]:


corrDf_yn


# In[8]:


stdCorr = 0.5


# In[9]:


features = corrDf_yn.loc[(abs(corrDf_yn.YN)> stdCorr) &(corrDf_yn.YN!=1) ].index


# In[10]:


label = ["YN"]


# In[11]:


trainingData_features_yn,testData_features_yn,trainingData_label_yn,testData_label_yn=train_test_split(mergedData.loc[:,features],
                mergedData.loc[:,label],
                test_size=0.3, random_state=1)

print(trainingData_features_yn.shape)
print(testData_features_yn.shape)
print(trainingData_label_yn.shape)
print(testData_label_yn.shape)


# ## 3.모델 생성 및 학습
# 

# In[12]:


model_yn_method_tr = tree.DecisionTreeRegressor(random_state=2)
model_yn = model_yn_method_tr.fit(trainingData_features_yn,trainingData_label_yn)


# ## 4.모델 예측
# 

# In[13]:


predict_yn = model_yn.predict(testData_features_yn)


# ## 5.데이터 정리

# In[14]:


predictData_yn = pd.DataFrame(predict_yn, columns =["PREDICT_YN"])


# In[15]:


testData_label_yn.reset_index(drop=True,inplace=True)


# In[16]:


testData_label_yn["PREDICT_YN"] = predictData_yn


# In[17]:


finalResult_yn = testData_label_yn


# In[18]:


finalResult_yn


# In[ ]:





# In[ ]:





# ## 6.학습 데이터 저장

# In[19]:


# 모델 저장
joblib.dump(model_yn_method_tr, './model_method_yn.pkl')


# In[20]:


# 모델 불러오기
loaded_model = joblib.load('./model_method_yn.pkl')

loaded_model

# loaded_model.predict(넣을값)


# In[ ]:




