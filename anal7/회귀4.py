# iris dataset으로 단순선형회귀 분석
import pandas as pd
import seaborn as sns 
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris') # seaborn이 iris dataset을 제공해줌
print(iris.head(3))

sns.pairplot(iris, hue = 'species') # 꽃 종류 별로 출력
# plt.show()
print('변수간 상관관계\n', iris.corr()) # 꽃받침(sepal_length)의 길이는 꽃잎(petal)의 길이(length)와 너비(width)와 양의 상관관계가 강함

# 선형 회귀모델 작성1 : 상관관계가 약한 변수 사용 (petal_length) : -0.117570 // 약한 음의 상관관계
result1 = smf.ols(formula = 'sepal_length ~ sepal_width', data = iris).fit() # 종속변수(sepal_length), 독립변수(sepal_width) // fin() : 학습
print(result1.summary()) # ols 장점 summary()가 가능
print('결정계수(설명력) : ', result1.rsquared) # 결정계수(설명력) :  0.013822654141080748
print('p-value(유의확률) : ', result1.pvalues[1])  # [0]번째는 절편, [1]번째는 pvalue
# p-value(유의확률) :  0.15189826071144708 > 0.05 이므로 모델로서 유의하지 않음 (사용할 수 없음)

# 선형 회귀모델 작성2 : 상관관계가 강한 변수 사용
result2 = smf.ols(formula = 'sepal_length ~ petal_length', data = iris).fit()
print(result2.summary())
print(0.871754 ** 2) # 0.759955036516 // 상관계수를 제곱한 값이 결정계수 (상관계수가 높게 나와야 결정계수도 높음)
print('결정계수(설명력) : ', result2.rsquared) # 결정계수(설명력) :  0.7599546457725153 // 독립변수가 종속변수의 분산을 76% 정도 설명한다.
print('p-value(유의확률) : ', result2.pvalues[1]) # p-value(유의확률) :  1.0386674194499606e-47 < 0.05 이므로 모델로서 유의함 (사용 가능)

pred = result2.predict() # 예측값
print('예측값 : ', pred[:5]) # 예측값 :  [4.8790946  4.8790946  4.83820238 4.91998683 4.8790946 ]
print('실제값 : ', iris.sepal_length[:5].values) # 실제값 :  [5.1 4.9 4.7 4.6 5. ]

# 전혀 새로운 값으로 예측 결과 얻기 : 궁극적으로 우리가 하고 싶은 것
new_data = pd.DataFrame({'petal_length' : [1.4, 0.8, 8.0]}) # petal_length 값으로 sepal_length 예측 (학습할 때 dataframe으로 했기 때문에 예측할 때도 dataframe 사용)
print(new_data)
y_pred_new = result2.predict(new_data) # predict이 y = wx + b를 구해줌
print('전혀 새로운 값의 에측 결과 : ', y_pred_new)

print('-----------------------------------')
# iris dataset으로 다중선형회귀분석 (독립변수가 복수)
result3 = smf.ols(formula = 'sepal_length ~ petal_length + petal_width', data = iris).fit()
print(result3.summary())
print('결정계수(설명력) : ', result3.rsquared) # 결정계수(설명력) :  0.7662612975425307 // 독립변수가 종속변수의 분산을 76.6% 정도 설명한다.
print('p-value(유의확률) : ', result3.pvalues[1]) # 9.414477120971864e-13 < 0.05

new_data = pd.DataFrame({'petal_length' : [1.4, 0.8, 8.0], 'patal_length' : [0.2, 0.8, 1.5]})
y_pred_new = result2.predict(new_data) # predict이 y = wx + b를 구해줌
print('전혀 새로운 값의 에측 결과 : ', y_pred_new) 
# 전혀 새로운 값의 에측 결과 :  0    4.879095
# 1    4.633741
# 2    7.577982

print('-----------------------------------')
# result4 = smf.ols(formula = 'sepal_length ~ petal_length + petal_width + sepal_width', data = iris).fit()
# 칼럼이 많을 때 53라인, 55라인으로 처리하는 방법이 있음
column_select = "+".join(iris.columns.difference(['sepal_length', 'species'])) # 'sepal_length', 'species' 제외한 나머지 컬럼 합치기
result4 = smf.ols(formula = 'sepal_length ~ ' + column_select, data = iris).fit()
print(result4.summary())
