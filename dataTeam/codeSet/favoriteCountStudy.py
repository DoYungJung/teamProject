#!/usr/bin/env python
# coding: utf-8

# # 연령대별 선호 features 생성 모델

# ## 라이브러리 선언

# In[1]:


##DB
import pymysql
from sqlalchemy import create_engine

#데이터 조작 및 숫자 연산
import pandas as pd
import numpy as np

# 분석모델 
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn import linear_model 
from sklearn import ensemble

# 분석평가지표
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

# 시각화 라이브러리
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import export_graphviz
import graphviz

# 학습모델 저장 라이브러리
import joblib

# 만든 함수 불러오기
import function as fc


# ## 데이터 불러오기

# In[2]:


##db에서 불러오기
engine = create_engine('mysql+pymysql://root:1023@127.0.0.1:3306/dataTeam')
mergeAreaTotal = pd.read_sql_query('select * from mergeAreaTotal', engine)


# ## 1. 타입 통합 / 특성 숫자컬럼 추가

# In[3]:


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


# In[4]:


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
                              np.where((labelcodeAddData.young_new==1)&(labelcodeAddData.old_new==0), 3 , 
                              np.where(  (labelcodeAddData.young_new==0)&(labelcodeAddData.old_new==1), 2,1  )) )
                                       
labelcodeAddData["prefer_gender_diff"] = np.where((labelcodeAddData.woman==1 )& (labelcodeAddData.man ==1), 4,
                                       np.where((labelcodeAddData.woman==1) & (labelcodeAddData.man ==0),3,
                                                np.where((labelcodeAddData.woman==0) & (labelcodeAddData.man ==1), 2, 1)))


# In[5]:


refinedData = labelcodeAddData.loc[:, ["labelcode","prefer_generation_diff", "prefer_gender_diff" ]]

groupKey=["labelcode","prefer_generation_diff"]
gnCntData1 = refinedData.groupby(groupKey)["prefer_generation_diff"].agg(["count"]).reset_index(drop=False)


# In[6]:


refinedData = labelcodeAddData.loc[:, ["labelcode","prefer_generation_diff", "prefer_gender_diff" ]]


# In[7]:


temp = labelcodeAddData.loc[:,["name", "labelcode","young_new","old_new","man","woman","prefer_generation_diff","prefer_gender_diff"]]


# In[8]:


temp.loc[(temp.prefer_generation_diff != 1) &(temp.prefer_generation_diff != 4)]


# In[9]:


groupKey=["labelcode","prefer_generation_diff"]

gnCntData1 = refinedData.groupby(groupKey)["prefer_generation_diff"].agg(["count"]).reset_index(drop=False)


# In[10]:


gnCntData1


# In[11]:


mergedData = pd.merge(left=refinedData, right= gnCntData1, how="left", on=groupKey).rename(columns = {"count":"favorite_count"})


# In[12]:


mergedData


# ## 2. 특성 선정 / 데이터 분리

# ### 2-1. 특성 선정

# In[13]:


corrDf_favorite_count = mergedData.loc[:,["prefer_generation_diff", "prefer_gender_diff","favorite_count"]].corr()


# In[14]:


corrDf_favorite_count


# In[15]:


stdCorr = 0.4


# In[16]:


features = corrDf_favorite_count.loc[(abs(corrDf_favorite_count.favorite_count)> stdCorr) &(corrDf_favorite_count.favorite_count!=1) ].index


# In[17]:


features


# In[18]:


label = ["favorite_count"]


# ### 2-2. 데이터 분리

# In[19]:


trainingData_features_favorite_count,testData_features_favorite_count,trainingData_label_favorite_count,testData_label_favorite_count=train_test_split(mergedData.loc[:,features],
                mergedData.loc[:,label],
                test_size=0.3, random_state=1)

print(trainingData_features_favorite_count.shape)
print(testData_features_favorite_count.shape)
print(trainingData_label_favorite_count.shape)
print(testData_label_favorite_count.shape)


# ## 3.모델 적용

# In[20]:


## decision tree


# In[21]:


model_favorite_count_method_tr = tree.DecisionTreeRegressor(random_state=1)
model_favorite_count = model_favorite_count_method_tr.fit(trainingData_features_favorite_count,trainingData_label_favorite_count)


# In[22]:


## linear regression
modelMethod_lr = linear_model.LinearRegression()
model_lr = modelMethod_lr.fit(X=trainingData_features_favorite_count,
                             y=trainingData_label_favorite_count)


# In[23]:


# model_lr.intercept_ # y절편
# model_lr.coef_ # 계수


# In[24]:


## random forest
modelMethod_Rf = ensemble.RandomForestRegressor(random_state=3)
model_Rf = modelMethod_Rf.fit(X=trainingData_features_favorite_count,
                             y=trainingData_label_favorite_count)


# ## 4.모델 예측

# In[25]:


# DT
predict_favorite_count = model_favorite_count.predict(testData_features_favorite_count)


# In[26]:


# LR
predict_lr = model_lr.predict(testData_features_favorite_count)


# In[27]:


# RF
predict_rf = model_Rf.predict(testData_features_favorite_count)


