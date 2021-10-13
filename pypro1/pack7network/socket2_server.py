# 서버 서비스는 계속 진행
import socket
import sys

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 7777

try:
    serversock.bind((HOST, PORT))  # 192.168.35.231
    serversock.listen(5)
    print('server srart ...')
    
    while True:
        conn, addr = serversock.accept()
        print('client info : ', addr[0], addr[1])
        # 메세지 수신
        print(conn.recv(1024).decode())
        
        # 메세지 송신
        conn.send(('from server : ' + str(addr[0]) + 
                  ' 너도 잘지내라~').encode('utf-8'))
    
except Exception as e:
    print('err : ', e)
    sys.exit()
finally:
    conn.close()
    serversock.close()
    