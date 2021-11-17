# -*- coding: utf-8 -*-
"""test1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WFUwOsIRn0rp_YEBJJ7YshrDd8ihIFIr
"""



import pandas as pd
import matplotlib.pyplot as plt
import urllib.request
from gensim.models.word2vec import  Word2Vec
#!pip install konlpy
from konlpy.tag import Okt

urllib.request.urlretrieve("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/ratings.txt", 
                           filename='rating.txt')
train_data = pd.read_table('rating.txt', error_bad_lines=False)
print(train_data[:5])
print(len(train_data))
print(train_data.isnull().values.any())

#정규표현식으로 한글 데이터만 얻기
train_data['document']= train_data['document'].str.replace('[^ㄱ - 하 - | 가-힣 ]','')
print(train_data[:50])

# 불용어(의미가 없는 단어)를 설정 후 토큰처리시 불용어 제거
stopwords = ['의', '이', '가', '은', '을', '들', '좀', '잘', '과', '와', '도', '에', '한', '으로', '부터'] # 불용어로 쓸 단어를 list로 설정
okt = Okt()
tokenized_data = [] # list 타입 준비
for sentence in train_data['document']:
  temp_x = okt.morphs(sentence, stem= True) # 모든 품사를 꺼냄. stem= True : 용언 처리
  temp_x = [word for word in temp_x if not word in stopwords] # 불용어 제거
  tokenized_data.append(temp_x)

# 리뷰 길이 확인
print(tokenized_data) # 위에서 용언처리된 단어들이 출력됨
print('리뷰의 최대 길이 :', max(len(l) for l in tokenized_data))
print('리뷰의 평균 길이 :', sum(map(len,tokenized_data))/ len(tokenized_data))

plt.hist([len(s) for s in tokenized_data], bins = 50)
plt.xlabel('length of samples')
plt.ylabel('number of samples')
#plt.show()

model = Word2Vec(sentences = tokenized_data, size=100 , window=5, workers=2, sg=0)
# 단어들을 벡터로 변환. workers = cpu개수 window = 주변 단 print(model.wv.vectors.shape) # (2879, 100)
print(model.wv.vectors.shape) # (2879, 100)
print(model.wv.vectors.shape)
print(model.wv.most_similar('한석규'))
print(model.wv.most_similar('히어로'))

'''
#!pip install kss
import kss
text='서울 등 수도권에도 집중호우가 내리는 곳이 있겠습니다. 이번 비는 내일 들어 대부분 그치겠습니다. 그러나 대부분 지역에는 무더위가 시작되겠습니다.'
print(kss.split_sentences(text))
'''