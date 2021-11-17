# 분산분석(ANOVA) : 종속변수의 변화폭이(분산)이 독립변수에 의해 기인 하는지를 파악하는 것
# 집단 간 분산이 집단 내 분산보다 충분히 큰 것인가를 파악,
#분산이 큰집단 / 분산이 작은집단, between variance/ within variance => f

# 세 개 이상의 모집단에 대한 가설검정 – 분산분석
# ‘분산분석’이라는 용어는 분산이 발생한 과정을 분석하여 요인에 의한 분산과 요인을 통해 나누어진 각 집단 내의 분산으로 나누고 
# 요인에 의한 분산이 의미 있는 크기를 크기를 가지는지를 검정하는 것을 의미한다.
# 세 집단 이상의 평균비교에서는 독립인 두 집단의 평균 비교를 반복하여 실시할 경우에 제1종 오류가 증가하게 되어 문제가 발생한다.
# 이를 해결하기 위해 Fisher가 개발한 분산분석(ANOVA, ANalysis Of Variance)을 이용하게 된다.

# * 서로 독립인 세 집단의 평균 차이 검정
# 실습) 세 가지 교육방법을 적용하여 1개월 동안 교육받은 교육생 80명을 대상으로 실기시험을 실시. three_sample.csv'
# 귀무가설 : 세가지 교육방법에 따른 시험점수 평균에 차이가 없다.
# 대립가설 : 세가지 교육방법에 따른 시험점수 평균에 차이가 있다.

import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols

data = pd.read_csv("../testdata/three_sample.csv")
print(data.head(3))
print(len(data))
print(data.info())
print(data.describe())

#시각화
import matplotlib.pyplot as plt
#plt.boxplot(data.score)
#plt.hist(data.score)
#plt.show()

data = data.query('score <= 100')
print(len(data))
#plt.boxplot(data.score)
#plt.hist(data.score)
#plt.show()

#선행조건
#독립성: 상관관계 등으로 확인
#등분산성
result = data[['method','score']]
#print(result)
m1 = result[result['method'] ==1]
m2 = result[result['method'] ==2]
m3 = result[result['method'] ==3]
score1 = m1['score']
score2 = m2['score']
score3 = m3['score']
print('등분산성 확인: ', stats.levene(score1,score2,score3).pvalue) # 0.113228 > 0.05 만족
# 등분산성 만족하지 못한 경우 welch_anova()를 사용

print(stats.shapiro(score1))
#정규성 : 집단 2개인 경우 stats.ks_2samp()
print('정규성 확인: ', stats.ks_2samp(score1, score2)) # pvalue=0.3096 > 0.05 이므로 마족
print('정규성 확인: ', stats.ks_2samp(score1, score3)) #pvalue=0.716 > 0.05 이므로 마족
print('정규성 확인: ', stats.ks_2samp(score1, score3)) #pvalue=0.7162 > 0.05 이므로 마족
#정규성을 만족하지 못한 경우 krskal-wallis test

print()
import statsmodels.api as sm
reg = ols("data['score'] ~ data['method']", data = data).fit()
print(reg)

table = sm.stats.anova_lm(reg, type = 2)
print(table)

