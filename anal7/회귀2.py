# 회귀분석 방법 확인
# 독립변수 : 연속향, 종속변수 : 연속형
# 두 변수는 상관관계가 있고 원인과 결과(인과) 관계가 있어야 한다.
# 기본 충족 조건 : 선형성, 잔차정규성, 잔차 독립성, 등분산성, 다중공산성
# 정량적인 모델을 생성

import statsmodels.api as sm
from sklearn.datasets import make_regression
import numpy as np

np.random.seed(12)

# 모델 맛보기
# 방법1 : make_regression을 사용
x, y, coef = make_regression(n_samples = 50, n_features = 1, bias = 100, coef = True)
print(x, x.shape)  # (50, 1) - matrix
print(y, y.shape)  # (50,) - vector
print(coef)   # 기울기
# 회귀식 y = coef * x + bias
y_pred = coef * 88.88 + 100
print('y_pred  :', y_pred )

xx = x
yy = y

print('------------------------')
# 방법2 : LinearRegression을 사용. 모델 생성 됨
from sklearn.linear_model import LinearRegression
model = LinearRegression()
fit_model = model.fit(xx, yy) # 학습데이터로 학습한 후 모델 추정 : 절편, 기울기 얻기
print(fit_model)
print(fit_model.coef_)
print(fit_model.intercept_)

y_new = fit_model.predict(xx[[0]])
print('y_new : ', y_new)
y_new = fit_model.predict([[66]])
print('y_new : ', y_new)

print('------------------------')
# 방법3 : LinearRegression을 사용. 모델 생성 됨
import statsmodels.formula.api as smf
import pandas as pd
print(xx.shape)
x1 = xx.flatten() # 자원 축소
print(x1.shape)
y1 = yy

data = np.array([x1, y1])
df = pd.DataFrame(data.T)
df.columns = ['x1', 'y1']
print(df.head(3))

model2 = smf.ols(formula = 'y1 ~ x1', data = df).fit()
print(model2.summary()) # 기울기(x1, coef) : 89.4743, 절편(Intercept, coef) : 100.0

# 예측값 확인
print(x1[:2]) # [-1.70073563 -0.67794537]
new_df = pd.DataFrame({'x1' : [-1.70073563, -0.67794537]})
new_pred = model2.predict(new_df)
print('new_pred(예측값) : ', new_pred) # new_pred(예측값) :  0   -112.830835
print('실제값 : ', df.y1[:2].values) # 실제값 :  [-52.17214291  39.34130801]

# 전혀 새로운 값 예측
new_df2 = pd.DataFrame({'x1' : [123, -2.3456]})
new_pred2 = model2.predict(new_df2)
print('new_pred2 : ', new_pred2)
