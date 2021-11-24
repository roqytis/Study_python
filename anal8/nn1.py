#  인공신경망(ANN)
# 단층시경망(뉴런, 노드) - Perception
#입력데이터 * 가중치 + bias의 합에 대해 임계값(활성화함수)을 기준으로 이항분류

import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

feature = np.array([[0,0],[0,1],[1,0],[1,1]])
print(feature)
#label = np.array([0,0,0,1]) #and
#label = np.array([0,1,1,1]) #or
label = np.array([0,1,1,0]) #exclusive or 인공신경망의 한계 -> 뉴런의 갯수를 (노드)의 갯수를 늘리는 것

ml = Perceptron(max_iter = 100, eta0 = 0.1).fit(feature,label) #max iter = 학습횟수(epoch), eta0 =학습량(learning_rate)
print(ml)
pred = ml.predict(feature)
print('pred: ', pred)
print('acc :', accuracy_score(label,pred))

print('-------------------------')
# MLP : Multi Layer Perceptron
# 뉴런(노드)의 갯수가 복수
from sklearn.neural_network import MLPClassifier

#ml2 = MLPClassifier(hidden_layer_sizes=30, max_iter = 100).fit(feature, label)
ml2 = MLPClassifier(hidden_layer_sizes=(10,10,10), max_iter = 300).fit(feature, label)

pred2 = ml2.predict(feature)
print('pred2: ', pred)
print('acc2 :', accuracy_score(label,pred2))
 

