# K-NN(K-NearestNeigher) : 최근접 이웃 알고리즘. k의 갯수가 중요
# 데이터로부터 거리가 가까운 k개의 다른 데이터의 레이블을 참조해서 분류

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import mglearn     # pip install mglearn
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')

# 가장 간단한 k-NN 알고리즘은 가장 가까운 훈련 데이터 포인트 하나를 최근접 이웃으로 찾아 예측에 사용한다. 
# 단순히 이 훈련 데이터 포인트의 출력이 예측이 된다.
# -------------------------
# Classification
mglearn.plots.plot_knn_classification(n_neighbors=1)
plt.show()

mglearn.plots.plot_knn_classification(n_neighbors=3)
plt.show()

mglearn.plots.plot_knn_classification(n_neighbors=5)
plt.show()

# Regression
mglearn.plots.plot_knn_regression(n_neighbors=1)
plt.show()

mglearn.plots.plot_knn_regression(n_neighbors=3)
plt.show()
# -------------------------
X, y = mglearn.datasets.make_forge()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=12)
print(X_train, ' ', X_train.shape)  # [[ 8.92229526 -0.63993225] ...   (19, 2)
print(X_test, ' ', X_test.shape)    #  (7, 2)
print(y_train)  # [0 0 1 1 0 1 0 1 1 1 0 1 0 0 0 1 0 1 0]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
print("test 예측: {}".format(model.predict(X_test)))
print("test 정확도: {:.2f}".format(model.score(X_test, y_test)))
print("train 정확도: {:.2f}".format(model.score(X_train, y_train)))

fig, axes = plt.subplots(1, 3, figsize=(10, 5))

for n_neighbors, ax in zip([1, 3, 9], axes):
    model2 = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X, y)
    mglearn.plots.plot_2d_separator(model2, X, fill=True, eps=0.5, ax=ax, alpha=.4)
    mglearn.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)
    ax.set_title("{} 이웃".format(n_neighbors))
    ax.set_xlabel("특성 0")
    ax.set_ylabel("특성 1")
    axes[0].legend(loc=1)

plt.show()
'''
그림을 보면 이웃을 하나 선택했을 때는 결정 경계가 훈련 데이터에 가깝게 따라가고 있다. 
이웃의 수를 늘릴수록 결정 경계는 더 부드러워진다. 부드러운 경계는 더 단순한 모델을 의미한다. 
다시 말해 이웃을 적게 사용하면 모델의 복잡도가 높아지고([그림]의 오른쪽) 많이 사용하면 복잡도는 낮아진다.
훈련 데이터 전체 개수를 이웃의 수로 지정하는 극단적인 경우에는 모든 테스트 포인트가 
같은 이웃(모든 훈련 데이터)을 가지게 되므로 테스트 포인트에 대한 예측은 모두 같은 값이 된다. 
즉 훈련 세트에서 가장 많은 데이터 포인트를 가진 클래스가 예측값이 된다.

일반적으로 KNeighbors 분류기에 중요한 매개변수는 두 개다. 데이터 포인트 사이의 거리를 재는 방법과 이웃의 수이다. 
실제로 이웃의 수는 3개나 5개 정도로 적을 때 잘 작동하지만, 이 매개변수는 잘 조정해야 한다. 
거리 재는 방법은 기본적으로 유클리디안 거리 방식을 사용.
'''