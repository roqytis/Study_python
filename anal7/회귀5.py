# 선형회귀 분석 : mtcars dataset 사용
import statsmodels.api
import statsmodels.formula.api as smf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family = 'malgun gothic')

mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data
print(mtcars)

print(mtcars.columns) # ['mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear','carb'],
print(np.corrcoef(mtcars.hp, mtcars.mpg)) # r : -0.77616837
print(np.corrcoef(mtcars.wt, mtcars.mpg)) # r : -0.86765938
#print(mtcars.corr())

# 시각화
plt.scatter(mtcars.hp, mtcars.mpg)
slope, intercept = np.polyfit(mtcars.hp, mtcars.mpg, deg=1)  # numpy로 기울기, 절편 얻기
# 회귀식을 표시
plt.plot(mtcars.hp, slope * mtcars.hp + intercept, 'r') # wx + b => slope * x + intercept
plt.xlabel('마력수')
plt.ylabel('연비')
plt.show()

print('단순 선형회귀 ------')
result = smf.ols('mpg ~ hp', data = mtcars).fit()
print(result.summary()) # 모델에 대한 p-value : 1.79e-07 < 0.05 이므로 모델은 의미가 있음
# R-squared: 0.602
# slope : -0.0682, Intercept(bias) : 30.0989
print('마력수 110에 대한 연비는 ', -0.0682 * 110 + 30.0989) # 22.5969
print('마력수 50에 대한 연비는 ', -0.0682 * 50 + 30.0989) # 26.6889
# 마력이 증가하면 연비는 줄어든다. 음의 상관관계이므로 결과는 반비례한다.

print('다중 선형회귀 ---------')
result2 = smf.ols('mpg ~ hp + wt', data = mtcars).fit()
print(result2.summary()) # 모델에 대한 p-value : 9.11e-12 < 0.05 이므로 모델은 의미가 있음
# Adj. R-squared: 0.815
# hp_slope : -0.0318, wt_slope : -3.8778, Intercept(bias) : 37.2273
print('마력수 110과 차체무게 5에 대한 연비는 ', (-0.0318 * 110) + (-3.8778 * 5) + 37.2273) # w1x1 + w2x2 + b
# 마력수 110과 차체무게 5에 대한 연비는  14.3403

print('\npredict() 메소드로 예측 --- 자체 무게를 입력해 연비를 추정하기')
result3 = smf.ols('mpg ~ wt', data = mtcars).fit()
print(result3.summary())
print('결정계수(설명력) : ', result3.rsquared)
pred = result3.predict()  # mtcars.wt 전체로 예측 결과 반환
print('예측값 : ', pred[0])
print('시렞값 : ', mtcars.mpg[0])

# 전체 예측값 실제값 보기
data = {
    '실제 mpg':mtcars.mpg,
    '예측 mpg':pred
}
df = pd.DataFrame(data)
print(df)

print(df)
# 새로운 차체 무게로 연비 추정하기
'''
mtcars.wt = float(input('차체 무게 입력: '))
new_pred = result3.predict(pd.DataFrame(mtcars.wt))
print('차체 무게 {}일 때 예셩연비는 {}'.format(mtcars.wt[0], new_pred[0]))
'''

print()
# 참고 : 차체 무게 여러 개
new_wt = pd.DataFrame({'wt':[6, 3, 0.5]})
new_pred2 = result3.predict(new_wt)
print('예상연비 : \n', new_pred2)
print('예상연비 : \n', np.round(new_pred2.values, 2))