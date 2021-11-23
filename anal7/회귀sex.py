# 회귀분석 문제 2) 
# testdata에 저장된 student.csv 파일을 이용하여 세 과목 점수에 대한 회귀분석 모델을 만든다. 
# 이 회귀문제 모델을 이용하여 아래의 문제를 해결하시오.
#   - 국어 점수를 입력하면 수학 점수 예측
#   - 국어, 영어 점수를 입력하면 수학 점수 예측

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

student_data = pd.read_csv('../testdata/student.csv')
print(student_data.head(3))
print(student_data.corr())

model1 = smf.ols(formula="수학 ~ 국어", data=student_data).fit()
student_data.국어 =  int(input("국어 점수를 입력하세요: "))
predict_math = model1.predict(pd.DataFrame({'국어':student_data.국어}))
print("예상수학점수: ", predict_math[0])

print('------------------')
model2 = smf.ols('수학 ~ 국어 + 영어', data = student_data).fit()
print(model2.summary())
# Adj. R-squared: 0.619
# p-value : 0.000105 < 0.05이므로 모델 의미 있음
# Intercept     22.6238 
# 국어             0.1158
# 영어             0.5942

pred = model2.predict()
print('예측 값 : ', pred[0])
print('실제 값 : ', student_data.수학[0])

new_student = pd.DataFrame({'국어':[80, 70, 50, 30], '영어':[55, 65, 83, 25]})
new_pred = model2.predict(new_student)
print('입력값으로 수학 점수 예측 : \n', new_pred)