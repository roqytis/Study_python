# LogisticRegression 클래스로 다항분류 : softmax 함수 사용 (결과를 확률값으로 내보냄. 확률값이 가장 큰 인덱스를 분류 결과로 사용
# iris dataset을 사용
# train / dataset으로 분리해 train으로 모델을 학습하고 test로 모델을 검정(평가) : overfitting(과적합) 방지

from sklearn import datasets
from sklearn.model_selection._split import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler # 표준화
from sklearn.linear_model import LogisticRegression

iris = datasets.load_iris() # iris에 대한 여러 정보가 담겨있다.
print(iris.keys()) # dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename'])

print(np.corrcoef(iris.data[:, 2], iris.data[:, 3])) # 0.96286543 1
x = iris.data[:, [2, 3]] # patal.length, petal.width
y = iris.target # 0 : setosa, 1 : versicolor, 2 : verginicar
print(x[:3])
print(y[:3], ' ', set(y)) # [0 0 0]   {0, 1, 2} // 1차원

# train / test로 분리
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0) # 7:3으로 분리
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # (105, 2) (45, 2) (105,) (45,)

"""
# 스케일링(입력 데이터 크기를 표준화 또는 정규화) 
# 스케일링을 하면 최적화 과정에서 안전성, 수련 속도 향상, 오버플로우/언더플로우 방지 가능
# 표준화 작업을 진행
print(x_train[:3]) # [[3.5 1. ] ...
sc = StandardScaler()
sc.fit(x_train)
sc.fit(x_test)
x_train = sc.transform(x_train) # 독립변수만 작업
x_test = sc.transform(x_test) # 독립변수만 작업
print(x_train[:3]) # [[-0.05624622 -0.18650096] ...

# 스케일링 원복
inverse_x_train = sc.inverse_transform(x_train)
print(inverse_x_train[:3]) # [[3.5 1. ]
"""

print('분류 모델 생성')
# model = LogisticRegression(C = 100.0, random_state = 0) # C : 모델에 패널티를 주면 정확도를 조정. tuning parameter

from sklearn.linear_model import Perceptron
model = Perceptron(max_iter = 100, eta0 = 0.1)

print(model)
model.fit(x_train, y_train) # train data로 학습을 진행. 지도학습

# 분류 예측
y_pred = model.predict(x_test) # 모델을 평가하기 위해 test data로 예측
print('예측값 : ', y_pred)
print('실제값 : ', y_test)
print('총 갯수 : %d, 오류 수 : %d' %(len(y_test), (y_test != y_pred).sum())) # 총 갯수 : 45, 오류 수 : 1
print('분류 정확도 확인1 : ')
print('%.5f' %accuracy_score(y_test, y_pred)) # 0.60000
