#직단 간 차이 분석 : 평균 또는 비율 차이를 분석
#모집단에서 추출한 표본정보를 이용하여 모집단의 다양한  특성을 과학적으로 추론할 수 있다.
#T-test와 ANOVA의 차이
#두집단 이하의 변수에 대한 평균차이를 검정할 경우 T-test를 사용하여 검정통계량 T값을 구해 가설 검정을 한다.
#세 집단 이상의 변수에 대한 평균차이를 검정할 경우에는 ANOVA를 이용하여 검정통계량 F값을 구해 가설 검정을 한다

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 실습 예제 1) 하나의 집단 평균 검정 (난수사용)
np.random.seed(1)
mu = 0
n = 30
x = stats.norm(mu).rvs(n)
print(x,' ',np.mean(x))

#귀무 : 임의 집단의 자료들의 평균은 0이다
#대립 : 임의 집단의 자료들의 평균은 0이 아니다
#sns.displot(x, kde = True, rug= True)
#plt.show()

print(stats.shapiro(x)) #pvalue=0.635038137 >0.05 이므로 정규성 만족

result = stats.ttest_1samp(x,popmean = 0) # one samples t-test는 평균이 주어짐
print(result) #pvalue=0.751363> 0.05 이므로 귀무 채택. 임의 ㅣㅈㅂ단의 자료들의 평균은 0이다.

print('--------------------------')

#*단일 모집단의 평균에 대한 가설검정(one samples t-test)
#실습 예제 1)
#A중학교 1학년 1반 학생들의 시험 결과가 담기 파일을 읽어 처리(국어 점수 평균 검정)student.csv
#귀무 : 학생들의 국어 점수 평균은 80이다
#대립 : 학생들의 국어 점수 평균은 80 이 아니다.

data = pd.read_csv("../testdata/student.csv")
print(data.head(3))
print(np.mean(data.국어)) #80과 72.9는 유의미한 차이가 있는가?
print('정규성 확인: ', stats.shapiro(data.국어)) #pvalue=0.0129597084 < 0.05이므로 정규성 만족 못함


result2 = stats.ttest_1samp(data.국어, popmean = 80)
print(result2) #pvalue=0.19856051>0.05 이므로 귀무가설 채택

print('-----------------------------------')
# 실습 예제 2)
# 여아 신생아 몸무게의 평균 검정 수행 babyboom.csv
# 여아 신생아의 몸무게는 평균이 2800(g)으로 알려져 왔으나 이보다 더 크다는 주장이 나왔다.
# 표본으로 여아 18명을 뽑아 체중을 측정하였다고 할 때 새로운 주장이 맞는지 검정해 보자.

# 귀무 : 여아 신생아의 몸무게는 평균은 2800(g)이다.
# 대립 : 여아 신생아의 몸무게는 평균은 2800(g) 보다 크다.

data = pd.read_csv("../testdata/babyboom.csv")
print(data.head(3)) # 여아:1, 남아:2
print(data.info())
print()
fdata = data[data.gender ==1]
print(fdata, ' ', len(fdata))
print(np.mean(fdata.weight)) # 3132.444
print(np.std(fdata.weight))
print('정규성 확인 : ',stats.shapiro(fdata.weight))#pvalue=0.0129597084 < 0.05이므로 정규성 만족 못함
sns.displot(fdata.weight, kde = True)
plt.show()

#Q-Q plot :정규성 확인
stats.probplot(fdata.iloc[:, 2], plot = plt)
plt.show()

result3 = stats.ttest_1samp(fdata['weight'], popmean = 2800)
print(result3) #pvalue=0.0392684 < 0.05 이므로 귀무가설을 기각. 대립가설 채택
#여아 신생아의 몸무게는 평균 2800g 보다 증가하였다. 