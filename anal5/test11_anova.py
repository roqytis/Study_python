# 분산분석
# 강남구에 있는 GS편의점 3개 지점 알바생의 급여에 대한 평균에 차이가 있는지 검정하시오
# 귀무 : GS편의점 3개 지점 알바생의 급여에 대한 평균에 차이가 없다.
# 대립 : GS편의점 3개 지점 알바생의 급여에 대한 평균에 차이가 있다.

import numpy as np
import pandas as pd
import urllib.request
import scipy.stats as stats
from statsmodels.formula.api import ols 
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/group3.txt'
#data = pd.read_csv(url, header=None)
#print(data)

# numpy 이용해서 url 읽는 방법
data = np.genfromtxt(urllib.request.urlopen(url), delimiter=',')
print(data, type(data)) # <class 'numpy.ndarray'>
print(data.shape) # (22, 2) // 배열의 크기


# 세 개 지점(집단)의 월급 자료 얻기, 평균 확인
g1 = data[data[:, 1] == 1, 0]
g2 = data[data[:, 1] == 2, 0]
g3 = data[data[:, 1] == 3, 0]
print(g1, np.mean(g1)) # [243. 251. 275. 291. 347. 354. 380. 392.] 316.625 // 1집단 월급
print(g2, np.mean(g2)) # [206. 210. 226. 249. 255. 273. 285. 295. 309.] 256.44444444444446 // 2집단 월급
print(g3, np.mean(g3)) # [241. 258. 270. 293. 328.] 278.0 // 3집단 월급

# 정규성 확인
print(stats.shapiro(g1)) # pvalue=0.3336853086948395 > 0.05 이므로 만족
print(stats.shapiro(g2)) # pvalue=0.6561065912246704 > 0.05 이므로 만족
print(stats.shapiro(g3)) # pvalue=0.832481324672699 > 0.05 이므로 만족

# 등분산성 확인
print(stats.levene(g1, g2, g3)) # pvalue=0.045846812634186246
print(stats.bartlett(g1, g2, g3)) # pvalue=0.3508032640105389 > 0.05 이므로 만족. 표본의 개수가 적어 bartlett이 더 적당

# 데이터의 산포도(퍼점 정도) 시각화
plt.boxplot([g1, g2, g3], showmeans = True) # , notch = True 속성은 안 주는 게 더 예쁨
plt.show()

# 일원분산분석 방법1) linear 모델 사용 : anova_lm
df = pd.DataFrame(data, columns = ['pay', 'group'])
print(df)
lmodel = ols('pay ~ C(group)', df).fit() # C() : 범주형임을 표시
print(anova_lm(lmodel, typ = 1)) # pvalue : 0.043589
#             df        sum_sq      mean_sq         F    PR(>F)
# C(group)   2.0  15515.766414  7757.883207  3.711336  0.043589
# Residual  19.0  39716.097222  2090.320906       NaN       NaN

print()
# 일원분산분석 방법2) f_oneway() // 참고 : f_twoway()는 없음
f_statistic, p_value = stats.f_oneway(g1, g2, g3)
print('f_statistic : ', f_statistic) # 3.71335
print('p_value : ', p_value) # 0.043589 < 0.05 이므로 귀무가설 기각
# 결론 : GS편의점 3개 지점 알바생의 급여에 대한 평균에 차이가 있다.

# 사후 검정
from statsmodels.stats.multicomp import pairwise_tukeyhsd #비교대상 표본 수가 동일한 경우 사용
tukeyResult = pairwise_tukeyhsd(df.pay, df.group)
print(tukeyResult)
tukeyResult.plot_simultaneous(xlabel='mean', ylabel='group')
plt.show()