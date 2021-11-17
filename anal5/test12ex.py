# [ANOVA 예제 1]
# 빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.
# 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.
# 조건 : NaN이 들어 있는 행은 해당 칼럼의 평균값으로 대체하여 사용한다.
import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

#귀무:기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하지 않는다.
#대립:기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재한다.

data = pd.read_csv('anovaex1.txt', sep=" ")
data.columns = ['종류','양']
print(data.head(6))
print(data.isnull().sum())   # 결측값 존재 여부 확인

data = data.fillna(data.mean())    # 평균으로 NaN값 대체
#data = data.fillna(data['양'].mean())  # 위와 동일

#print(data.head(6))
oil1 = data[data['종류'] == 1]
oil2 = data[data['종류'] == 2]
oil3 = data[data['종류'] == 3]
oil4 = data[data['종류'] == 4]

#print(oil1)
print(stats.ks_2samp(oil1['양'], oil2['양']))   # pvalue=0.9307359307359307
print("정규성 검정 : ",stats.shapiro(oil1['양'])) # 0.8680403232574463  정규성 만족
print("정규성 검정 : ",stats.shapiro(oil2['양']))
print("정규성 검정 : ",stats.shapiro(oil3['양']))
print("정규성 검정 : ",stats.shapiro(oil4['양'])) 

print('등분산성 확인 :', stats.levene(oil1['양'], oil2['양'], oil3['양'], oil4['양']).pvalue) # 0.32689 등분산성 만족
print()
print('방법 1')
f_sta, p_val = stats.f_oneway(oil1['양'], oil2['양'], oil3['양'], oil4['양'])
print("p-value : {}".format(p_val))    # p > 0.05이므로 귀무가설 채택 

print()
print('방법 2')
data = pd.DataFrame(data, columns=['종류','양'])
#print(data.head(3))
lmodel = ols('양 ~ C(종류)', data).fit()
print(anova_lm(lmodel))      # PR(>F) 0.848244  > 0.05이므로 귀무가설 채택


# [ANOVA 예제 2]
# DB에 저장된 buser와 jikwon 테이블을 이용하여 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있는지 검정하시오.
# 만약에 연봉이 없는 직원이 있다면 작업에서 제외한다.
# 귀무가설 : 총무부, 영업부, 전산부, 관리부의 연봉에 차이가 없다
# 대립가설 : 총무부, 영업부, 전산부, 관리부의 연봉에 차이가 있다

import MySQLdb
import pandas as pd
import numpy as np
import pickle
import csv
import scipy.stats as stats
import matplotlib.pyplot as plt

try:
    with open('mydb.dat', 'rb') as obj:
        # pickle.dump(config, obj)
        config = pickle.load(obj)    
except Exception as e:
    print('read err : ', str(e))

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwon_pay, buser_num from jikwon 
    """
    cursor.execute(sql)
    df = cursor.fetchall()
    df = pd.DataFrame(df, columns = ['연봉', '부서'])
    sp = np.array(df.iloc[:,[0,1]])
    print(sp)
    
    a1 = sp[sp[:,1] == 10, 0]
    a2 = sp[sp[:,1] == 20, 0]
    a3 = sp[sp[:,1] == 30, 0]
    a4 = sp[sp[:,1] == 40, 0]
  
    # 정규성
    print('총무부와 영업부의 정규성 : ', stats.ks_2samp(a1, a2).pvalue)   # pvalue=0.3357 > 0.05 만족
    print('총무부와 전산부의 정규성 : ', stats.ks_2samp(a1, a3).pvalue)   # pvalue=0.5751 > 0.05 만족 
    print('총무부와 관리부의 정규성 : ', stats.ks_2samp(a1, a4).pvalue)   # pvalue=0.5363 > 0.05 만족
    print('영업부와 전산부의 정규성 : ', stats.ks_2samp(a2, a3).pvalue)   # pvalue=0.3357 > 0.05 만족
    print('영업부와 관리부의 정규성 : ', stats.ks_2samp(a2, a4).pvalue)   # pvalue=0.6406 > 0.05 만족
    print('전산부와 관리부의 정규성 : ', stats.ks_2samp(a3, a4).pvalue)   # pvalue=0.5363 > 0.05 만족
    
    spp = df.loc[:, ['연봉', '부서']]
    print(spp.groupby('부서').mean())
    #             연봉
    # 부서             
    # 10  5414.285714
    # 20  4908.333333
    # 30  5328.571429
    # 40  6262.500000
    
    #등분산성
    print(stats.levene(a1, a2, a3, a4)) # pvalue=0.7980
    print(stats.bartlett(a1, a2, a3, a4)) # pvalue=0.6290
    
    # 부서별 연봉 평균
    print('총무부 연봉 평균 : ', np.mean(a1))
    print('영업부 연봉 평균 : ', np.mean(a2))
    print('전산부 연봉 평균 : ', np.mean(a3))
    print('관리부 연봉 평균 : ', np.mean(a4)) 
    print(pd.pivot_table(spp, index = ['부서'], aggfunc = 'mean'))
    
    # 분산분석
    print(stats.f_oneway(a1,a2,a3,a4))
    # F_onewayResult(statistic=0.41244077160708414, pvalue=0.7454421884076983)
    # pvalue=0.7454421884076983 > 0.05이므로 귀무가설 채택
    # 귀무가설 : 총무부, 영업부, 전산부, 관리부의 연봉에 차이가 없다 
    
    
    # 정규성
    print(stats.kruskal(a1,a2,a3,a4))
    # KruskalResult(statistic=1.671252253685445, pvalue=0.6433438752252654)
    # pvalue=0.6433438752252654 > 0.05
    
    # 등분산성
    from pingouin import welch_anova
    print(welch_anova(data = df, dv = '연봉', between = '부서'))    
    #   Source  ddof1      ddof2         F     p-unc       np2
    # 0     부서      3  10.304681  0.339809  0.797119  0.045427
    
    # 사후 분석
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    result = pairwise_tukeyhsd(spp['연봉'], spp['부서'], alpha = 0.05)
    print(result)
    
    # 시각화
    result.plot_simultaneous(xlabel = 'pay', ylabel = 'buser')
    plt.show()
    
except Exception as e:
    print('err : ', str(e))
    conn.rollback()
finally:
    cursor.close()
    conn.close()    