# 가설검정 총 정리 : chi2, t검정 ,ANOVA
#부서와 직원자료사용

import MySQLdb
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import scipy.stats as stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

try:
    with open('mydb.dat', 'rb') as obj:
        # pickle.dump(config, obj)
        config = pickle.load(obj)
except Exception as e:
    print('read err : ', str(e))

conn = MySQLdb.connect(**config)
cursur = conn.cursor()

print('교차분석(이원 카이제곱):각 부서(범주형)와 직원평가점수(범주형) 간의 관련성 분석')
#독립변수 : 범주형 , 종속변수 : 범주형
#귀무 : 각 부서와 직원평가 점수간에 관련이 없다.
#대립 : 각 부서와 직원평가 점수간에 관련이 있다.

df = pd.read_sql("select * from jikwon",conn)
print(df.head(3))
buser = df['buser_num']
rating = df['jikwon_rating']
ctab = pd.crosstab(buser, rating)
print(ctab)

chi, p, df, exp = stats.chi2_contingency(ctab)
print('chi:{}, p:{}, df:{}'.format(chi,p,df)) #p값(유의확률):0.29060 > 0.05(유의수준. 95% 신회구간)이므로 귀무 채택

print('차이분석(t-test):10, 20 부서(범주형)와 직원평균연봉(연속형) 간의 관련성 분석')
#독립변수 : 범주형 , 종속변수 : 연속형
#귀무 : 두 부서 간 평균연봉에 차이가 없다.
#대립 : 두 부서 간 평균연봉에 차이가 있다.
df_10 = pd.read_sql("select buser_num,jikwon_pay from jikwon where buser_num=10",conn)
df_20 = pd.read_sql("select buser_num,jikwon_pay from jikwon where buser_num=20",conn)
#print(df_10)
#print(df_20)
buser10 = df_10['jikwon_pay']
buser20 = df_20['jikwon_pay']
print(np.mean(buser10),' ',np.mean(buser20)) #5414.285714285715   4908.333333333333
print(stats.ttest_ind(buser10, buser20))
#Ttest_indResult(statistic=0.4585177708256519, pvalue=0.6523879191675446)
#pvalue=0.6523 > 0.05 이므로 귀무 가설 채택, 두 부서 간 평균 연봉에 차이가 없다.

print('분산분석(ANOVA): 부서(10,20,30,40 : 부서요인 하나에 4개의 그룹)의 직원평균연봉(연속형) 간의 차이를 분석---')
#독립변수 :범주형, 종속변수 : 연속형
#요인에 대한 집단이 3개 이상
#귀무 :4개의 부서 간 평균 연봉에 차이가 없다.
#대립 :4개의 부서 간 평균 연봉에 차이가 있다.
df3 = pd.read_sql("select buser_num,jikwon_pay from jikwon", conn)
buser = df3['buser_num']
pay = df3['jikwon_pay']

gr1 = df3[df3['buser_num'] == 10]['jikwon_pay']
gr2 = df3[df3['buser_num'] == 20]['jikwon_pay']
gr3 = df3[df3['buser_num'] == 30]['jikwon_pay']
gr4 = df3[df3['buser_num'] == 40]['jikwon_pay']
print(np.mean(gr1), ' ',np.mean(gr2), ' ',np.mean(gr3), ' ',np.mean(gr4)) #5414.285714285715   4908.333333333333   5328.571428571428   6262.5

#시각화
plt.boxplot([gr1,gr2,gr3,gr4])
plt.show()

#방버1
f_sta,pv =stats.f_oneway(gr1,gr2,gr3,gr4)
print(('f_sta, pv:', f_sta, pv))

#방법2 
lmodel = ols('jikwon_pay ~C(buser_num)',data = df3).fit()
result = anova_lm(lmodel,type=2)
print(result) #PR(>F) : 0.745442

#사후검정
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tk = pairwise_tukeyhsd(df3.jikwon_pay,df3.buser_num,alpha = 0.05)
print(tk)

tk.plot_simultaneous()
plt.show()
