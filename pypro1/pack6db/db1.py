# 데이터 연동 프로그래밍
# 개인용 DBMS : sqlite <- 파이썬 설치시 자동 등록. 기본 모듈로 (라이브러리)로 제공
import sqlite3
print(sqlite3.sqlite_version)

print()
#conn=sqlite3.connect('exam.db') #db 파일 생성
conn=sqlite3.connect(':memory:') #ram 파일 생성

try:
    cur= conn.cursor() #SQL 처리가능 객체
    
    cur.execute("create table if not exists friends(name text, phone text, addr text)")
    cur.execute("insert into friends(name,phone,addr) values('한국인','111-111','강남구 역삼동')")
    cur.execute("insert into friends values('이상한','222-111','강남구 서초동')")
    inputdata= ('유비','333-3333','그 동네')
    cur.execute("insert into friends values(?,?,?)", inputdata)
    conn.commit()
    
    #select
    cur.execute("select*from friends") #select의 결과를 커서가 기억함
    #print(cur.fetchone())
    print(cur.fetchall())
    
except Exception as e:
    print('err : ',e)
finally:
    cur.close()
    conn.close()