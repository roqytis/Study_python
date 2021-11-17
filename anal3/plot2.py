#데이터에 따라 차트의 종류를 선택할 수 있어야 한다.

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn

x = np.arange(10)

'''
#인터페이스 유형
#1) Matlab 스타일의 인텊에시으
plt.figure()
plt.subplot(2,1,1)
plt.plot(x,np.sin(x))
plt.subplot(2,1,2)
plt.plot(x,np.cos(x))
plt.show()

#2) 객체지향 인터페이스
fig, ax = plt.subplots(nrows=2, ncols=1)
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))
plt.show()
'''

fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
ax1.hist(np.random.randn(10), bins=10, alpha= 0.9)
ax2.plot(np.random.randn(10))
plt.show()

# 막대 
data = [50, 80,100,70, 90]
plt.bar(range(len(data)),data)
plt.show()

err = np.random.rand(len(data))
plt.barh(range(len(data)),data, alpha =0.3, xerr =err)
plt.show()

#파이
plt.pie(data, explode = (0,0.1,0,0.3,0),  colors= ['yellow','red','blue'])
plt.show()

# 박스플롯
plt.boxplot(data)
plt.show()

# bubble chart
n = 30
np.random.seed(0)
x = np.random.randn(n)
y = np.random.randn(n)
color = np.random.rand(n)
scale = np.pi*(15*np.random.rand(n))**2
plt.scatter(x, y, s=scale, c = color)
plt.show()

# Series, 시계열 데이터
import pandas as pd
sdata = pd.Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
plt.plot(sdata)
plt.show()

fdata = pd.DataFrame(np.random.randn(1000, 4), index=pd.date_range('1/1/2000', periods=1000), columns=list('ABCD'))
fdata = fdata.cumsum()
print(fdata.head())
plt.plot(fdata)
plt.show()