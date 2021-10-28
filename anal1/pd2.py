# DataFrame : 표 모양의 자료구조

from pandas import Series,DataFrame

data = {
    'irum':['홍길동','한국인', '신기해', '공기밥','한가해'],
    'juso':('역상동', '신당동','역삼동','역삼동','신사동'),
    'nai':[23,25,33,32,35]
}

print(data, type(data))

frame = DataFrame(data)
print(frame, type(frame)) #<class 'pandas.core.frame.DataFrame'>

print(frame['irum'])
print(frame.irum)
print(type(frame.irum))

print()
frame2 = DataFrame(data,columns=['irum','nai','juso','tel'], index = ['a','b','c','d','e'])

print(frame2)
frame2['tel'] = '111-1111'
print(frame2)

val = Series(['222-2222','333-3333','444-4444'], index = ['b','c','e'])
frame2['tel'] = val
print(frame2)
print(frame.T) #전치
print()
print(frame2.values)
print(frame2.values[0,1])
print(frame2.values[0:2])

print()
#frame3 = frame2.drop('d')
frame3 = frame2.drop('d', axis =0) #axis = 0 : 행, axis = 1열
print(frame3)

frame4 = frame2.drop('tel', axis = 1)
print(frame4)

print()
print(frame2)
print(frame2.sort_index(axis = 0, ascending = False))
print(frame2.sort_index(axis = 1, ascending = True))

print()
print(frame2['juso'].value_counts())

print()
data = {
     'juso':('강남구 역삼동','중구 신당동','강남구 신사동'),
     'inwon':[23,25,33]
}

fr = DataFrame(data)
print(fr)

result1 = Series([x.split()[0] for x in fr.juso])
print(result1, result1.value_counts())

print('재색인')
data = Series([1,3,2], index = (1,4,2))
print(data)
data2 = data.reindex((1,2,4))
print(data2)

data3 = data2.reindex([0,1,2,3,4,5])
print(data3)

print(data2.reindex([0,1,2,3,4,5]))
print()
print(data2.reindex([0,1,2,3,4,5], fill_value= 777)) #method ='pad'
print()
print(data2.reindex([0,1,2,3,4,5], method = 'ffill')) #method ='backfill'

print('-----DataFrame-----------------')
import numpy as np

df = DataFrame(np.arange(12).reshape(4,3), index = ['1월','2월','3월','4월'], columns = ['강남', '강북','서초'])
print(df)
print(df['강남'] > 3)
print(df[df['강남'] > 3])

print('DataFrame 슬라이싱 관련 메소드 loc(): 라벨지원, iloc():인덱스 지원')
print(df.loc['3월', :])
print(df.loc['3월', :])
print(df.loc['3월', ['서초']]) # 2월 이하 행 서초 열

print()
print(df.iloc[2])
print(df.iloc[:2])
print(df.iloc[:3, 1:3]) #3행 미만 , 1 ,2, 열 출력 

#연산
df1 = DataFrame(np.arange(9).reshape(3,3), columns = list('kbs'))
print(df1)
df2 = DataFrame(np.arange(12).reshape(4,3), columns = list('kbs'))
print(df2)

print()
print(df1 + df2)
print(df1.add(df2, fill_value = 0))

print('------------------')
df = DataFrame([[1.4,np.nan], [7, -4.5], [np.NaN, np.NAN],[0.5, -1]], columns = ['one','two'])
print(df)

print(df.drop(1)) #행삭제
print(df.dropna()) #아래와 동일
print(df.dropna(how= 'any')) # Nan이 하나라도 있는 행은 삭제
print(df.dropna(how= 'all')) # 모든 값이 NaN이 있는 행은 삭제 
print(df.dropna(subset= ['one'])) # 'one'열 값 중에 NaN이 있는 행은 삭제

print()
print(df.sum())
print(df.sum(axis = 1))

print(df.describe())
print(df.info())

#//////////////////////////////////////////////////////////////////
print('------------------------------')
'''
pandas 문제 1)
  a) 표준정규분포를 따르는 9 X 4 형태의 DataFrame을 생성하시오. 
     np.random.randn(9, 4)
  b) a에서 생성한 DataFrame의 칼럼 이름을 - No1, No2, No2, No4로 지정하시오
  c) 각 컬럼의 평균을 구하시오. means() 함수와 axis 속성 사용
'''
import pandas as pd
df1 = pd.DataFrame(np.random.randn(9,4), columns= ['No1','No2','No3','No4'])
print(df1)
print(df1.mean(axis = 0))

print('------------------------------')

#pandas 문제 2)
#a) DataFrame으로 위와 같은 자료를 만드시오. 컬럼 이름은 numbers, 로우 네임은 a~d, 값은 10~40
df2 = pd.DataFrame([[i] for i in range(10,41,10)],
                   columns = ['numbers'], index = ['a','b','c','d'])
print(df2)
#b) c 로우의 값을 가져오시오.
print(df2.loc['c'])
#c) a, d 로우들의 값을 가져오시오.
print(df2.loc[['a','d']])
#d) numbers의 합을 구하시오.
print(df2.numbers.sum())
#e) numbers의 값들을 각각 제곱하시오 아래 결과가 나와야 함
print(df2 ** 2)

# f) floats 라는 이름의 칼럼을 추가하시오. 값은 1.5, 2.5, 3.5, 4.5
df2['floats']= [1.5,2.5,3.5,4.5]
print(df2)

df2['names'] = pd.Series(['길동','오정','팔계','오공'], index = ['d','a','b','c'])
print(df2)