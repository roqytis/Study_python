from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
def mainFunc(request):
    return render(request, 'index.html')

class Callview(TemplateView):
    template_name = 'callget.html'
    
def insertFunc(request):
    if request.method == 'GET':
       return render(request, 'insert.html')
    elif request.method == 'POST':
        msg = request.POST.get("msg")
        #msg = request.POST["msg"] #위와 같은 얘기 
        return render(request, 'list.html',{'message':msg})
    else:
        print('요청에러')