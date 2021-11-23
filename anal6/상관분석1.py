#상관관계 분석 : 어떤 두 대상이 얼마나 관련이 있는지 그 정도를 분석
#상관계수의 수치(공분산을 표준화 함)로 관계의 정도를 파악
#광고비와 매출액, 게임시간과 능력치...

import numpy as np

#공분산
print(np.cov(np.arange(1,6),np.arange(2, 7)))
print(np.cov(np.arange(1,6),(3,3,3,3,3)))
print(np.cov(np.arange(1,6),np.arange(6,1,-1)))

x = [8,3,6,6,9,4,3,9,3,4]
print('x 평균: ', np.mean(x)) #평균 
print('x 분산: ', np.var(x)) #분산

y = [600,200,400,600,900,500,100,800,400,500]
print('y 평균: ', np.mean(y)) #평균 
print('y 분산: ', np.var(y)) #분산

print('x,y 공분산: \n',np.cov(x,y))
print('x,y 공분산: \n',np.cov(x,y)[0,1])

#공부산의 크기가 클수록 두 변수는 함께 많이 변화
#단위에 따라 공분산의 크기가 달라지므로 크기가 달라지므로 절대적 크기로 판단이 어렵다.
#공분산을 -1~1범위로 표준화 한것이 상관계수
print('x,y 상관계수 : \n', np.corrcoef(x,y))
print('x,y 상관계수 : \n', np.corrcoef(x,y)[0,1]) #0.86638