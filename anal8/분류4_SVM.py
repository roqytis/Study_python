# 서포트 벡터 머신(support vector machine, SVM[1].[2])은 기계 학습의 분야 중 하나로 패턴 인식, 
# 자료 분석을 위한 지도 학습 모델이며, 주로 분류와 회귀 분석을 위해 사용한다. 
# 두 카테고리 중 어느 하나에 속한 데이터의 집합이 주어졌을 때, SVM 알고리즘은 주어진 데이터 집합을 바탕으로 하여 
# 새로운 데이터가 어느 카테고리에 속할지 판단하는 비확률적 이진 선형 분류 모델을 만든다. 
# 만들어진 분류 모델은 데이터가 사상된 공간에서 경계로 표현되는데 SVM 알고리즘은 그 중 가장 큰 폭을 가진 경계를 
# 찾는 알고리즘이다. SVM은 선형 분류와 더불어 비선형 분류에서도 사용될 수 있다. 
# 비선형 분류를 하기 위해서 주어진 데이터를 고차원 특징 공간으로 사상하는 작업이 필요한데, 
# 이를 효율적으로 하기 위해 커널 트릭을 사용하기도 한다.

from sklearn import datasets
from sklearn.model_selection._split import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler # 표준화,
from sklearn.linear_model import LogisticRegression
from sklearn.metrics._scorer import accuracy_scorer

iris = datasets.load_iris() # iris에 대한 여러 정보가 담겨있다
print(iris.keys()) # dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename'])

print(iris.data)
print(np.corrcoef(iris.data[:, 2], iris.data[:, 3])) # 0.9628
x = iris.data[:, [2, 3]] # petal.length, petal.width
y = iris.target # 0:setosa, 1:versicolor, 2:verginicar
print(x[:3]) # 2차원 sklearn 모듈의 클래스는 독립은 2차원, 종속은 1차원을 원함
print(y[:3], ' ', set(y)) # [0 0 0] {0, 1, 2} # 1차원

# train / test로 분리
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0) # 7:3으로 분리
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # (105, 2) (45, 2) (105,) (45,)

"""
# 스케일링(입력 데이터 크기를 표준화또는 정규화
# 스케일링을 하면 최적화 과정에서 안전성, 수련 속도 향상, 오버플로우/언더플로우 방지 가능
# 표준화 작업을 진행
print(x_train[:3]) # [[3.5 1. ]...
sc = StandardScaler()
sc.fit(x_train)
sc.fit(x_test)
x_train = sc.transform(x_train) # 독립변수만 작업
x_test = sc.transform(x_test) # 독립변수만 작업
print(x_train[:3]) # [[-0.05624622 -0.18650096]
# 스케일링 원복
inverse_x_train = sc.inverse_transform(x_train)
print(inverse_x_train)
"""

print('분류 모델 생성')
#model = LogisticRegression(C = 100.0, random_state = 0) # C : 모델에 패널티를 주면 정확도를 조정 uuning parameter
from sklearn import svm
# model = svm.SVC(C = 1, random_state = 0) # train data로 학습을 진행. 지도 학습
model = svm.LinearSVC(C = 1000, random_state = 0) # train data로 학습을 진행. 지도 학습

print(model)
model.fit(x_train, y_train)

# 븐류 예측
y_pred = model.predict(x_test)  # 모델을 평가하기 위해 test data로 예측
print('예측값 : ', y_pred)
print('실제값 : ', y_test)
print('총 개수 : %d, 오유수 : %d'%(len(y_test), (y_test != y_pred).sum()))
print('분류 정확도 확인 1: ')
print('%.5f'%accuracy_score(y_test, y_pred))  # 0.97778

print('분류 정확도 확인 2: ')
con_mat = pd.crosstab(y_test, y_pred, rownames = ['예측값'], colnames = ['관측값'])
print(con_mat)
print((con_mat[0][0] + con_mat[1][1] + con_mat[2][2]) / len(y_test))

print('분류 정확도 확인 3: ')
print('test : ', model.score(x_test, y_test)) # 모델을 사용하지 않고 분류 정확도 확인  # 0.9777777777
print('train : ', model.score(x_train, y_train)) # 0.961904 <- 이 값이 test 결과와 차이가 많으면 오버피팅 또는 언더 피팅 의심

# 모델 저장 : 모델의 분류 정확도가 만족스러운 경우엔 모델을 저장한 후 저장된 모델을 불러다 사용
import pickle
pickle.dump(model, open('model.sav', 'wb'))
del model

read_model = pickle.load(open('model.sav', 'rb'))
#print(read_model)
# -----------------------------

# 새로운 값으로 분류 진행 - petal.length, petal.width
print(x_test[:3])  # 기존에 데이터를 읽어 새 데이터로 변신
new_data = np.array([[5.1, 2.4], [0.3, 0.3], [3.4, 0.2]]) # 만약 표준화하고 학습했다면 얘도 표준화해야 함
new_pred = read_model.predict(new_data)

print('분류 결과 : ', new_pred) # [2 0 1]
#print('참고 : 분류 결과(확률로 보기) : ',read_model.predict_proba(new_data)) # [2 0 1]
# [[1.25746586e-11 8.81678918e-04 9.99118321e-01] -> 2
# [9.99999491e-01 5.09165551e-07 1.32715591e-21] -> 0

#* 붓꽃 자료에 대한 로지스틱 회귀 결과를 차트로 그리기 *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib import font_manager, rc

plt.rc('font', family='malgun gothic')      
plt.rcParams['axes.unicode_minus']= False


