import socket
import threading
import sys

def handleFunc(socket):
    while True:
        data = socket.recv(1024)
        if not data: continue
        print(data.decode('utf-8'))
        
sys.stdout.flush() #버퍼를 비우기

name= input('채팅 아이디 입력:')
cs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cs.connect(('127.0.0.1',5555))
cs.send(name.encode('utf-8'))

th =threading.Thread(target=handleFunc, args =(cs, ))
th.start()

while True:
    msg =input('msg: ')
    sys.stdout.flush()
    if not msg:continue
    cs.send(msg.encode('utf-8'))
    
cs.close()