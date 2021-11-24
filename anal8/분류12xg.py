# 앙상블 기법 중 부스팅 알고리즘으로 제공된 클래스로 XGBClassifier 부스타가 있다.
# Randomforest보다 성능이 우수하나 오버피팅의 우려가 있다. 직렬 처리
# 위스콘신 악성종양 데이터 사용

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.ensemble import RandomForestClassifier
from xgboost import plot_importance
import matplotlib.pyplot as plt
from lightgbm import LGBMClassifier

dataset = load_breast_cancer() 
print(dataset.keys()) #dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename'])
x_feature = dataset.data
y_label = dataset.target
#print(x_feature,' ',x_feature.shape)#(569, 30)
#print(y_label,' ',y_label.shape)#(569, 30)
#print(dataset.feature_names)

pd.set_option('max_columns',None)
cancer_df = pd.DataFrame(data = x_feature, columns = dataset.feature_names)
print(cancer_df.head(2),cancer_df.shape)
print(dataset.target_names) #['malignant':양성 'benign':악성]
print()
print(np.sum(y_label == 0)) # malignant 212
print(np.sum(y_label == 1)) # benign 357

# train / test
x_train, x_test,y_train, y_test = train_test_split(x_feature,y_label, test_size=0.2,random_state = 12)
print(x_train.shape, x_test.shape) #(455,30)(114,30)

#model = RandomForestClassifier(n_estimators= 500).fit(x_train, y_train) #BAgging 알고리즘 (병렬)
model = xgb.XGBClassifier(booster = 'gbtree', max_depth = 6, n_estimators = 500).fit(x_train,y_train) #boosing 알고리즘 (직렬)
#model = LGBMClassifier(max_depth = 6, n_estimators = 500).fit(x_train,y_train)

print()
print(model)
pred = model.predict(x_test)
print('예측값', pred[:10])
print('시제값:', y_test[:10])

from sklearn import metrics
acc = metrics.accuracy_score(y_test,pred)
print('acc: ', acc)

#시각화: XGBClassifier
fig, ax = plt.subplots(figsize = (10,12))
plot_importance(model, ax = ax)
plt.show()