# *서로 대응인 두 집단의 평균 차이 검정 (paired samples t test
# 처리 이전과 처리 이후를 각각의 모집단으로 판단하여 동일한 관찰 대상으로부터 처리 이전과 처리 이후를 1 1 로 대응시킨 두 집단으로 부터
# 의 표본을 대응표본 (paired sample) 이라고 한다
# 대응인 두 집단의 평균 비교는 동일한 관찰 대상으로부터 처리 이전의 관찰과 이후의 관찰을 비교하여 영향을 미친 정도를 밝히는데 주로 사용
# 하고 있다 집단 간 비교가 아니므로 등분산 검정을 할 필요가 없다

#실습1) 3강의실 교육생들을 대상으로 특가이 시험점수에 영향을 줄었는가? 이름 검정하시오
# 귀무 : 특강 저후의 시험점수는 차이가 없다.
# 대립 : 특강 전후의 시험점수는 차이가 없다.

import numpy as np
import scipy.stats as stats

np.random.seed(123)
x1 = np.random.normal(75, 10, 100) #특갖 전 점수
x2 = np.random.normal(80, 10, 100) #특강 후 점수
#print(x1)
#print(x2)

#정규성을 위한 기각화
import matplotlib.pyplot as plt
import  seaborn as sns
sns.histplot(x1,kde =True)
sns.histplot(x2,kde =True)
plt.show()

print(stats.shapiro(x1)) #pvalue=0.274 > 0.05 정규성 만족
print(stats.shapiro(x2)) #pvalue=0.102138 > 0.05 정규성 만족

#등분산설 검정은 안함
print(stats.ttest_rel(x1, x2))
#Ttest_relResult(statistic=-3.003102708378836, pvalue=0.0033837913974620205)
#pvalue=0.0033837<0.05 이므로 귀무가설 기각
#대립 : 특강 전후의 시험점수 차이가 있다

print('-----------------------------')

# 실습2) 9명의 환자에 대해 복부 수술 전  몸무게와 복부 수술 후 몸무게 변화
#귀무 : 복부 수술 전  몸무게와 복부 수술 후 몸무게 변화에 차이가 없다
#대립 : 복부 수술 전  몸무게와 복부 수술 후 몸무게 변화에 차이가 있다

baseline = [67.2, 67.4, 71.5, 77.6, 86.0, 89.1, 59.5, 81.9, 105.5]
follow_up = [62.4, 64.6, 70.4, 62.6, 80.1, 73.2, 58.2, 71.0, 101.0]
print(np.mean(baseline))
print(np.mean(follow_up))
print(np.mean(baseline)-np.mean(follow_up)) #6.911

paired = stats.ttest_rel(baseline, follow_up)
print(paired)
#Ttest_relResult(statistic=3.6681166519351103, pvalue=0.006326650855933662)
#pvalue=0.00632 < 0.05이므로 귀무가설 기각
# 조치 사항....

print('-----집단에 따라 검정 방법을 결정----------------------')
#수면제 1종류를 먹다가 수면제 2종류를 먹었을때 숨ㄴ시간 변화가 있는가 검정
x1 = np.array([0.7, 0.3, 0.1, -0.3,0.2]) #수면제 1종류
x2 = np.array([1.0, 1.3, 0.4, -0.1,0.5]) #수면제 2종류

#독립 표본 검정 t검정 : 서로 다른 사람이 ㅅ면제를 복용 했다면
r= stats.ttest_ind(x1,x2)
print(r)
# Ttest_indResult(statistic=-1.4372104127412249, pvalue=0.188594337977496)
#대응 표본 검정 t검정 : 동일한 사람이 수면제를 복용 했다면
r= stats.ttest_rel(x1,x2)
print(r)
#Ttest_relResult(statistic=-2.8710608935035853, pvalue=0.0454200326745538)