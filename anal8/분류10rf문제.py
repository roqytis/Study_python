from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import model_selection

df = pd.read_csv("winequality-red.csv")
print(df.head(3), ' ', df.shape)  # (1599, 12)
print(df.isnull().any())

df_x = df.drop(['quality'], axis=1)  # 독립변수로 사용. quality를 제외한 나머지 칼람
df_y = df['quality']  # 종속변수로 사용
print(df_y.unique())  # [5 6 7 4 8 3]
print(df_x.columns)  # ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', ...


# train/test
train_x, test_x, train_y, test_y = train_test_split(df_x, df_y)
print(train_x.shape, test_x.shape, train_y.shape, test_y.shape)
# (1199, 11) (400, 11) (1199,) (400,)

# model
model = RandomForestClassifier(criterion='entropy', n_estimators=500)  
model.fit(train_x, train_y)

# pred
pred = model.predict(test_x)

# acc
from sklearn.metrics import accuracy_score
print('acc: ', accuracy_score(test_y, pred))  # acc:  0.7075

# 독립변수 중 중요 변수 확인
print()
import matplotlib.pyplot as plt
import numpy as np

print('특성(변수) 중요도: {}'.format(model.feature_importances_))
# 특성(변수) 중요도: [0.07075122 0.1046604  0.07579604 0.06846865 0.08306736 0.06500258
# 0.09446111 0.08946545 0.06900384 0.11966801 0.15965535]

def plot_importance_func(model):
    n_features = df_x.shape[1]
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), df_x.columns)
    plt.xlabel("attr importance")
    plt.ylabel("attr")
    plt.show()

plot_importance_func(model)  # alcohol 이 독립변수 중 가장 중요도가 높다!

