# 원격 DB와 연동

import MySQLdb
import pandas as pd
import numpy as np
import pickle
import csv


config = {}

try:
    with open('mydb.dat', mode='rb') as obj:
        config = pickle.load(obj)
        
except Exception as e:
    print('read err :', str(e))


try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwon_no, jikwon_name, buser_name, jikwon_jik, jikwon_gen, jikwon_pay
        from jikwon inner join buser on buser_num=buser_no
    """

    cursor.execute(sql)
    for a,b,c,d,e,f in cursor:
        print(a,b,c,d,e,f)
    
    
    # jikwon.csv 로 저장
    with open('jikwon.csv', 'w', encoding ='UTF-8') as fw:
        wr = csv.writer(fw)
        for row in cursor:
            wr.writerow(row)
        print('csv 저장 완료')
    
    # 자료읽기1) csv 읽기
    df = pd.read_csv('jikwon.csv', header = None, names = ('번호','이름','부서명','직급','성별','연봉'))
    print(df.head(3))    
    
    # 자료읽기2) SQL문으로 읽기
    df2 = pd.read_sql(sql, conn)
    df2.columns =('번호','이름','부서명','직급','성별','연봉')
    print(df2.head(3))
    
    print()
    print('전체 인원 수 :', len(df2))
    print('전체 인원 수 :', df2['이름'].count())
    
    print('직급별 인원 수 : \n', df2['직급'].value_counts())
    
    print('연봉 평균 : ', df2.loc[:, '연봉'].sum() / len(df2), ' ', df2.loc[:, '연봉'].mean())
    
    print('연봉이 8000 이상')
    print(df2.loc[df2['연봉'] >= 8000])
    
    print('연봉이 5000 이상')
    print(df2.loc[(df2['연봉'] >= 5000) & (df2['부서명'] == '영업부')])
    
    print('교차표---------------------')
    ctab = pd.crosstab(df2['성별'],df2['직급'],margins=True)
    print(ctab)
    
    print('groupby---------')
    print(df2.groupby(['성별','직급'])['이름'].count())
    
    print('pivot_table-----')
    print(df2.pivot_table(['연봉'], index = ['성별'], columns=['직급']))
    print(df2.pivot_table(['연봉'], index = ['성별'], columns=['직급'],aggfunc = [np.sum, np.mean]))
    
    #시각화
    import matplotlib.pyplot as plt
    plt.rc('font',family = 'malgun gothic')
    jik_ypay = df2.groupby(['직급'])['연봉'].mean()
    print(jik_ypay, type(jik_ypay))# <class 'pandas.core.series.Series'>
    print(jik_ypay.index) #Index(['과장', '대리', '부장', '사원', '이사'], dtype='object', name='직급')
    print(jik_ypay.values)     #[7200.         5064.28571429 8466.66666667 3476.92307692 9900.        ]
    plt.pie(jik_ypay,
            labels = jik_ypay.index,
            labeldistance=0.5,
            counterclock=False,
            explode=(0.2,0,0,0.2,0),
            shadow = True
            )
    
    plt.show()
except Exception as e:
    print('err : ', str(e))

finally:
    cursor.close()
    conn.close()
    
    