# 선형회귀 : LinearRegression
import statsmodels.api

mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data

print(mtcars[:3])

from sklearn.linear_model import LinearRegression

x = mtcars[['hp']].values
y = mtcars[['mpg']].values
print(x[:3])
print(y[:3])

import matplotlib.pyplot as plt
# plt.scatter(x, y)
# plt.show()

fit_model = LinearRegression().fit(x, y)
print('기울기 : ', fit_model.coef_[0])
print('절편 : ', fit_model.intercept_)
#fit_model.summary()
pred = fit_model.predict(x)
print('예측값 : ', pred[:3])
print('실제값 : ', y[:3])
'''
예측값:  
[[22.59374995]
 [22.59374995]
 [23.75363068]]
실제값:  
[[21. ]
 [21. ]
 [22.8]]'''