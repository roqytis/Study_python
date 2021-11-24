# 회귀분석을 위한 몇 가지 모델 사용
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor # 회귀를 목적으로 사용
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score

adver = pd.read_csv('../testdata/Advertising.csv', usecols = [1, 2, 3, 4])
print(adver.head(2))
print(adver.corr())

x = np.array(adver.loc[:, 'tv':'newspaper'])
y = np.array(adver.sales)
print(x[:2])
print(y[:2])

print()
lmodel = LinearRegression().fit(x, y)
print(lmodel) # LinearRegression() // 클래스가 만들어짐
lpred = lmodel.predict(x)
print('LinearRegression pred : ', lpred[:5])
print('실제값 : ', y[:5])
print('lr2 : ', r2_score(y, lpred)) # lr2 :  0.8972106381789522 // 89.7% 설명력을 가지고 있음

print()
kmodel = KNeighborsRegressor(n_neighbors = 3).fit(x, y)
print(kmodel)
kpred = kmodel.predict(x)
print('KNeighborsRegressor pred : ', kpred[:5])
print('실제값 : ', y[:5])
print('kr2 : ', r2_score(y, kpred)) # kr2 :  0.968012077694316 // 96.8% 설명력을 가지고 있음

print()
rmodel = RandomForestRegressor(n_estimators = 100, criterion = 'mse').fit(x, y)
print(rmodel)
rpred = rmodel.predict(x)
print('RandomForestRegressor pred : ', rpred[:5])
print('실제값 : ', y[:5])
print('rr2 : ', r2_score(y, rpred)) # rr2 :  0.9973851305080002

print()
xmodel = XGBRegressor(n_estimators = 100).fit(x, y)
print(xmodel)
xpred = xmodel.predict(x)
print('XGBRegressor pred : ', xpred[:5])
print('실제값 : ', y[:5])
print('xr2 : ', r2_score(y, xpred)) # xr2 :  0.9999996661140423