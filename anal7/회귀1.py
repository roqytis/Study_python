# 최소제곱해를 이용해 선형행렬 방정식 얻기 y = ax + b

import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family = 'malgun gothic')

x = np.array([0, 1, 2, 3])
y = np.array([-1, 0.2, 0.9, 2.1])
plt.scatter(x, y)
plt.grid(True)
plt.show()

aa = np.vstack([x, np.ones(len(x))]).T # lstsq() 함수가 2차원을 원하기 때문에 이렇게 만듦
# print(aa)

import numpy.linalg as lin
w, b = lin.lstsq(aa, y, rcond = None)[0]  # 최소자승법(내부적으로 편미분) 계산
print(w, b)  # w : 0.9999999999999997  b : -0.9499999999999992

# 모델 수식 완성 y = wx + b ==> y = 0.9999999999999997 * x + -0.9499999999999992

plt.scatter(x, y)
plt.plot(x, w * x + b, 'red')
plt.grid(True)
plt.show()
