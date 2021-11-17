import MySQLdb
import pandas as pd
import numpy as np
import pickle
import csv

config = {}

try:
    with open('mydb.dat', 'rb') as obj:
        config = pickle.load(obj)
    
except Exception as e:
    print('read err : ', str(e))

try:
    conn = MySQLdb.connect(**config)
    cur = conn.cursor()
    sql = '''
        select jikwon_no,jikwon_name,buser_name,jikwon_pay,jikwon_jik
        from jikwon inner join buser on buser_num=buser_no
    '''
    
    cur.execute(sql)
    
    # 파일은 jikwon.csv로 저장
    with open('jikwon.csv','w',encoding='UTF-8') as fw:
        wr = csv.writer(fw) # sql 결과를 csv 파일로 작성할 writer(wr) 생성
        for row in cur: # sql 결과가 담긴 cur 에서 한 행씩 꺼내서
            wr.writerow(row) # wr를 이용해 한 행씩 csv파일로 작성
        print('csv 저장 완료')
        
    # csv 파일 읽어 DataFrame 생성
    df = pd.read_csv('jikwon.csv', header=None, names=('번호', '이름','부서명','연봉', '직급'))
    print(df.head(3))
    
    print('\n부서명별 연봉의 합, 연봉의 최대/최소값을 출력')
    print(df.groupby(['부서명'])['연봉'].sum())
    print(df.groupby(['부서명'])['연봉'].min())
    print(df.groupby(['부서명'])['연봉'].max())
    
    print('\n----------부서명, 직급 crosstab----------')
    ctab = pd.crosstab(df['부서명'],df['직급'], margins=True)
    print(ctab)
    
    # 직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력
    sql2 = '''
        select jikwon_no,gogek_no, gogek_name, gogek_tel
        from gogek inner join jikwon on jikwon_no=gogek_damsano
    '''
    
    cur.execute(sql2)
    df2 = pd.read_sql(sql2, conn) 
    df2.columns =('담당직원번호','고객번호', '고객명','고객전화')
    print(df2.head(3))
    
    import matplotlib.pyplot as plt
    plt.rc('font', family='malgun gothic')
    jik_ypay = df.groupby(['부서명'])['연봉'].mean() # 부서명별 연봉 평균
    print(jik_ypay)
    buser_name = jik_ypay.index
    print(buser_name)
    plt.barh(buser_name,jik_ypay)
    plt.xlabel("연봉 평균")
    plt.ylabel("부서명")
    plt.show()
    
except Exception as e:
    print('read err : ', str(e))
finally:
    cur.close()
    conn.close()