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

import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols

data = pd.read_csv('../testdata/three_sample.csv')
print(data.head(3))
print(len(data))
print(data.info())
print(data.describe())

# 시각화
import matplotlib.pyplot as plt
# plt.boxplot(data.score)
# plt.hist(data.score)
# plt.show()

data = data.query('score <= 100')
print(len(data)) # 78명
# plt.boxplot(data.score)
# plt.hist(data.score)
plt.show()

# 선행 조건
# 독립성 : 상관관계 등으로 확인
# 등분산성
result = data[['method', 'score']]
# print(result)
m1 = result[result['method'] == 1]
m2 = result[result['method'] == 2]
m3 = result[result['method'] == 3]
score1 = m1['score']
score2 = m2['score']
score3 = m3['score']
print('등분산성 확인 : ', stats.levene(score1, score2, score3).pvalue) # 등분산성 확인 :  0.11322850654055751 > 0.05 이므로 등분산성 만족
# 등분산성을 만족하지 못 한 경우 welche_anova()를 사용

print(stats.shapiro(score1))
# 정규성 : 집단 2개인 경우 stats.ks_2samp()
print('정규성 확인 : ', stats.ks_2samp(score1, score2)) # pvalue=0.3096879629846001 > 0.05 이므로 만족
print('정규성 확인 : ', stats.ks_2samp(score1, score3)) # pvalue=0.7162094473752455 > 0.05 이므로 만족
print('정규성 확인 : ', stats.ks_2samp(score2, score3)) # pvalue=0.7724081666033108 > 0.05 이므로 만족
# 정규성을 만족하지 못한 경우 kruskal-wallis test
# 정규성을 만족하지 못한 경우 데이터를 가공하는 방법도 있다. - 표준화, 정규화, log를 적용 ...


print()
import statsmodels.api as sm
reg = ols("data['score'] ~ data['method']", data = data).fit()
print(reg) # <statsmodels.regression.linear_model.RegressionResultsWrapper object at 0x000001DF274F4A00>

table = sm.stats.anova_lm(reg, type = 2)
print(table) # F : 검정 통계량 F 값 / PR : Pvalue
#                   df        sum_sq     mean_sq         F    PR(>F)
# data['method']   1.0     27.980888   27.980888  0.122228  0.727597
# Residual        76.0  17398.134497  228.922822       NaN       NaN

# 결론 : 세 가지 교육 방법에 따른 시험 점수 평균에 차이가 없다. (pvalue 0.727597 > 0.05 이므로 귀무가설 채택)

# ANOVA는 전체 그룹 간의 평균 값 차이가 의미가 있는지만 판단해 줌
# 그룹 간의 평균의 차이를 구체적으로 알고 싶은 경우에는 사후 분석(Post Hoc Test)을 함

from statsmodels.stats.multicomp import pairwise_tukeyhsd # 비교대상 표본 수가 동일한 경우 사용
tukeyResult = pairwise_tukeyhsd(data.score, data.method)
print(tukeyResult)
# group1 group2 meandiff p-adj  lower   upper  reject
# ---------------------------------------------------
#      1      2   0.9725   0.9  -8.946  10.891  False // 유의미한 차이가 있으면 True 없으면 False (결론은 세 가지 교육 방법에 따른 시험 점수 평균에는 차이가 없어서 False)
#      1      3   1.4904   0.9 -8.8184 11.7992  False
#      2      3   0.5179   0.9 -9.6127 10.6484  False
# --------------------------------------------------- 

# 결과를 시각화
tukeyResult.plot_simultaneous(xlabel = 'mean', ylabel = 'group')
plt.show()