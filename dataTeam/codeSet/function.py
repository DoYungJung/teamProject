#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

def labelFun(df):

    cvect = CountVectorizer()
    dtm = cvect.fit_transform(df["gubun"])
    # gubun에 들어있는 내용들 구분자, 띄어쓰기 기준으로 분류(중복도 제거해줌)
    feature_names = cvect.get_feature_names()

    # for문에서 사용하기 위해서 list로 담아줌
    feature_namesList = list(feature_names)

    # 카테고리 분류
    # 카테고리 분류
    categoryDic = {"이자카야": "카페및기타"
    ,"오므라이스": "아시아음식"
    ,"김밥": "한식"
    ,"피자":"양식"
    ,"포장마차": "카페및기타"
    ,"패밀리레스토랑": "카페및기타"
    ,"스테이크":"양식"
    ,"설렁탕": "한식"
    ,"블루보틀":"카페및기타"
    ,"케이크": "카페및기타"
    ,"국밥": "한식"
    ,"칼국수": "한식"
    ,"만두": "한식"               
    ,"퓨전음식": "카페및기타"
    ,"카페": "카페및기타"
    ,"디저트": "카페및기타"
    ,"베이커리": "카페및기타"
    ,"베트남음식": "아시아음식"
    ,"족발": "한식"
    ,"보쌈": "한식"
    ,"백숙": "한식"
    ,"백숙삼계탕": "한식"
    ,"찌개": "한식"
    ,"전골": "한식"
    ,"한식": "한식"
    ,"종합분식": "분식"
    ,"분식": "카페및기타"
    ,"이탈리아음식": "양식"
    ,"브런치": "카페및기타"
    ,"덮밥": "아시아음식"
    ,"쭈꾸미요리": "한식" 
    ,"냉면": "한식"
    ,"장어": "한식"
    ,"먹장어": "한식"
    ,"양식": "양식"
    ,"멕시코": "양식"
    ,"남미음식": "양식"
    ,"중식": "아시아음식"
    ,"중식당": "아시아음식"
    ,"곰탕": "한식"
    ,"설렁탕": "한식"
    ,"치킨": "한식"
    ,"닭강정": "한식"
    ,"요리주점": "카페및기타"
    ,"햄버거": "양식"
    ,"순대": "한식"
    ,"순대국": "한식"
    ,"전": "한식"
    ,"빈대떡": "한식"
    ,"국밥": "한식"
    ,"양꼬치": "아시아음식"
    ,"태국음식": "아시아음식"
    ,"돼지고기구이": "한식"
    ,"초밥": "아시아음식"
    ,"롤": "아시아음식"
    ,"샤브샤브": "한식"
    ,"소고기구이": "한식"
    ,"만두": "한식"
    ,"돈가스": "카페및기타"
    ,"곱창": "한식"
    ,"막창": "한식"
    ,"양": "한식"
    ,"스파게티": "양식"
    ,"파스타전문": "양식"
    ,"일식당": "아시아음식"
    ,"우동" : "아시아음식"
    ,"소바" : "아시아음식"
    ,"칼국수": "한식"
    ,"만두" : "한식"
    ,"다이어트": "카페및기타"
    ,"샐러드": "카페및기타"
    ,"아시아음식": "아시아음식"
    ,"아귀찜": "한식"
    ,"해물찜": "한식"
    ,"감자탕": "한식"
    ,"추어탕": "한식"
    ,"일본식라면": "아시아음식"
    ,"생선구이": "한식"
    ,"양갈비": "카페및기타"
    ,"국밥": "한식"
    ,"두부요리": "한식"
    ,"찌개": "한식"
    ,"전골": "한식"
    ,"돼지고기구이": "한식"
    ,"햄버거": "양식"
    ,"멕시코": "양식"
    ,"남미음식": "양식"
    ,"정육식당": "한식" 
    ,"육류": "한식"
    ,"고기요리" : "한식"
    ,"맥주": "카페및기타"
    ,"호프": "카페및기타"
    ,"국수": "한식"
    ,"닭갈비": "한식"
    ,"생선회": "아시아음식"
    ,"일식튀김": "아시아음식"
    ,"닭발": "한식"
    ,"술집": "카페및기타"
    ,"닭볶음탕": "한식"
    ,"떡볶이": "분식"
    ,"카페": "카페및기타"
    ,"대게요리": "기타"
    ,"피자": "양식"
    ,"양꼬치": "아시아음식"
    ,"백반": "한식"
    ,"가정식": "한식"
    ,"전": "한식"
    ,"빈대떡" : "한식"
    ,"닭발": "한식"
    ,"게요리": "카페및기타"
    ,"양식": "양식"
    ,"베이글": "카페및기타"
    ,"브런치": "카페및기타"
    ,"도넛": "카페및기타"
    ,"케이크": "카페및기타"
    ,"베이커리": "카페및기타"
    ,"케이크전문": "카페및기타"
    ,"스페인음식": "양식"
    ,"BAR": "카페및기타"
    ,"바": "카페및기타"
    ,"bar": "카페및기타"
    ,"딤섬": "아시아음식"
    ,"중식만두": "아시아음식"
    ,"일식튀김": "아시아음식"
    ,"꼬치": "아시아음식"
    ,"프랑스음식": "양식",
    "인도음식": "아시아음식",
    "터키음식": "아시아음식",
    "와인": "카페및기타",
    "아이스크림"  :"카페및기타" ,
    "카레" : "아시아음식",
    "카페": "카페및기타"
    ,"디저트" : "카페및기타"
    ,"차": "카페및기타"
    ,"뷔페": "카페및기타"
    ,"주꾸미요리": "한식"
    ,"이북음식": "한식"
    ,"프랑스음식": "양식"
    ,"홍차전문점": "카페및기타"
    ,"해물": "한식"
    ,"샌드위치": "카페및기타"
    ,"빙수": "카페및기타"
    ,"기사식당": "한식"
    ,"뷔페": "카페및기타"
    ,"매운탕": "한식"
    ,"스페인음식": "양식"
    ,"한정식":"한식"
    ,"바\(BAR\)": "카페및기타"
    ,"바닷가재요리": "양식"
    ,"백숙삼계탕": "한식"
    ,"페밀리레스토랑": "카페및기타"
    ,"아귀찜": "한식"
    ,"추어탕": "한식"
    ,"생선구이": "한식"
    ,"두부요리": "한식"
    ,"정육식당": "한식"
    ,"술집": "카페및기타"
    ,"닭볶음탕": "한식"
    ,"대게요리": "한식"
    ,"게요리": "한식"
    ,"민속주점" : "카페및기타"}

    # for문에서 사용하기 위해서 list로 담아줌(key값 : gubun)
    categoryDicList = list(categoryDic)

    # for문에서 사용하기 위해서 list로 담아줌(value값 : category)
    categoryDicReverse = list(categoryDic.values())

    # 카테고리 생성
    for j in range (0, len(feature_namesList)):
        for i in range (0, len(categoryDicList)):
            if (feature_namesList[j] == categoryDicList[i]):
                key = "string"
                keyReplace = key.replace("string",feature_namesList[j])
                value = categoryDic[keyReplace]
                df.loc[df["gubun"].str.contains(categoryDicList[i]), "category"] = value

    # 카테고리 분류 안된 Nan값 찾기 위해서 변수 생성
    findCategory = df.category

    # Nan값 찾기
    findNan = df.loc[((findCategory != "한식") & (findCategory != "양식") & (findCategory != "아시아음식") & (findCategory != "카페및기타"))]

    # Nan값 변경위해 gubun 리스트 생성
    findNanList = list(findNan.gubun)

    # Nan값 기타로 변경
    for i in range (0, len(findNanList)):
            findNan.loc[findNan["gubun"].str.contains(findNanList[i]), "category"] = "카페및기타"

    # 기존 데이터프레임에서 Nan값이 아닌 카테고리 찾기
    findNotNan = df.loc[~((findCategory != "한식") & (findCategory != "양식") & (findCategory != "아시아음식") & (findCategory != "카페및기타"))]

    # 데이터 합치기(기존, 기타)
    joinCatagory = pd.concat([findNan, findNotNan], axis=0, ignore_index=True)

    joinCatagory

    # 바(BAR)는 괄호때문에 인식을 못해서 따로 변경
    joinCatagory.loc[joinCatagory.gubun.str.contains("바\(BAR\)"),"category"] = "카페및기타"

    joinCatagory

    joinCatagory.category.drop_duplicates()

    joinCatagory["category"].value_counts()

    labelDict = joinCatagory.category.drop_duplicates().reset_index(drop=True).to_dict()

    labelDict

    labelDict = dict(map(reversed,labelDict.items()))

    labelDict

    joinCatagory.category.map(labelDict)

    joinCatagory["labelcode"] = joinCatagory.category.map(labelDict)

    return joinCatagory


def selectData(finalData, weightedData):
    
    finalWeighted = pd.merge(finalData,weightedData,on="name", how ="left")
    
    ##predict 0 부터 조회
    selectDatas = []

    for i in range(0,3):
        selectData = finalWeighted.loc[finalWeighted.predict == i]

        sortKey = ["score_weighted", "total_count"]

        asc = [False, True]

        selectData.sort_values(sortKey, ascending=asc, inplace=True)
        selectDatas.append(selectData.iloc[:5,:])
        
    return selectDatas




