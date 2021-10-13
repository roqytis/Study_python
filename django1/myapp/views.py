from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
#얘가 컨트롤러 역할: 클라이언트의 요청을 urls.y가 받아서 컨트롤러로 전달해서 요청에 대한 처리
def index(request):
    msg = '장고 만세'
    ss = "<html><body>인덱스 요청 처리 %s</body></html>"%(msg)
    return HttpResponse(ss)

def helloFunc(request):
    ss = '홍길동'
    nai = '22'
    return render(request, 'show.html',{'name':ss, 'age':nai})

def worldFunc(request):
    
    return render(request, 'disp.html')