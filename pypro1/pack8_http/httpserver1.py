# HttpServer: 기본적인 소켓연결을 관리 
#SimpleHTTPRequestHandler: 요청을 처리
from http.server import SimpleHTTPRequestHandler,HTTPServer

port = 7777

handler =SimpleHTTPRequestHandler
serv = HTTPServer(('127.0.0.1',port),handler)
print('웹 서비스 시작...')
serv.serve_forever()