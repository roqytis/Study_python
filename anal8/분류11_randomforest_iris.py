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
#model = LogisticRegression(C = 100.0, random_state = 0) # C : 모델에 패널티를 주면 정확도를 조정. tuning parameter

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(criterion = 'entropy', n_estimators = 500, n_jobs = 2, random_state = 0)

print(model)
model.fit(x_train, y_train) # train data로 학습을 진행. 지도학습

# 분류 예측
y_pred = model.predict(x_test) # 모델을 평가하기 위해 test data로 예측
print('예측값 : ', y_pred)
print('실제값 : ', y_test)
print('총 갯수 : %d, 오류 수 : %d' %(len(y_test), (y_test != y_pred).sum())) # 총 갯수 : 45, 오류 수 : 1
print('분류 정확도 확인1 : ')
print('%.5f' %accuracy_score(y_test, y_pred)) # 0.97778

print('분류 정확도 확인 2 :')
con_mat = pd.crosstab(y_test, y_pred, rownames = ['예측값'], colnames = ['관측값'])
print(con_mat)
print((con_mat[0][0] + con_mat[1][1] + con_mat[2][2]) / len(y_test)) # 0.9777777777777777

print('분류 정확도 확인 3 : ')
print('test : ', model.score(x_test, y_test)) # test :  0.9777777777777777 // 모델을 사용하지 않고 분류 정확도 확인 
print('train : ', model.score(x_train, y_train)) # train :  0.9619047619047619 <- 이 값이 test 결과와 차이가 많으면 오버피팅 또는 언더피팅 의심

# 모델 저장 : 모델의 분류 정확도가 만족스러운 경우엔 모델을 저장ㅎ나 후 저장된 모델을 불러다 사용
import pickle
pickle.dump(model, open('model.sav', 'wb'))
del model
#print(model)

import pickle
read_model = pickle.load(open('model.sav', 'rb'))
#print(read_model)

# 새로운 값으로 분류 진행 - petal.length, petal.width
print(x_test[:3]) # 기존에 데이터를 읽어 새 데이터로 변신
new_data = np.array([[5.1, 2.4], [0.3, 0.3], [3.4, 0.2]]) # 만약 표준화하고 학습했다면 애도 표준화해야 함
new_pred = read_model.predict(new_data)

print('분류 결과 : ', new_pred) # [2 0 1]
print('참고 : 분류 결과(확률로 보기) : ', read_model.predict_proba(new_data)) # [2 0 1]
# [[1.25746582e-11 8.81678918e-04 9.99118321e-01]
#  [9.99999491e-01 5.09165532e-07 1.32715591e-21]
#  [5.23769475e-03 9.94762296e-01 9.41292567e-09]]

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