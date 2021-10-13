#client source
'''
from socket import *

clientsock= socket(AF_INET,SOCK_STREAM)
clientsock.connect('127.0.0.1',7777)
clientsock.send('하이 반가워'.encode(encoding='utf-8'))
re_msg =clientsock.recv(1024).decode()
print('수신딘 자료:',re_msg)

clientsock.close()
'''

from socket import *

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('127.0.0.1', 7777))  # 해당 주소로 능동적으로 접속 시도
clientsock.send('하이 반가워'.encode(encoding='utf-8'))
re_msg = clientsock.recv(1024).decode()
print('수신된 자료 : ', re_msg)

clientsock.close()
