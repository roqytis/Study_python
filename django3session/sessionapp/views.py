from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from gevent.libev.corecext import NONE

# Create your views here.
def mainFunc(request):
    return render(request,'main.html')

def setosFunc(request):
    #request.session['키'] = '값' 세션에 값 저장
    # 변수 = request.session['키'] 세션 값 읽기
    
    if "favorite_os" in request.GET:
        print(request.GET['favorite_os'])
        request.session['f_os']=request.GET['favorite_os'] # 세션에 값 저장
        return HttpResponseRedirect('/showos') #showos 요청이 발생. 클라이언트를 통해 요청이 이루어짐 그래야 main의 urls.py를 만남
    else:
        return render(request, 'setos.html')

def showosFunc(request):
    context = {}
    
    if "f_os" in request.session:
        context['f_os']= request.session['f_os'] #세션 값 읽기
        context['message']= "그대가 선택한 운영체제는 %s"%request.session['f_os']
    else:
        context['f_os']= None
        context['message'] = "운영체제를 서택하지 않았어요"
        
    request.session.set_expiry(5) #세션의 유효시간 5초
    return render(request,'showos.html',context)

