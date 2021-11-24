# 나이브베이즈 분류 알고리즘 모델 - 비가 올지 여부 확인

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn import metrics

df = pd.read_csv('../testdata/weather.csv')
print(df.head(3))
print(df.info())

x = df[['MinTemp', 'MaxTemp', 'Rainfall']] # 독립변수
label = df['RainTomorrow'].apply(lambda x:1 if x == 'Yes' else 0) # 종속변수
print(x[:5])
print(label[:5])

# train / test
train_x, test_x, train_y, test_y = train_test_split(x, label, test_size = 0.3, random_state = 0)
print(len(train_x), ' ', len(test_x)) # 256   110

print('모델 생성 ---------------------------')
gmodel = GaussianNB()
print(gmodel)
gmodel.fit(train_x, train_y)

# 분류 예측
pred = gmodel.predict(test_x)
print('예측값 : ', pred[:5])
print('실제값 : ', test_y[:5].values)
acc = sum(test_y == pred) / len(pred)
print('분류 정확도 : ', acc)

print('분류 정확도 : ', accuracy_score(test_y, pred))
print('분류 보고서 : ', metrics.classification_report(test_y, pred))

print()
# 새로운 자료로 분류 예측
import numpy as np
print(x[:3])
my_weather = np.array([[0, 16, 10], [10, 13, 0], [20, 26, 0]])
print(gmodel.predict(my_weather))