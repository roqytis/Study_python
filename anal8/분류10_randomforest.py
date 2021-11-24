# 앙상블 기법 중 DecisitionTree를 여러개 묶어 결과에 대해 투표를 해서 최종 결과 얻기
# 알고리즘 : 배깅(bagging) : 샘플을 복원 추출로 여러 번 뽑아 각 모델을 학습시켜 집계하는 방법. 병렬처리

# 타이타닉 데이터로 연습
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import model_selection

df = pd.read_csv('../testdata/titanic_data.csv')
print(df.head(3))
print(df.isnull().any())
df = df.dropna(subset = ['Pclass', 'Age', 'Sex'])
print(df.shape) # (714, 12)

df_x = df[['Pclass', 'Age', 'Sex']] # 독립변수로 사용
df_y = df['Survived'] # 종속변수로 사용

print(df.Sex[:3]) # male : 1, female : 0
# 스케일링
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
df_x.loc[:, 'Sex'] = LabelEncoder().fit_transform(df_x['Sex'])
print(df_x.head(3))

# train / test
train_x, test_x, train_y, test_y = train_test_split(df_x, df_y)

# model 
model = RandomForestClassifier(criterion = 'entropy', n_estimators = 500, random_state = 0) # 현장에서는 보통 2000개
model.fit(train_x, train_y)

# pred
pred = model.predict(test_x)

# acc
print('acc : ', sum(test_y == pred) / len(test_y)) # acc :  0.7988826815642458

from sklearn.metrics import accuracy_score
print('acc : ', accuracy_score(test_y, pred)) # acc :  0.7988826815642458

# 독립변수 중 중요 변수 확인
print()
import matplotlib.pyplot as plt
import numpy as np
print('특성(변수) 중요도 : {}' .format(model.feature_importances_))

def plot_importance_func(model):
    n_features = df_x.shape[1]
    plt.barh(range(n_features), model.feature_importances_, align = 'center')
    plt.yticks(np.arange(n_features), df_x.columns)
    plt.xlabel('attr importance')
    plt.ylabel('attr')
    plt.show()

plot_importance_func(model)