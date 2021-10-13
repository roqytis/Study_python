# 단순한 서버 구축: 클라이언트의 요청에 1회만 반응
from socket import *

serversock =socket(AF_INET, SOCK_STREAM) #소켓의 종류 AF_INET socket(소켓종류, 소켓유형)
serversock.bind(('127.0.0.1', 8888)) #소켓의 컴 주소에 바인딩
serversock.listen(1) #클라이언트와의 연결 정보수 :1~5까지 가능
print('서버 서비스 시작...')

conn,addr=serversock.accept()
print('client addr :', addr)
print('from client msg : ', conn.recv(1024).decode())
conn.close()
serversock.close()