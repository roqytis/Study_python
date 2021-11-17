#교차분석(카이제곱 분석) :범주형 변수 간의 상관관계를 검정
#카이제곱 : 합(관측값 - 기대값)**2 /기대값
#독립변수:범주형, 종속변수 :범주형
#데이터나 집단의 분산을 추정하고 검정할 때 사용
# 독립성 검정 : 범주형 변수간의 관련성 여부 확인
# 적합도 검정 : 데이터가 특정한 분포에서 추출된 것인가를 알고자 할 때
# 동질성 검정 : 번주형 변수 간의 다항분포가 동일한 지 여부 확인

import pandas as pd
data = pd.read_csv("../testdata/pass_cross.csv", encoding='EUC-KR')
print(data.head(3))
#귀무가설 : 벼락치기 공부하는 것과 합격여부는 관계가 없다.
#대립가설 : 벼락치기 공부하는 것과 합격여부는 관계가 있다.

print()
print(data.shape[0]) #행수 50행
print(data.shape[1]) #열수  4열

print(data[(data['공부함']==1) & (data['합격'] == 1)].shape[0]) #18
print(data[(data['공부함']==1) & (data['불합격'] == 1)].shape[0]) #7

#빈도표
#data2 = pd.crosstab(index = data['공부함'],columns = data['합격'], margins=True)
data2 = pd.crosstab(index = data['공부안함'],columns = data['불합격'], margins=True)
print(data2)
dfree = (2-1)*(2-1) # 1
print('자유도 :',dfree)
print(25*20/50)
print(25*30/50)

chi2 = (18-15)**2 / 15 + (7-10) ** 2 / 10 +(12-15) **2/15 +(13 -10)** 2/10
print('검정통계량 중 카이제곱 값: ', chi2) #3.0

# 임계값 - 카이제곱표 이용 3.84
#결론 : 카이제곱 값 3.0 < 임계치 3.84이므로 채택역 내에 존재. 귀무가설 채택
#벼락치기 공부하는 것과 합격여부는 관계가 없다. 연구자가 수집한 데이터는 우연히 발생했다.

#scipy모듈 사용
import scipy.stats as stats
chi2, p, _,_ = stats.chi2_contingency(data2)
print('chi2:{}, p값:{}'.format(chi2,p)) #chi2:3.0, p값:0.5578254003710748
#결론 : p값(유의확률): 0.5578254003710748 > 0.05(유의수준) 이므로 귀무가설 채택.
#걍 0.05보다 크면 귀무가설 채택
#보고서 양식에 맞춰 보고서를 작성