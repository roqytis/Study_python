import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import random
import pandas as pd

#https://cafe.daum.net/flowlife/RUrO/78
'''
[two-sample t 검정(독립표본 t검정) : 문제2]  
아래와 같은 자료 중에서 남자와 여자를 각각 15명씩 무작위로 비복원 추출하여 혈관 내의 콜레스테롤 양에 차이가 있는지를 검정하시오.
  남자 : 0.9 2.2 1.6 2.8 4.2 3.7 2.6 2.9 3.3 1.2 3.2 2.7 3.8 4.5 4 2.2 0.8 0.5 0.3 5.3 5.7 2.3 9.8
  여자 : 1.4 2.7 2.1 1.8 3.3 3.2 1.6 1.9 2.3 2.5 2.3 1.4 2.6 3.5 2.1 6.6 7.7 8.8 6.6 6.4
'''
# 귀무가설 : 남/여 간 콜레스테롤 수치의 차이가 없다.
# 대립가설 : 남/여 간 콜레스테롤 수치의 차이가 있다.
male = [0.9, 2.2, 1.6, 2.8, 4.2, 3.7, 2.6, 2.9, 3.3, 1.2, 3.2, 2.7, 3.8, 4.5, 4, 2.2, 0.8, 0.5, 0.3, 5.3, 5.7, 2.3, 9.8]
female = [1.4, 2.7, 2.1, 1.8, 3.3, 3.2, 1.6, 1.9, 2.3, 2.5, 2.3, 1.4, 2.6, 3.5, 2.1, 6.6, 7.7, 8.8, 6.6, 6.4]
ranmale = random.sample(male, k = 15)
ranfemale = random.sample(female, k = 15)
#귀무가설 : 남자와 여자의 현관 내 콜레스테롤 양에 차이가 없다.
# 대립 : 남자와 여자의 현관 내 콜레스테롤 양에 차이가 있다.
#실행마다 랜덤하게 작동.
print(np.mean(ranmale))
print(np.mean(ranfemale))
print(stats.shapiro(ranmale)) #pvalue=0.01723109371960163 < 0.05 정규성을 만족하지 않음.
print(stats.shapiro(ranfemale)) #pvalue=0.007430407218635082 < 0.05 정규성을 만족하지 않음.
print(stats.levene(ranmale, ranfemale)) #pvalue=0.6360323071189946 > 0.05이므로 등분산성 만족.
two_sample = stats.ttest_ind(ranmale, ranfemale, equal_var = True)
print(two_sample) #pvalue=0.6555208189450701 > 0.05
#대립가설을 기각하고 귀무가설을 채택
#결론 : 남/여 간 콜레스테롤 수치의 차이가 없다.



'''
[two-sample t 검정(독립표본 t검정) : 문제3]
DB에 저장된 jikwon 테이블에서 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하는지 검정하시오.
연봉이 없는 직원은 해당 부서의 평균연봉으로 채워준다. '''
# 귀무가설 : 총부무와 영업부의 연봉의 평균은 차이가 없다.
# 대립가설 : 총부무와 영업부의 연봉의 평균은 차이가 있다.
import MySQLdb
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

try:
    conn= MySQLdb.connect(**config) #DB연동. dict타입인 config 넣어주기. **표시 주의
    print(conn) #<_mysql.connection open to '127.0.0.1' at 000002585BCD2440> 정상 출력.
    cursor=conn.cursor()
    sql= "select jikwon_pay, buser_num from jikwon where buser_num in (10, 20)" 
    cursor.execute(sql)
    df=cursor.fetchall()
    df = pd.DataFrame(df, columns = ['연봉', '부서'])
    sp = np.array(df.iloc[:, [0,1]])
    print(sp)
    jik1 = sp[sp[:,1] == 10, 0] #총부무의 연봉
    jik2 = sp[sp[:,1] == 20, 0] #영업부의 연봉
    print(np.mean(jik1)) #총무부 연봉 평균
    print(np.mean(jik2)) #영업부 연봉 평균
    print(stats.shapiro(jik1)) # pvalue=0.02604489028453827 정규성 만족x
    print(stats.shapiro(jik2)) #pvalue=0.025608452036976814 정규성 만족x
    print(stats.levene(jik1, jik2)) #pvalue=0.915044305043978 > 0.05 등분산성 만족
    print(stats.ttest_ind(jik1, jik2, equal_var = True)) #pvalue=0.6523879191675446 > 0.05
    # p값이 0.05보다 크므로 대립가설 기각, 귀무가설 채택
    # 결론 : 총부무와 영업부의 연봉의 평균은 차이가 없다.
    
except Exception as e:
    print('err: ',e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()





'''
[대응표본 t 검정 : 문제4]
어느 학급의 교사는 매년 학기 내 치뤄지는 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있다고 말하고 있다. 
이 때, 올해의 해당 학급의 중간고사 성적과 기말고사 성적은 다음과 같다. 점수는 학생 번호 순으로 배열되어 있다.
   중간 : 80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80
   기말 : 90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95
그렇다면 이 학급의 학업능력이 변화했다고 이야기 할 수 있는가? '''
# 귀무가설 : 학급의 학업능력은 변화하지 않았다.
# 대립가설 : 학급의 학업능력은 변화가 있었다.
jungan = [80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80]
gimal = [90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95]
print(np.mean(jungan)) #중간 평균 74.16666666666667
print(np.mean(gimal)) #기말 평균 81.66666666666667

print(stats.ttest_rel(jungan, gimal)) #pvalue=0.023486192540203194
# pvalue=0.023486192540203194 < 0.05이므로 귀무가설을 기각, 대립가설을 채택한다.
# 결론 : 학급의 학업능력은 변화가 있었다.









