# iris dataset으로 단순선형회귀분석
import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
print(iris)
'''
     sepal_length  sepal_width  petal_length  petal_width    species
0             5.1          3.5           1.4          0.2     setosa
1             4.9          3.0           1.4          0.2     setosa ~...'''


#sns.pairplot(iris, hue = 'species')
#plt.show()
print('변수간 상관관계\n', iris.corr())
'''
               sepal_length  sepal_width  petal_length  petal_width
sepal_length      1.000000    -0.117570      0.871754     0.817941
sepal_width      -0.117570     1.000000     -0.428440    -0.366126
petal_length      0.871754    -0.428440      1.000000     0.962865
petal_width       0.817941    -0.366126      0.962865     1.000000 '''

# 선형회귀모델 작성1 : 상관관계가 약한 변수를 이용
result1 = smf.ols(formula = 'sepal_length ~ sepal_width', data = iris).fit()  #두 변수의 상관관계는 -0.117570 -> 매우 약한 음의 상관관계
print(result1.summary())
'''  기울기 : -0.2234   절편 : 6.5262
                            OLS Regression Results                            
==============================================================================
Dep. Variable:           sepal_length   R-squared(설명력):                 0.014
Model:                            OLS   Adj. R-squared(설명력-독립변수 2개이상): 0.007
Method:                 Least Squares   F-statistic:                     2.074
Date:                Fri, 05 Nov 2021   Prob (F-statistic)(모델이 의미가 있는가? -> 0.05보다 작아야 의미가 있는 모델.): 0.152
Time:                        12:46:49   Log-Likelihood:                -183.00
No. Observations:                 150   AIC:                             370.0
Df Residuals:                     148   BIC:                             376.0
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
===============================================================================
                  coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------
Intercept       6.5262      0.479     13.628      0.000       5.580       7.473
sepal_width    -0.2234      0.155     -1.440      0.152      -0.530       0.083
==============================================================================
Omnibus:                        4.389   Durbin-Watson:                   0.952
Prob(Omnibus):                  0.111   Jarque-Bera (JB):                4.237
Skew:                           0.360   Prob(JB):                        0.120
Kurtosis:                       2.600   Cond. No.                         24.2 '''
print('결정계수(설명력):', result1.rsquared) #결정계수(설명력): 0.013822654141080748  설명력은 0.35이상은 되어야 함.
print('p-value(유의확률):', result1.pvalues[1]) #p-value(유의확률): 0.15189826071144813 > 0.05이므로 모델로서 유의하지 않음. 사용할 수 없는 부적합한 모델.



# 선형회귀모델 작성2 : 상관관계가 강한 변수를 이용
result2 = smf.ols(formula = 'sepal_length ~ petal_length', data = iris).fit()  #두 변수의 상관관계는 0.871754 -> 매우 강한 양의 상관관계
print(result2.summary())
print('결정계수(설명력):', result2.rsquared) #결정계수(설명력): 0.7599546457725151 -> 독립변수가 종속변수의 분산을 약 76%의 설명함으로 상당히 높음.
print('p-value(유의확률):', result2.pvalues[1]) #p-value(유의확률): 1.0386674194499307e-47 < 0.05이므로 모델로서 유의하다. 사용할 수 있는 모델.
print(0.871754**2) # 상관계수를 제곱한 값은 결정계수(설명력)이 된다. 즉, 상관계수를 제곱한 값으로 말미암아 모델로서 적합한지도 확인할 수 있다.
pred = result2.predict()
print('예측값:',pred[:5]) #예측값: [4.8790946  4.8790946  4.83820238 4.91998683 4.8790946 ]
print('실제값:', iris.sepal_length[:5].values) #실제값: [5.1 4.9 4.7 4.6 5.]

