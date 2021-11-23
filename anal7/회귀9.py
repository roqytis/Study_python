# 보스톤 집 값 데이터로 다항회귀 분석
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics._regression import r2_score
import matplotlib.pyplot as plt
plt.rc('font', family = 'malgun gothic')

df = pd.read_csv('../testdata/housing.data', header=None, sep='\s+')
df.columns = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']
print(df.head(2))
print(df.corr())

x = df[['LSTAT']].values # LinearRegression이 독립은 2차원, 종속은 1차원을 원함
y = df['MEDV'].values
model = LinearRegression()

# 다항 특성
quad = PolynomialFeatures(degree = 2)
cubic = PolynomialFeatures(degree = 3)
x_quad = quad.fit_transform(x)
x_cubic = cubic.fit_transform(x)
print(x_quad[:3])
# [[ 1.      4.98   24.8004]
#  [ 1.      9.14   83.5396]
#  [ 1.      4.03   16.2409]]
print(x_cubic[:3])
# [[  1.         4.98      24.8004   123.505992]
#  [  1.         9.14      83.5396   763.551944]
#  [  1.         4.03      16.2409    65.450827]]

print()
# 단순회귀
x_fit = np.arange(x.min(), x.max(), 1)[:, np.newaxis]
model.fit(x, y)
y_lin_fit = model.predict(x_fit)
model_r2 = r2_score(y, model.predict(x)) # 실제값, 예측값으로 결정계수 얻기
print('model_r2 : ', model_r2) # model_r2 :  0.5441462975864797

# 다항회귀 degree = 2
model.fit(x_quad, y)
y_quad_fit = model.predict(quad.fit_transform(x_fit))
q_r2 = r2_score(y, model.predict(x_quad))
print('q_r2 : ', q_r2) # q_r2 :  0.6407168971636612

# 다항회귀 degree = 3
model.fit(x_cubic, y)
y_cubic_fit = model.predict(cubic.fit_transform(x_fit))
c_r2 = r2_score(y, model.predict(x_cubic))
print('c_r2 : ', c_r2) # c_r2 :  0.657847640589572

# 시각화
plt.scatter(x, y, label = 'train data', c = 'gray')
plt.xlabel('인구의 낮은 백분율')
plt.ylabel('주택가격')
plt.plot(x_fit, y_lin_fit, linestyle=':', label='선형회귀', c = 'b')
plt.plot(x_fit, y_quad_fit, linestyle='-', label='비선형회귀1', c = 'r')
plt.plot(x_fit, y_cubic_fit, linestyle='--', label='비선형회귀2', c = 'g')

plt.legend()
plt.show()