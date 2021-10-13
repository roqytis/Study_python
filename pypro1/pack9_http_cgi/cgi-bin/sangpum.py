import MySQLdb
import pickle
'''
with open('mydb.dat', 'rb') as obj:
    config = pickle.load(obj)
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

print('Content-Type:text/html;charset=utf-8\n')
print('<html><body><h2>상품 정보</h2>')
print('<table border="1">')
print('<tr><th>코드</th><th>상품명</th><th>수량</th><th>단가</th></tr>')
try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    cursor.execute("select * from sangdata")
    datas = cursor.fetchall()
    for code,sang,su,dan in datas:
        print('''
        <tr>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
        </tr>
        '''.format(str(code), sang, su, dan))
except Exception as err:
    print('오류 : ', err)
finally:
    cursor.close()
    conn.close()

print('</table>')
print('</body></html>')
