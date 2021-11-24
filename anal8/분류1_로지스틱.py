# Logistic Regreession : 로지스틱 회귀분석 - 이항분류(binary classfication)
# 독립변수 : 연속형, 종속변수 : 범주형
# odds -> odds ratio -> logit -> 시그모이드 함수 사용하여 0 또는 1로 분류

import statsmodels.api as sm
import numpy as np

# 시그 모이드 함수 처리
import math
def sig_func(x):
    return 1 / (1 + math.exp(-x))

print(np.around(sig_func(3)))
print(np.around(sig_func(1)))
print(np.around(sig_func(-2)))
print(np.around(sig_func(-5)))


mtcars = sm.datasets.get_rdataset('mtcars').data
print(mtcars.head(2))

mtcar = mtcars.loc[:, ['mpg','hp','am']]
print(mtcar.head(2))
print(mtcar.am.unique())

print()

import statsmodels.formula.api as smf
# 연비와 마력수(독립:연속형)로 변속기(종속:범주형) 분류
# 방법1 : logit()
formula = 'am ~ mpg + hp'
result= smf.logit(formula = formula, data = mtcar).fit()
print(result.summary()) # logit Regression Results
print()
pred = result.predict(mtcar[:10])

print('예측 값 :',pred.values)
print('예측 값 :', np.around(pred.values))
print('실제 값 :', mtcar['am'][:10].values)

# confusion matrix
conf_tab = result.pred_table()
print(conf_tab)

# 분류 정확도
print('분류 정확도 : ', (16+10) / len(mtcar)) # 0.8125 81%의 분류 정확도를 가진 모델
print('분류 정확도 : ', (conf_tab[0][0] + conf_tab[1][1])/ len(mtcar))

from sklearn.metrics import accuracy_score
print('분류 정확도 : ', accuracy_score(mtcar['am'], np.around(result.predict(mtcar)))) # accuracy_score(실제

# 방법2 : glm() : 일반화된 선형 모델
result2 = smf.glm(formula = formula, data = mtcar, family = sm.families.Binomial()).fit()
print(result2)
print(result2.summary())

glm_pred = result2.predict(mtcar[:5])
print('예측 값 :', glm_pred)
print('예측 값 :', np.around(glm_pred).values)
print('실제 값 :', mtcar['am'][:10].values)

print()

glm_pred2 = result2.predict(mtcar)
print('분류 정확도 :', accuracy_score(mtcar['am'], np.around(glm_pred2))) # 0.8125


print('새로운 값으로 분류------------')
newdf = mtcar.iloc[:2].copy()
newdf['mpg'] = [10, 30]
newdf['hp'] = [100,120]
print(newdf)


new_pred = result2.predict(newdf)
print(new_pred)
print('새자료 분류 결과 : ',np.around(new_pred).values)
print('새자료 분류 결과 : ',np.rint(new_pred).values)


