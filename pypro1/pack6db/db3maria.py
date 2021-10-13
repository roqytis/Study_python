#원격 데이터 베이스 연동 프로그래밍 : MariaDB
#pip install mysqlclient
import MySQLdb
'''
conn = MySQLdb.connect(host = '127.0.0.1', user = 'root', password='123', database='test', port= 3306)
print(conn)
conn.close
'''

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
    conn= MySQLdb.connect(**config)
    print(conn)
    cursor =conn.cursor()
    '''
    #자료추가
    sql="insert into sangdata(code,sang,su,dan) values (%s,%s,%s,%s)"
    sql_input_data=('10','아메리카노',5,5000)
    cursor.execute(sql,sql_input_data)
    conn.commit()
    '''
    '''
    #자료수정
    sql = "update sangdata set sang=%s,su=%s,dan=%s where code=%s"
    sql_update_data=('냉수',25,6000,'10')
    result = cursor.execute(sql,sql_update_data)
    print('result :', result)
    conn.commit()
    '''
    #자료삭제 방법 1
    sql = "delete from sangdata where code=%s"
    sql_delete_data='10'
    result = cursor.execute(sql,(sql_delete_data,))

    #자료삭제 방법 2
    sql_delete_data='10'
    sql = "delete from sangdata where code={0}".format(sql_delete_data)
    result = cursor.execute(sql)
    
    
    if result== 0:
        print('삭제된 자료가 없어요')
    else:
        print('삭제 성공')
    conn.commit()
    
    
    # 자료 읽기
    sql = "select * from sangdata"
    cursor.execute(sql)
    
    for data in cursor.fetchall():
        #print(data)
        print('%s %s %s %s'%data)
    '''   
    print()
    for aa in cursor:
        print(aa[0],aa[1],aa[2],aa[3])
        
    print()
    for (code,sang,su,dan) in cursor:
        print(code, sang, su, dan)

    print()
    for (a,b,c,d) in cursor:
        print(a,b,c,d)
    '''   
except Exception as e:
    print('err: ', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()