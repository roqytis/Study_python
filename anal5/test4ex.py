'''
* 카이제곱 검정

카이제곱 문제1) 부모학력 수준이 자녀의 진학여부와 관련이 있는가?를 가설검정하시오

  예제파일 : cleanDescriptive.csv

  칼럼 중 level - 부모의 학력수준, pass - 자녀의 대학 진학여부

  조건 : NA가 있는 행은 제외한다.
'''
import pandas as pd
import scipy.stats as stats

#귀무: 부모학력 수준이 자녀의 진학여부와 관련이 없다.
#대립: 부모학력 수준이 자녀이 진학여부와 관련이 있다. 

data1 = pd.read_csv('../testdata/cleanDescriptive.csv').dropna(subset=['level','pass'])
print(data1.head(2))
print(data1['level'].unique())
print(data1['pass'].unique())
ctab = pd.crosstab(index =data1['level'],columns = data1['pass'])
ctab.index=['고졸','대졸','대학원졸']
ctab.cloumns = ['합격','불합격']
print(ctab)
chi2, p, ddof, _ = stats.chi2_contingency(ctab)
print('chi2,p, ddof : ',chi2,p,ddof)
#귀무가설 성립

print('---------------------------')
'''
카이제곱 문제2) jikwon_jik과 jikwon_pay 간의 관련성 분석. 가설검정하시오.

  예제파일 : MariaDB의 jikwon table 

  jikwon_jik   (이사:1, 부장:2, 과장:3, 대리:4, 사원:5)

  jikwon_pay (1000 ~2999 :1, 3000 ~4999 :2, 5000 ~6999 :3, 7000 ~ :4)

  조건 : NA가 있는 행은 제외한다.
'''
import MySQLdb
import pandas as pd
import csv
import scipy.stats as stats

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123',
    'database': 'test',
    'port': 3306,
    'charset': 'utf8',
    'use_unicode': True
}

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwon_jik, jikwon_pay from jikwon
    """
    
    cursor.execute(sql)
    # for jik, pay in cursor:
    #     print(jik, pay)
        
    with open('jikwon.csv', 'w', encoding = "UTF-8") as fw:
        wr = csv.writer(fw)
        for row in cursor:
            wr.writerow(row)
        
    df = pd.read_csv('jikwon.csv', header = None, names = ('직급', '연봉'))
    
    def get_jik(v):
        if v == '이사':
            jik = 1
        elif v == '부장':
            jik = 2
        elif v == '과장':
            jik = 3
        elif v == '대리':
            jik = 4
        elif v == '사원':
            jik = 5
        return jik

    df['직급'] = df['직급'].apply(lambda v: get_jik(v)) 
    
    
    def get_pay(p):
        if p >= 1000 and p <= 2999:
            pay = 1
        elif p >= 3000 and p <= 4999:
            pay = 2
        elif p >= 5000 and p <= 6999:
            pay = 3
        elif p >= 7000:
            pay = 4
        return pay
    
    df['연봉'] = df['연봉'].apply(lambda p: get_pay(p))
        
    #print(df)
    
    data = pd.DataFrame(df)
   
    ctab = pd.crosstab(index = data['직급'], columns = data['연봉'])
    print(ctab)
    
    chi2, p, df, _ = stats.chi2_contingency(ctab)
    print('\nchi2 : ', chi2, '\np-value :', p, '\ndf : ', df)
    
    
except Exception as e:
    print('err : ', str(e))
finally:
    cursor.close()