# 궁극적으로 해야할 목표 : 전혀 새로운 값으로 아래에서 예측 결과 얻어보기
new_data = pd.DataFrame({'petal_length' : [1.4, 0.8, 8.0]}) #독립변수로 데이터프레임 만들기.모델을 데이터 프레임으로 만들었기 때문
#print(new_data)
y_pred_new = result2.predict(new_data)
print('새로운 값을 예측한 결과:\n', y_pred_new)
#4.879095      4.633741       7.577982

# iris dataset으로 다중선형회귀분석 (독립변수가 복수)
print('-------------')
result3 = smf.ols(formula = 'sepal_length ~ petal_length + petal_width', data = iris).fit()
print(result3.summary())
'''
                           OLS Regression Results                            
==============================================================================
Dep. Variable:           sepal_length   R-squared:                       0.766
Model:                            OLS   Adj. R-squared:                  0.763 -> 독립변수가 2개 이상이므로 이것을 볼것!
Method:                 Least Squares   F-statistic:                     241.0
Date:                Fri, 05 Nov 2021   Prob (F-statistic):           4.00e-47
Time:                        15:05:34   Log-Likelihood:                -75.023
No. Observations:                 150   AIC:                             156.0
Df Residuals:                     147   BIC:                             165.1
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept        4.1906      0.097     43.181      0.000       3.999       4.382
petal_length     0.5418      0.069      7.820      0.000       0.405       0.679
petal_width     -0.3196      0.160     -1.992      0.048      -0.637      -0.002
==============================================================================
Omnibus:                        0.383   Durbin-Watson:                   1.826
Prob(Omnibus):                  0.826   Jarque-Bera (JB):                0.540
Skew:                           0.060   Prob(JB):                        0.763
Kurtosis:                       2.732   Cond. No.                         25.3'''
print('결정계수(설명력):', result3.rsquared) #결정계수(설명력): 0.7662612975425306
print('p-value(유의확률):', result3.pvalues[1]) #p-value(유의확률): 9.414477120971696e-13
new_data = pd.DataFrame({'petal_length' : [1.4, 0.8, 8.0], 'petal_width' : [0.2, 0.8, 1.5]}) 
#print(new_data)
y_pred_new = result3.predict(new_data)
print('새로운 값을 예측한 결과:\n', y_pred_new)
#4.885160  4.368364  8.045474

print('--------------')
column_select = "+".join(iris.columns.difference(['sepal_length', 'species']))
print('column_select: ', column_select)
result4 = smf.ols(formula = 'sepal_length ~ ' + column_select, data = iris).fit()
#result4 = smf.ols(formula = 'sepal_length ~ petal_length + petal_width + sepal_width', data = iris).fit()
# 컬럼을 나열하기 싫을 때 위처럼 종속변수 평을 제외한 컬럼들을 join하여 변수에 넣어준 다음, 해당 변수를 ols에 넣어주면 된다.
print(result4.summary())
'''
                            OLS Regression Results                            
==============================================================================
Dep. Variable:           sepal_length   R-squared:                       0.859
Model:                            OLS   Adj. R-squared:                  0.856
Method:                 Least Squares   F-statistic:                     295.5
Date:                Fri, 05 Nov 2021   Prob (F-statistic):           8.59e-62
Time:                        16:04:05   Log-Likelihood:                -37.321
No. Observations:                 150   AIC:                             82.64
Df Residuals:                     146   BIC:                             94.69
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept        1.8560      0.251      7.401      0.000       1.360       2.352
petal_length     0.7091      0.057     12.502      0.000       0.597       0.821
petal_width     -0.5565      0.128     -4.363      0.000      -0.809      -0.304
sepal_width      0.6508      0.067      9.765      0.000       0.519       0.783
==============================================================================
Omnibus:                        0.345   Durbin-Watson:                   2.060
Prob(Omnibus):                  0.842   Jarque-Bera (JB):                0.504
Skew:                           0.007   Prob(JB):                        0.777
Kurtosis:                       2.716   Cond. No.                         54.7'''