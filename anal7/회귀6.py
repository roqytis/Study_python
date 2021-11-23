# 선형회귀의 충족 조건

import statsmodels.formula.api as smf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family="malgun gothic")

advdf = pd.read_csv('../testdata/Advertising.csv', usecols=[1, 2, 3, 4])
print(advdf.head(3), ' ', advdf.shape) # (200, 4)

print(advdf.index, advdf.columns)
print(advdf.info())

print(advdf.loc[:, ['sales', 'tv']].corr()) # 0.782224 // 강한 양의 상관관계

# 모델 생성
# lm = smf.ols(formula='sales ~ tv', data=advdf)
# lm_model = lm.fit()
lm = smf.ols(formula='sales ~ tv', data=advdf).fit() # fit() : 데이터 학습
print(lm.summary()) # R-squared:                       0.612
print(lm.pvalues) # Intercept    1.406300e-35
print(lm.rsquared) # tv           1.467390e-42

print()
# 시각화
import seaborn as sns
# plt.scatter(advdf.tv, advdf.sales)
# plt.xlabel('tv')
# plt.ylabel('판매량')
# x = pd.DataFrame({'tv':[advdf.tv.min(), advdf.tv.max()]})
# y_pred = lm.predict(x)
# plt.plot(x, y_pred, c='r') # 선 긋기
# plt.show()

# 예측 : 새로운 tv 값으로 sales를 예측
x_new = pd.DataFrame({'tv':[230.0, 45.5, 100.1]})
pred = lm.predict(x_new)
print('예측 값 : ', pred)

print()
# 다중 선형 회귀
print(advdf.corr())

lm_mul = smf.ols(formula='sales ~ tv + radio + newspaper', data=advdf).fit()
# lm_mul = smf.ols(formula='sales ~ tv + radio', data=advdf).fit()
print(lm_mul.summary()) # newspaper는 모델의 성능에 영향을 주지 않으므로 빼는 게 좋겠다.

# 예측2 : 새로운 tv 값으로 sales를 예측
x_new2 = pd.DataFrame({'tv':[230.0, 45.5, 100.1], 'radio':[30.0, 40.5, 50.1], 'newspaper':[10.0, 5.5, 4.1]})
pred2 = lm.predict(x_new2)
print('예측 값 : ', pred2)

print('선형회귀분석모형의 적절성 확인 : 정규성, 독립성, 선형성, 등분산성, 다중공선성 -------------')
# 잔차항(실제값 - 예측값) 구하기 // 잔차 제곱이 최소가 되는 선 : 회귀선
fitted = lm_mul.predict(advdf) # 예측값
residual = advdf['sales'] - fitted # 실제값 - 예측값

print('선형성 : 예측값과 잔차가 비슷한 패턴을 가짐')
sns.regplot(fitted, residual, line_kws = {'color' : 'red'}, lowess = True)
plt.plot([fitted.min(), fitted.max()], [0, 0], '--', color='grey')
plt.show() # 선형성을 완전하게 만족하지는 못 함

print('정규성 : 잔차가 정규분포를 따라야 함. Q-Q plot 사용')
import scipy.stats
sr = scipy.stats.zscore(residual)
(x, y), _ = scipy.stats.probplot(sr)
sns.scatterplot(x, y)
plt.plot([-3, 3], [-3, 3], '--', color = 'gray')
plt.show() # 정규성을 완전하게 만족하지는 못 함

print('shapiro test : ', scipy.stats.shapiro(residual)) # pvalue=3.938041004403203e-09 < 0.05 정규성 만족 못 함

print('독립성 : 잔차가 독립적. 자기상관(인접 관측치와 오차가 상관되어 있음)이 없어야 함')
# 더빈왓슨 값으로 확인 : Durbin-Watson:                   2.084 (0에 가까우면 양의 상관, 4에 가까우면 음의 상관. 2에 가까우면 자기상관이 없다.) -> 독립성은 만족

print('등분산성 : 잔차의 분산이 일정')
sns.regplot(fitted, np.sqrt(np.abs(sr)), lowess = True, line_kws = {'color' : 'red'})
plt.show() # 등분산성 만족 못 함. 이상치 확인. 정규성, 선형성 확인

print('다중 공선성 : 독립변수들 간에 강한 상관관계가 있는 경우')
# VIF(분산 인플레 요인) 값이 10을 넘으면 다중 공선성 발생
from statsmodels.stats.outliers_influence import variance_inflation_factor
vifdf = pd.DataFrame()
vifdf['vif_value'] = [variance_inflation_factor(advdf.shape[1], i) for i in range(advdf.shape[1])]
print(vifdf) # 
