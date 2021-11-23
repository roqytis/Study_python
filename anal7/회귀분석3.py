# 방법4 : 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

score_iq = pd.read_csv('../testdata/score_iq.csv')
print(score_iq)
'''
      sid   score   iq   academy  game tv
0    10001     90  140        2     1   0
1    10002     75  125        1     3   3 ~...'''
x = score_iq.iq #독립변수 iq
y = score_iq.score #iq에 영향을 받는 시험점수 score

#상관계수 확인
print(np.corrcoef(x, y))
print(score_iq.corr())
plt.scatter(x, y)
#plt.show()
model = stats.linregress(x, y)
print(model)
#LinregressResult(slope=0.6514309527270075, intercept=-2.8564471221974657, rvalue=0.8822203446134699, 
#pvalue=2.8476895206683644e-50, stderr=0.028577934409305443, intercept_stderr=3.546211918048538)
print('기울기: ', model.slope) # 0.6514309527270075
print('절편: ', model.intercept) # -2.8564471221974657
print('p값: ', model.pvalue) # 2.8476895206683644e-50 < 0.05이므로 적합한 모델.
plt.scatter(x, y)
plt.plot(x, model.slope*x + model.intercept, 'r') # ax+b를 이용해 추세선 만들기.
plt.show()