# ## 5. 데이터 정리

# ### 5-1. 데이터 정리

# In[28]:


# DT
predictData_favorite_count = pd.DataFrame(predict_favorite_count, columns =["PREDICT_DT"])
testData_label_favorite_count.reset_index(drop=True,inplace=True)
testData_label_favorite_count["PREDICT_DT"] = predictData_favorite_count
finalResult_favorite_count = testData_label_favorite_count
finalResult_favorite_count


# In[29]:


# LR
predictData_lr = pd.DataFrame(predict_lr, columns =["PREDICT_LR"])
testData_label_favorite_count.reset_index(drop=True,inplace=True)
testData_label_favorite_count["PREDICT_LR"] = predictData_lr
finalResult_favorite_count = testData_label_favorite_count
finalResult_favorite_count


# In[30]:


# RF
predictData_favorite_count = pd.DataFrame(predict_favorite_count, columns =["PREDICT_RF"])
testData_label_favorite_count.reset_index(drop=True,inplace=True)
testData_label_favorite_count["PREDICT_RF"] = predictData_favorite_count
finalResult_favorite_count = testData_label_favorite_count
finalResult_favorite_count


# ### 5-2. 결과 검증 (정확도 비교)

# In[31]:


# DT


# In[32]:


print("DT의 결과")
### (MAE)오차의 절댓값의 평균
print("MAE : {}".format( mean_absolute_error(y_true=finalResult_favorite_count.favorite_count, y_pred=finalResult_favorite_count.PREDICT_DT)))
### (MSE)오차의 제곱의 평균
print("MSE : {}".format(mean_squared_error(y_true=finalResult_favorite_count.favorite_count, y_pred=finalResult_favorite_count.PREDICT_DT)))
### (RMSE) : 제곱근 MSE
print("RMSE : {}".format(np.sqrt(mean_squared_error(y_true=finalResult_favorite_count.favorite_count, y_pred=finalResult_favorite_count.PREDICT_DT))))


# In[33]:


# LR


# In[34]:


print("LR의 결과")
### (MAE)오차의 절댓값의 평균
print("MAE : {}".format( mean_absolute_error(y_true=finalResult_favorite_count.favorite_count, y_pred=finalResult_favorite_count.PREDICT_LR)))
### (MSE)오차의 제곱의 평균
print("MSE : {}".format(mean_squared_error(y_true=finalResult_favorite_count.favorite_count, y_pred=finalResult_favorite_count.PREDICT_LR)))
### (RMSE) : 제곱근 MSE
print("RMSE : {}".format(np.sqrt(mean_squared_error(y_true=finalResult_favorite_count.favorite_count, y_pred=finalResult_favorite_count.PREDICT_LR))))


# In[35]:


# RF


# In[36]:


print("RF의 결과")
### (MAE)오차의 절댓값의 평균
print("MAE : {}".format( mean_absolute_error(y_true=finalResult_favorite_count.favorite_count, y_pred=finalResult_favorite_count.PREDICT_RF)))
### (MSE)오차의 제곱의 평균
print("MSE : {}".format(mean_squared_error(y_true=finalResult_favorite_count.favorite_count, y_pred=finalResult_favorite_count.PREDICT_RF)))
### (RMSE) : 제곱근 MSE
print("RMSE : {}".format(np.sqrt(mean_squared_error(y_true=finalResult_favorite_count.favorite_count, y_pred=finalResult_favorite_count.PREDICT_RF))))


# In[37]:


### mae와 rmse의 차이가 비슷하면 치명적인 에러가 없는 것(무난무난)
### 2배 이상 차이가 난다면 이상치값이 많은 것(어디로 튈지 모르는 모델)


# ### 5-3. 시각화

# # dicision tree

# In[38]:


# dot_data_DT = export_graphviz(decision_tree=model_favorite_count, rounded=True)
# ## X[0] : trainingData_features_favorite_count
# graph_DT = graphviz.Source(dot_data_DT, format="png")

# graph_DT.render("dt_tree_DT", format="png")


# # random forest

# In[39]:


# dot_data_RF = export_graphviz(decision_tree=model_Rf.estimators_[0],rounded=True)
# graph_RF = graphviz.Source(dot_data_RF, format="png")

# dot_data_RF = export_graphviz(decision_tree=model_Rf.estimators_[1], rounded=True)

# graph_RF = graphviz.Source(dot_data_RF, format="png")

# dot_data_RF = export_graphviz(decision_tree=model_Rf.estimators_[2], rounded=True)
# graph_RF = graphviz.Source(dot_data_RF, format="png")

# graph_RF.render("dt_tree_RF", format="png")


# # linear regression

# In[40]:


# temp = pd.DataFrame()
# temp["PREDICT_LR"] =finalResult_favorite_count.PREDICT_LR
# temp["prefer_generation_diff" ] = list(testData_features_favorite_count.prefer_generation_diff)

# sns.regplot(x='prefer_generation_diff', y='PREDICT_LR', data = temp)


# ## 6.학습 데이터 저장

# In[41]:


# 모델 저장
joblib.dump(model_favorite_count_method_tr, './model_method_favorite_count.pkl')

