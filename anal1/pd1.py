# pandas : Series, DataFrame 객체 지원, 시계열, SQL, 파일처리, 시각화 ...

import pandas as pd
import numpy as np

#Series : 1차원 배열과 같은 자료구조로 색인을 갖는다. 
obj = pd.Series([3,7,-5,4])
#obj = pd.Series((3,7,-5,4))
#obj = pd.Series({3,7,-5,4}) #TypeError: 'set' type is unordered

print(obj,type(obj)) # int64 <class 'pandas.core.series.Series'>

obj2 = pd.Series([3,7,-5,4], index = ['a','b','c','d'])
print(obj2)
print(obj2.sum(), np.sum(obj2),sum(obj2))

print(obj2.values)
print(obj2.index)
print(obj2['a'])
print(obj2[0])
print(obj2[1:4])

print()
names = {'mouse':5000, 'keyboard':25000, 'monitor': 550000}
obj3 = pd.Series(names)
print(obj3,' ', type(obj3))
