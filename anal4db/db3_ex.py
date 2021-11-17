import MySQLdb
import pandas as pd
import numpy as np
import pickle
import csv

config={}

try:
    with open('mydb.dat', 'rb') as obj:
        config=pickle.load(obj)
except Exception as e:
    print('err: ', str(e))
    
try:
    conn= MySQLdb.connect(**config)
    cursor=conn.cursor()
    sql="""
        select jikwon_no, jikwon_name, buser_name, jikwon_pay, jikwon_jik from jikwon
        inner join buser on buser_num=buser_no
        """
    cursor.execute(sql)
    rows=cursor.fetchall()
    # for a in rows:
    #     print(a)
    
    #1  
    df=pd.DataFrame(rows, columns=['사번', '이름', '부서명', '연봉', '직급'])
    print(df.head(2))
    
    #2
    with open('jikwon.csv', 'w', encoding='UTF-8') as fw:
        wr=csv.writer(fw)
        for rows in cursor:
            wr.writerow(rows)
        print('csv 저장 완료')

    #3
    chong=df.loc[df['부서명']=='총무부']
    yung=df.loc[df['부서명']=='영업부']
    jun=df.loc[df['부서명']=='전산부']
    kwan=df.loc[df['부서명']=='관리부']
    
    print('총무부 연봉 합계: ', chong.loc[:,'연봉'].sum(), '연봉최대값: ', chong.loc[:,'연봉'].max(), '연봉최소값: ', chong.loc[:,'연봉'].min())
    print('영업부 연봉 합계: ', yung.loc[:,'연봉'].sum(), '연봉최대값: ', yung.loc[:,'연봉'].max(), '연봉최소값: ', yung.loc[:,'연봉'].min())
    print('전산부 연봉 합계: ', jun.loc[:,'연봉'].sum(), '연봉최대값: ', jun.loc[:,'연봉'].max(), '연봉최소값: ', jun.loc[:,'연봉'].min())
    print('관리부 연봉 합계: ', kwan.loc[:,'연봉'].sum(), '연봉최대값: ', kwan.loc[:,'연봉'].max(), '연봉최소값: ', kwan.loc[:,'연봉'].min())
    print('부서명별 연봉의 합 : ', df.groupby(['부서명'])['연봉'].sum())
    
    #4
    cd=pd.crosstab(df.부서명, df.직급, margins=True)
    print(cd)
    
    # 직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력
    # print(df.index[0])
    # print(df['사번'][1])
    #print(df.index)
    
    for i in range(len(df.index)):
        sql2 = """
            select gogek_no,gogek_name,gogek_tel from gogek
            inner join jikwon on gogek.gogek_damsano = jikwon.jikwon_no
            where jikwon_no={}
        """.format(str(df.index[i + 1]))
        #print(sql2)
        cursor.execute(sql2)
        result = cursor.fetchone()
        #print(result)
        if result == None:
            print(df['이름'][i + 1], "담당고객 X")
        else:
            print(df['이름'][i + 1], "직원의 담당고객 정보")
            df2 = pd.read_sql(sql2, conn)
            df2.columns = ['고객번호','고객명','전화']
            df2.set_index('고객번호', inplace = True)
            print(df2)
            
        
    
except Exception as e:
    print('err: ', str(e))
finally:
    cursor.close()
    conn.close()
