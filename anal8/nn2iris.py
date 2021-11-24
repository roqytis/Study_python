# LogisticRegression 클래스로 다항분류 : softmax 함수 사용(결과를 확률값으로 내보냄. 확률값이 가장 큰 인덱스를 분류결과로 사용)
# iris dataset을 사용
# train / dataset 으로 분리해 train으로 모델을 학습하고 test로 모델을 검정(평가) : overfitting(과적합) 방지

from sklearn import datasets
from sklearn.model_selection._split import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler # 표준화
from sklearn.linear_model import LogisticRegression

iris = datasets.load_iris() # iris에 대한 여러 정보가 있다.
print(iris.keys())
#print(iris.data)


print(np.corrcoef(iris.data[:,2], iris.data[:, 3])) # 0.9628

x = iris.data[:, [2, 3]]
y = iris.target

print(x[:3])
print(y[:3], ' ', set(y))

# train / test로 분리
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

#스케일링(입력 데이터 크기를 표준화 또는 정규화)
# 스케일링을 하면 최적화 과정에서 안전성, 수련 속도 향상, 오버플로우/언더플로우 방지 가능
# 표준화 작업을 진행
# print(x_train[:3])
# sc = StandardScaler()
# sc.fit(x_train)
# sc.fit(x_test)
# x_train = sc.transform(x_train)
# x_test = sc.transform(x_test)
# print(x_train[:3])
# # 스케일링 원복
# inverse_x_train = sc.inverse_transform(x_train)
# print(inverse_x_train[:3])


print('분류 모델 생성')
#model = LogisticRegression(C = 100.0, random_state = 0)

from sklearn.linear_model import Perceptron
model = Perceptron(max_iter= 100, eta0 = 0.1)

print(model)
model.fit(x_train, y_train) # train data로 학습을 진행 지도 학습

# 분류 예측
y_pred = model.predict(x_test) # 모델을 평가하기 위해  test data로 예측
print('예측값 : ', y_pred)
print('예측값 : ', y_test)
print('총 갯수:%d, 오류수:%d '%(len(y_test), (y_test != y_pred).sum()))
print( '분류 정확도 확인 1 :')
print('%.3f'%accuracy_score(y_test, y_pred)) #0.600

