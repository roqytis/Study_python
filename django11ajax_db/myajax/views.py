from django.shortcuts import render
from myajax.models import Sangdata
from django.http.response import HttpResponse
import json

# Create your views here.
def mainFunc(reqeust):
    return render(reqeust,'main.html')

def listFunc(reqeust):
    return render(reqeust,'sanglist.html')

def listDbFunc(reqeust):
    sdata = Sangdata.objects.all()
    
    datas = []
    for s in sdata:
        dic = {'code':s.code,'sang':s.sang,'su':s.su,'dan':s.dan}
        datas.append(dic)
        
    return HttpResponse(json.dumps(datas), content_type='application/json')


