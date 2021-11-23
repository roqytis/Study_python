# 회귀분석 문제 2) 
# testdata에 저장된 student.csv 파일을 이용하여 세 과목 점수에 대한 회귀분석 모델을 만든다. 
# 이 회귀문제 모델을 이용하여 아래의 문제를 해결하시오.
#   - 국어 점수를 입력하면 수학 점수 예측
#   - 국어, 영어 점수를 입력하면 수학 점수 예측

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

grade_df = pd.read_csv('../testdata/student.csv')
print(grade_df.head(3))

#print(frame)

# 상관관계
print(grade_df.corr())

# - 국어 점수를 입력하면 수학 점수 예측
# linear regression model1
model1 = smf.ols(formula = "수학 ~ 국어", data = grade_df).fit()
#print(model1.summary())
grade_df.국어 = int(input("국어 점수를 입력하시오 : "))
predict_math = model1.predict(pd.DataFrame({'국어':grade_df.국어}))
pred1 = model1.predict()
print("예상 수학 점수 ", pred1[0])

print('---' * 15)

#   - 국어, 영어 점수를 입력하면 수학 점수 예측
# linear regression model2
model2 = smf.ols(formula = '수학 ~ 국어 + 영어', data = grade_df).fit()
print(model2.summary()) # R-squared : 0.619  p-value : 0.000105 < 0.05
# Intercept : 22.6238, x1 : 0.1158, y1 : 0.5942
# 회귀식 : (0.1158 * 95) + (0.5942 * 85) + 22.6238

# predict
pred = model2.predict()
print('예측값 : ', pred[0])
print('실제값 : ', grade_df.수학[0])

# new predict
# 원래는 input 으로 국어 점수와 영어 점수 받아야 함. 그치만 귀찮은걸...ㅎ

new_grade = pd.DataFrame({'국어':[80, 70, 50, 30], '영어':[55, 95, 83, 25]})
new_pred = model2.predict(new_grade)
print('입력값으로 수학 점수 예측 : \n', new_pred)