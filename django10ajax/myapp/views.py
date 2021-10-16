from django.shortcuts import render
from django.http.response import HttpResponse

#연습용 dict data
lan = {
     'id':111,
     'name': '파이썬',
     'history':[
         {'date':'2021-5-1','exam':'basic'},     
         {'date':'2021-6-1','exam':'django'},     
    ]
}

import json

def testFunc():
    print(type(lan)) #<class 'dict'>
    
    #JSON 인코딩: dict -> str로 변경
    jsonString = json.dumps(lan)
    print(jsonString, type(jsonString)) #<class 'str'>
    
    #JSON 디코딩 : str -> dict로 변경
    dic = json.loads(jsonString)
    print(type(dic))
    print(dic)
    print(dic['name'])
    
# Create your views here.
def indexFunc(request):
    #참고로 파이썬 인코딩/디코딩
    testFunc()
    
    return render(request,'abc.html')

import time

def func1(request):
    msg = request.GET.get('msg')
    msg = 'nice ' + msg
    print(msg)
    
    time.sleep(5) #지연시간 일부러 줌
    
    context={'key' :msg} # dict type : 그런데 web을 전송할떄는 str로 바꿔 이진처리해서 전송
    return HttpResponse(json.dumps(context), content_type='application/json')

def func2(request):
    datas=[
        {'irum':'홍길동', 'nai':22},
        {'irum':'고길동', 'nai':25},
        {'irum':'신길동', 'nai':32}
    ]  
    print(type(datas))
    return HttpResponse(json.dumps(datas), content_type='application/json')

def func3(request):
    datas= [
        {'irum':'박소영', 'nai':22},
        {'irum':'박정수', 'nai':25},
        {'irum':'방준영', 'nai':32}
    ]  
    print(type(datas))
    return HttpResponse(json.dumps(datas), content_type='application/json')






