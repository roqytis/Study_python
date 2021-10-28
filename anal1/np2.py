# numpy : 연산
import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64) 
y = np.arange(5,9).reshape((2,2))
y = y.astype(np.float64)
print(x, ' ',x.dtype)
print(y, ' ',x.dtype)

print()
print(x + y)
print()
print(x - y) #substract()
print()
print(x * y) #multiply()
print()
print(x / y) #divide()

print()
print(x.dot(y)) # 내적 : R x %*% y
print(np.dot(x,y))

print()
print(np.sum(x))
print(np.mean(x))
print(np.cumsum(x))

print()
print(x)
print(x.T)
print(x.transpose())

print('Broodcasting : 크기가 다른 배열 간 연산을 할 경우 자동으로 작은 배열을 여러번 반복해 큰 배열과 연산 수행')
x = np.arange(1,10). reshape(3,3)
print(x)
y = np.array([1,0,1])
print(y)

kbs = print(x+y)
print(kbs)