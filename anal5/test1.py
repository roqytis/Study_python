#기술통계 : 자료를 정리 및 요약하는 기초적 통계
#중심경향값, 산포도, 부포도(왜도,첨도)
# 요약 통계량, 도수분포표 를 출력 ...

#돗수분포표 : 특정 구간에 속하는 자료의 수를 나타낸 표(빈도표)
import pandas as pd

frame = pd.read_csv('../testdata/ex_studentlist.csv') #csv폴더 읽어오기
print(frame.head(2))
print(frame.shape)
print(frame.info())
print(frame['age'].mean()) #평균
print(frame['age'].var())  #분산
print(frame['age'].std())  #표준편차
print(frame.describe()) #4분위
print(frame['bloodtype'].unique()) #['O' 'AB' 'B' 'A'] 

#bloodtype 빈도
data1 =frame.groupby(['bloodtype'])['bloodtype'].count()
print(data1)

# one - way table
data2 = pd.crosstab(index = frame['bloodtype'],columns = 'count')
#A              3
#AB             3
#B              4
#O              5
print(data2)

print()
# two-way table
data3 = pd.crosstab(index = frame['bloodtype'],columns = frame['sex'], margins=True)
print(data3)
