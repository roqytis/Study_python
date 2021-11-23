# 방법4 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

score_iq = pd.read_csv('../testdata/score_iq.csv') # iq에 따른 시험 점수 데이터
print(score_iq.head(3))
x = score_iq.iq # 연속형
y = score_iq.score # 연속형

# 상관계수 확인
print(np.corrcoef(x, y)) # 0.88222034 // 양의 상관관계가 매우 높음
print(score_iq.corr()) # 0.882220 // 양의 상관관계가 매우 높음

# plt.scatter(x, y)
# plt.show()

model = stats.linregress(x, y)
print(model)
print('기울기 : ', model.slope) # 기울기 :  0.6514309527270075
print('절편 : ', model.intercept) # 절편 :  -2.8564471221974657
print('pvalue : ', model.pvalue) # pvalue :  2.8476895206683644e-50 < 0.05 이므로 적합한 모델
plt.scatter(x, y)
plt.plot(x, model.slope * x + model.intercept, 'r') # ax+b를 이용해 추세선 만들기
plt.show()
