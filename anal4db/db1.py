#local db: sqlite
import sqlite3

sql = "create table if not exists test(product varchar(10), maker varchar(10), weight real, price integer)"

conn =  sqlite3.connect(':memory:')
conn.execute(sql)
conn.commit()

data = [('mouse','sanmsung',12.5,5000),('keyborad','lg',52.5,55000)]
stmt = "insert into test values(?,?,?,?)"
conn.executemany(stmt,data)
conn.commit()

cursor = conn.execute("select * from test")
rows = cursor.fetchall()
for a in rows:
    print(a)

print()
import pandas as pd
df1 =pd.DataFrame(rows,columns= ['product','maker','weight','price'])
print(df1)

print()

df2 = pd.read_sql("select * from test",conn)

# DataFramed의 자료를 db에 저장
data = {
    'product':['연필','볼펜','지우개'],
    'maker' :['모나미','모나미','모나미'],
    'weight':[1.5,5.5,12.3],
    'price':[500,1000,1500]
}
print(data)
df3 = pd.DataFrame(data)
print(df3)

df3.to_sql('test',conn, if_exists= 'append', index=False)

df4 = pd.read_sql("select * from test", conn)
print(df4)