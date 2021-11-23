# 다항회귀 : 선형가정이 어긋날 때(비정규성) - 비선형 데이터에 대해 다항회귀 모델 작성

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model._base import LinearRegression


print()
# 다항회귀 모델 작성
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree = 2, include_bias = False) # degree = 열 갯수, include_bias = False 편향 X
# print(poly)
x2 = poly.fit_transform(x)
print(x2)

model2 = LinearRegression().fit(x2, y) # 특징 행렬값으로 학습
ypred2 = model2.predict(x2)
print(ypred2)

plt.scatter(x, y)
plt.plot(x, ypred2, c = 'red')
plt.show()