def plot_decision_region(X, y, classifier, test_idx=None, resolution=0.02, title=''):
    markers = ('s', 'x', 'o', '^', 'v')  # 점 표시 모양 5개 정의
    colors = ('r', 'b', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    #print('cmap : ', cmap.colors[0], cmap.colors[1], cmap.colors[2])

    # decision surface 그리기
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    xx, yy = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))

    # xx, yy를 ravel()를 이용해 1차원 배열로 만든 후 전치행렬로 변환하여 퍼셉트론 분류기의 
    # predict()의 인자로 입력하여 계산된 예측값을 Z로 둔다.

    Z = classifier.predict(np.array([xx.ravel(), yy.ravel()]).T)
    Z = Z.reshape(xx.shape)   # Z를 reshape()을 이용해 원래 배열 모양으로 복원한다.

    # X를 xx, yy가 축인 그래프 상에 cmap을 이용해 등고선을 그림
    plt.contourf(xx, yy, Z, alpha=0.5, cmap=cmap)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

    X_test = X[test_idx, :]

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y==cl, 0], y=X[y==cl, 1], c=cmap(idx), marker=markers[idx], label=cl)
        
    if test_idx:
        X_test = X[test_idx, :]
        plt.scatter(X_test[:, 0], X_test[:, 1], c=[], linewidth=1, marker='o', s=80, label='testset')

    plt.xlabel('꽃잎 길이')
    plt.ylabel('꽃잎 너비')
    plt.legend(loc=2)
    plt.title(title)
    plt.show()

x_combined_std = np.vstack((x_train, x_test))
y_combined = np.hstack((y_train, y_test))
plot_decision_region(X=x_combined_std, y=y_combined, classifier=read_model, test_idx=range(105, 150), title='scikit-learn제공')

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier

# Import some data to play with

iris = datasets.load_iris()
X = iris.data
y = iris.target

# Binarize the output
y = label_binarize(y, classes=[0, 1, 2])
n_classes = y.shape[1]

# Add noisy features to make the problem harder
random_state = np.random.RandomState(0)
n_samples, n_features = X.shape
X = np.c_[X, random_state.randn(n_samples, 200 * n_features)]

# shuffle and split training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5, random_state=0)


# Learn to predict each class against the other
# OneVsOneClassifier 클래스를 사용하면 이진 클래스용 모형을 OvO 방법으로 다중 클래스용 모형으로 변환한다. 
# OneVsOneClassifier 클래스는 각 클래스가 얻는 조건부 확률값을 합한 값을 decision_function으로 출력한다.
classifier = OneVsRestClassifier(svm.SVC(kernel='linear', probability=True,

                                 random_state=random_state))

y_score = classifier.fit(X_train, y_train).decision_function(X_test)

# Compute ROC curve and ROC area for each class
fpr = dict()
tpr = dict()
roc_auc = dict()

for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

# Compute micro-average ROC curve and ROC area
# 사이킷런 패키지는  roc_curve 명령을 제공한다. 
# 인수로는 타겟 y 벡터와 판별함수 벡터(혹은 확률 벡터)를 넣고 결과로는 변화되는 기준값과 그 기준값을 사용했을 때의 재현율을 반환한다.
fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_score.ravel())

# AUC(Area Under the Curve)는 ROC curve의 면적을 뜻한다. 
# 위양성률(fall out)값이 같을 때 재현률값이 클거나 재현률값이 같을 때 위양성률값이 작을수록 AUC가 1에 가까운 값이고 좋은 모형이다.
roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

#Plot of a ROC curve for a specific class
plt.figure()
lw = 2
plt.plot(fpr[2], tpr[2], color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc[2])

plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')

plt.xlim([0.0, 1.0])

plt.ylim([0.0, 1.05])

plt.xlabel('False Positive Rate')

plt.ylabel('True Positive Rate')

plt.title('Receiver operating characteristic example')

plt.legend(loc="lower right")

plt.show()



# Plot ROC curves for the multiclass problem

# Compute macro-average ROC curve and ROC area



# First aggregate all false positive rates

all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_classes)]))



# Then interpolate all ROC curves at this points

mean_tpr = np.zeros_like(all_fpr)



for i in range(n_classes):

    mean_tpr += np.interp(all_fpr, fpr[i], tpr[i])



# Finally average it and compute AUC

mean_tpr /= n_classes



fpr["macro"] = all_fpr

tpr["macro"] = mean_tpr

roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])



# Plot all ROC curves

plt.figure()

plt.plot(fpr["micro"], tpr["micro"],

         label='micro-average ROC curve (area = {0:0.2f})'

               ''.format(roc_auc["micro"]),

         color='deeppink', linestyle=':', linewidth=4)



plt.plot(fpr["macro"], tpr["macro"],

         label='macro-average ROC curve (area = {0:0.2f})'

               ''.format(roc_auc["macro"]),

         color='navy', linestyle=':', linewidth=4)



from itertools import cycle

# iterable에서 요소를 반환하고 각각의 복사본을 저장하는 반복자를 만든다. 반복 가능한 요소가 모두 소모되면 저장된 사본에서 요소를 리턴한다. 

# 반복 가능한 요소가 모두 소모될때까지 무한정 반복한다.

colors = cycle(['aqua', 'darkorange', 'cornflowerblue'])

for i, color in zip(range(n_classes), colors):

    plt.plot(fpr[i], tpr[i], color=color, lw=lw,

             label='ROC curve of class {0} (area = {1:0.2f})'

             ''.format(i, roc_auc[i]))



plt.plot([0, 1], [0, 1], 'k--', lw=lw)

plt.xlim([0.0, 1.0])

plt.ylim([0.0, 1.05])

plt.xlabel('False Positive Rate')

plt.ylabel('True Positive Rate')

plt.title('Some extension of Receiver operating characteristic to multi-class')

plt.legend(loc="lower right")

plt.show()
