# 선형회귀 분석 : mtcars dataset 사용
import statsmodels.api
import statsmodels.formula.api as smf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family = 'malgun gothic')

mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data
print(mtcars)
print(mtcars.columns)
print(np.corrcoef(mtcars.hp, mtcars.mpg)) # -0.776 / 마력수 커지면 연비는 줄어듦
print(np.corrcoef(mtcars.wt, mtcars.mpg)) # -0.867 / 차가 무거우면 연비는 줄어듦 numpy로 상관계수 판단
#print(mtcars.corr()) # pandas로 상관계수 판단

'''
# 데이터의 퍼짐 정도 시각화
plt.scatter(mtcars.hp, mtcars.mpg) # 실제 값으로 산포도 표시
slope, intercept = np.polyfit(mtcars.hp, mtcars.mpg, deg=1)
# polyfit : numpy를 이용하여 기울기, 절편을 얻음 (회귀식 생성됨) / deg는 차원
# 회귀식을 화면에 표시
plt.plot(mtcars.hp, slope*mtcars.hp + intercept, 'r') # Wx + B -> slope * x + intercept / 예측 값으로 산포도 표시
plt.xlabel('마력수')
plt.ylabel('연비')
plt.show()
# 연비와 마력수 데이터 퍼짐 정도 시각화
'''

print('---------- 단순 선형 회귀 ----------')
result = smf.ols('mpg ~ hp', data=mtcars).fit()
print(result.summary()) # R-squared: 0.602 / 모델에 대한 p-value Prob (F-statistic): 1.79e-07 < 0.05 이므로 유의한 모델
# slope = -0.0682 / bias(Intercept) = 30.0989. 기울기 / 절편
print('마력수 110에 대한 연비는 ', -0.0682 *110 +30.0989) # 22.59
print('마력수 50에 대한 연비는 ', -0.0682 *50 +30.0989) # 26.68 -> 마력수가 떨어져 연비가 상승
# 마력이 증가하면 연비는 줄어든다. 음의 상관관계이므로 결과는 반비례한다.
# 결과를 맹신하지 말고 의사결정에 참고하는 자료로 사용한다.

print('\n---------- 다중 선형 회귀 ----------')
result2 = smf.ols('mpg ~ hp + wt', data=mtcars).fit()
print(result2.summary()) # 모델에 대한 p-value : 9.11e-12 < 0.05 이므로 유의한 모델
# 수정된 결정력 Adj. R-squared: 0.815 (독립변수가 두개 이상일 때 사용)
# hp slope : -0.0318 , wt slope : -3.8778, bias(Intercept) = 37.2273
print('마력수 110과 차체무게 5에 대한 연비는 ', (-0.0318 *110) + (-3.8778*5) +37.2273) # w1x1 + w2x2 + b = 14.3403