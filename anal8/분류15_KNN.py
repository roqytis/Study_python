from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
plt.rc('font', family = 'malgun gothic')

cancer = load_breast_cancer()
x_train, x_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify = cancer.target, random_state = 66)

train_acc = []
test_acc = []
k_setting = range(1, 11)

for n_neighbor in k_setting:
    clf = KNeighborsClassifier(n_neighbors = n_neighbor)
    clf.fit(x_train, y_train)
    train_acc.append(clf.score(x_train, y_train))
    test_acc.append(clf.score(x_test, y_test))


import numpy as np
print('train 분류 평균 정확도 : ', np.mean(train_acc)) # train 분류 평균 정확도 :  0.954225352112676
print('test 분류 평균 정확도 : ', np.mean(test_acc)) # test 분류 평균 정확도 :  0.918881118881119

plt.plot(k_setting, train_acc, label = 'train 분류 평균 정확도') # x축, y축 
plt.plot(k_setting, test_acc, label = 'test 분류 평균 정확도')
plt.xlabel('k')
plt.ylabel('acc')
plt.legend()
plt.show()