# 어느 음식점의 매출 데이터와 날씨 데이터를 활용하여 최고 온도에 따른 매출의 평균에 차이가 있는지 검정

# 원본소스는 data.go.kr
# 귀무 가설 : 매출액은 온도의 영향과 관련이 없다.
# 대립 가설 : 매출액은 온도의 영향과 관련이 있다.


import numpy as np
import scipy.stats as stats
import pandas as pd

# 매출 데이터 읽기

sales_data = pd.read_csv("../testdata/tsales.csv", \
                         dtype = {'YMD':'object'})
print(sales_data.head(3))
print(sales_data.info())

wt_data = pd.read_csv("../testdata/tweather.csv")
print(wt_data.head(3))
print(wt_data.info())


print()

# sales_data 날짜를 기준으로 join 하기위해 wt_data의 tm 칼럼을 변경 (2018-06-01 -> 20180601)

wt_data.tm = wt_data.tm.map(lambda x: x.replace('-',''))
print(wt_data.head(3))

print()
frame = sales_data.merge(wt_data, how = 'left', left_on='YMD', right_on = 'tm')
print(frame.head(5)) # 328 rows x 12 columns
print(frame.columns) # Index(['YMD', 'AMT', 'CNT', 'stnId', 'tm', 'avgTa', 'minTa', 'maxTa', 'sumRn','maxWs', 'avgWs', 'ddMes'],

data = frame.iloc[:, [0,1,7,8]]

print(data.head(3))
print(data.isnull().sum())

# 일별 최고 온도 -> 구간 설정(추움 : 0, 보통 : 1, 더움 : 2)
print(data.maxTa.describe())

# 시각화
import matplotlib.pyplot as plt
plt.boxplot(data.maxTa)
plt.show()

# 일별 최고 온도 -> 구간 설정(추움 : 0, 보통 : 1, 더움 : 2)
data['Ta_gubun'] = pd.cut(data.maxTa, bins = [-5, 8, 24, 37], labels = [0, 1, 2])
print(data.head(5))

# 상관관계 
print(data.corr()) # -0.660066 // 매출액과 온도는 음의 상관관계가 높다
#             AMT     maxTa     sumRn 
# AMT    1.000000 -0.660066 -0.080907
# maxTa -0.660066  1.000000  0.119268
# sumRn -0.080907  0.119268  1.000000

# 3그룹으로 매출액을 분리
x1 = np.array(data[data.Ta_gubun == 0].AMT) # 추울 때
x2 = np.array(data[data.Ta_gubun == 1].AMT) # 보통
x3 = np.array(data[data.Ta_gubun == 2].AMT) # 더울 때
print('x1 : ', x1[:10]) # x1 :  [1050500  770000 1054500  969000 1061500 1002000 1148500 1184500  994000 907500]
print('x2 : ', x2[:10]) # x2 :  [ 18000  50000 274000 203000 381500 295000 816500 993000 813500 754500]
print('x3 : ', x3[:10]) # x3 :  [     0 125000 222500 209000 302000 267000 179500 189500 240000 366500]

# 등분산성
print(stats.levene(x1, x2, x3)) # pvalue=0.039002396565063324 < 0.05 이므로 등분산성 만족 X

# 정규성
print(stats.ks_2samp(x1, x2).pvalue) # 9.28938415079017e-09 < 0.05 이므로 정규성 만족 X
print(stats.ks_2samp(x1, x3).pvalue) # 1.198570472122961e-28 < 0.05 이므로 정규성 만족 X
print(stats.ks_2samp(x2, x3).pvalue) # 1.4133139103478243e-13 < 0.05 이므로 정규성 만족 X

# 평균 보는 법1
spp = data.loc[:, ['AMT', 'Ta_gubun']]
print(spp.groupby('Ta_gubun').mean())
#                    AMT
# Ta_gubun              
# 0         1.032362e+06
# 1         8.181069e+05
# 2         5.537109e+05

# 평균 보는 법2
print(np.mean(x1)) # 1032362.3188405797
print(np.mean(x2)) # 818106.8702290077
print(np.mean(x3)) # 553710.9375

# 평균 보는 법3
print(pd.pivot_table(spp, index = ['Ta_gubun'], aggfunc = 'mean'))
#                    AMT
# Ta_gubun              
# 0         1.032362e+06
# 1         8.181069e+05
# 2         5.537109e+05

sp = np.array(spp)
group1 = sp[sp[:, 1] == 0, 0]
group2 = sp[sp[:, 1] == 1, 0]
group3 = sp[sp[:, 1] == 2, 0]

plt.boxplot([group1, group2, group3])
plt.show()

# 분산분석
print(stats.f_oneway(group1, group2, group3)) # pvalue 2.360737101089604e-34 < 0.05 이므로 귀무가설 기각
# 결론 : 매출액은 온도의 영향과 관련이 있다.

# 정규성 만족 X
print(stats.kruskal(group1, group2, group3)) # pvalue 1.5278142583114522e-29

# 등분산성 만족 X
# 아나콘다에서 설치 pip install pingouin
from pingouin import welch_anova
print(welch_anova(data = data, dv = 'AMT', between = 'Ta_gubun'))

# 사후 분석
from statsmodels.stats.multicomp import pairwise_tukeyhsd
result = pairwise_tukeyhsd(spp['AMT'], spp['Ta_gubun'], alpha = 0.05)
print(result)

result.plot_simultaneous()
plt.show()