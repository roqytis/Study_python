#차이분석 중 두 집단 평균차이 검저-
# *서로 독립인 두 집단의 평균 차이 검저(independent samples t-test : 독립표본 t검정)
# 남녀의 성적, A반과 B반의 키, 경기도와 충청도의 소득 따위의 서로 독립인 두 집단에서 얻은 표본을 독립표본(two sample)이라고 한다.

from scipy import stats
import pandas as pd
from numpy import mean, average

#실습) 남녀 두 집단 간 파이썬 시험의 평균 차이 검정
male = [75, 85, 100,72.5,86.5] 
female = [63.2, 76, 52, 100, 70]
# 귀무 : 남녀 두 집단 간 파이썬 시험의 평균에 차이가 없다
# 대립 : 남녀 두 집단 간 파이썬 시험의 평균에 차이가 있따.

print(average(male)) #83.8
print(average(female)) #72.24 11.5정도의 차이가 95% 신뢰구간에서 우연히 발생할 롹률이 5%이상이면 귀무채택

#두개의 표본 데이터로 t검정 실시 
two_sample = stats.ttest_ind(male,female)
print(two_sample) #pvalue=0.2525076 > 0.05 이면 이건 우연이다 귀무가설 채택
#Ttest_indResult(statistic=1.233193127514512, pvalue=0.25250768448532773)
print('---------------------------------------------------------------------------')
# 실습) 두가지 교육방법에 따른 평균시험 점수에 대한 검정 수행 two_sample.csv

data = pd.read_csv("../testdata/two_sample.csv")
print(data.head(3))
print(data.info())
ms = data[['method','score']]
print(ms)
# 교육 방법
m1 = ms[ms['method'] == 1]
m2 = ms[ms['method'] == 2]
print(m1)
print(m2)
score1 = m1['score'] #얘는 nan이 없고
score2 = m2['score'] # 얘는 nan이 2개있다
print(score1.isnull().sum())
print(score2.isnull().sum())

#sco2 = score2.dropna() #nan 제거 
#sco2 = score2.fillna(0) #nan 0으로 채우기

sco1 = score1.fillna(score1.mean())
sco2 = score2.fillna(score2.mean())

#시각화
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(sco1, kde = True, color='r')
sns.histplot(sco2, kde = True)
plt.show()

#정규성 test
print('sco1 정규성 :', stats.shapiro(sco1)) #pvalue=0.3679903 > 0.05 정규성 만족
print('sco2 정규성 :', stats.shapiro(sco2)) #pvalue=0.67141896> 0.05 정규성 만족

#등분산성 : 두 정기분포의 분산모수가 같은지 확인 0.5qhek zmaus whgek
print(stats.levene(sco1,sco2))
print(stats.levene(sco1,sco2).pvalue)
print(stats.fligner(sco1,sco2))
print(stats.bartlett(sco1,sco2))

#t-test 독립검정
result = stats.ttest_ind(sco1,sco2,equal_var = True) #등분산성 만족
print(result)
#Ttest_indResult(statistic=-0.19649386929539883, pvalue=0.8450532207209545) >0.05 귀무 채택
#두가지 교육방법에 따른 평균 시험 점수에 차이가 없다.

#참고 : 정규성을 만족하지 못한 경우 
#print(stats.wilcoxon(sco1,sco2)) #valueError : the samples x and y must have the same length
print(stats.mannwhitneyu(sco1, sco2))
