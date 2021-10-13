#chatserver 운영
#채팅 서버: 여러 개의 클라이언트와 소켓 통신을 스레드로 운영

import socket
import threading

ss=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('127.0.0.1',5555))
ss.listen(5)
print('채팅 서비스 시작~~')
users = [] # 채팅에 참여하는 클라이언트  기억장소

def chatUser(conn):
    name=conn.recv(1024)#채팅 아이디 받기
    data = '^^ ' +name.decode('utf-8')+'님 입장^^;'
    print(data) #서버에 출력
    
    try:
        for p in users:
            p.send(data.encode('utf-8'))
            
        while True: #접속 상태에서 수다 떨기
            msg= conn.recv(1024) #채팅 메세지 받기   
            data = name.decode('utf-8')+'님 메세지:'+msg.decode('utf-8')
            print('메세지 내용: ',data) #서버에 출력
            for p in users:
                p.send(data.encode('utf-8'))            
            
                    
    except:
        users.remove(conn)
        data = '~~ ' +name.decode('utf-8')+'님 퇴장 ~~'
        print(data)
        if users:
             for p in users:
                 p.send(data.encode('utf-8')) 
        else:
            print('exit')
               
while True:
    conn,addr = ss.accept()
    users.append(conn)
    th =threading.Thread(target=chatUser,args=(conn, ))
    th.start()    