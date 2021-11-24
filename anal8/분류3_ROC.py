# Receiver operating characterisitics, ROC : 혹은 반응자 작용특성,
# 수용자 반응특성은 신호탐지이론에서 적중확률(Y축, True Positive Rate, Seneitivity) 대
# 오경보확률(X축, False Positive Rate, 1 - Specificity)의 그래프이다.
# ROC그래프는 정기각률이 늘어나면 탈루률이 늘어나는 관계를 효용 대 비용의 관계로 설명하고 있다.

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

x, y = make_classification(n_samples = 16, n_features = 2, n_redundant = 0, random_state = 0)
print(x) # [ 2.03418291 -0.38437236] ... // 독립변수
print(y) # [0 1 0 1 1 0 0 0 1 0 1 0 1 1 0 1] // 종속변수 (실제값)

model = LogisticRegression().fit(x, y)
y_hat = model.predict(x) # 예측
print('예측값 : ', y_hat) # 예측값 :  [1 1 0 1 1 0 0 0 1 0 0 0 1 1 0 1]
f_value = model.decision_function(x) # 결정 함수 : ROC curve를 위해 준비함
print('f_value : ', f_value) # 경계선으로 쓸 거라 별로 중요하게 안 여겨도 됨

print()
df = pd.DataFrame(np.vstack([f_value, y_hat, y]).T, columns = ['f', 'y_hat', 'y']) # f_value, y_hat, y // 결정함수, 예측값, 실제값
print(df)
df.sort_values('f', ascending = False).reset_index(drop = True)
print(df)

# ROC 그래프 작성
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y, y_hat))
# [[7 1]   // 맞은 걸 틀렸다고 한 것 1
#  [1 7]]  // 틀린 걸 맞았다곻 한 것 1
recall = 7 / (7 + 1) # 재현율, 민감도
fallout = 1 / (1 + 7) # 위 양성율 (1 - 특이도) fpr
print('recall : ', recall)
print('fallout : ', fallout)

from sklearn import metrics
ac_sco = metrics.accuracy_score(y, y_hat)
print('ac_sco(분류 정확도) : ', ac_sco)
cl_rep = metrics.classification_report(y, y_hat)
print('cl_rep(분류 보고서) : ', cl_rep)

print()
from sklearn.metrics import roc_curve

fpr, tpr, threshold = roc_curve(y, model.decision_function(x))
print('fpr : ', fpr)
print('tpr : ', tpr)
print('threshold : ', threshold)

import matplotlib.pyplot as plt
plt.plot(fpr, tpr, 'o-', label = 'Logistic Regression')
plt.plot([0, 1], [0, 1], 'k--', label = 'random guess')
plt.plot([fallout], [recall], 'ro', ms = 10)
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.legend(loc = 4)
plt.show()

from sklearn.metrics import auc # auc : Area Under the Curve
print(auc(fpr, tpr)) # 0.9375 // 1에 가까울수록 좋음
