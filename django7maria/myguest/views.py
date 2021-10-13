from django.shortcuts import render
from myguest.models import Guest
from datetime import datetime
from django.http.response import HttpResponseRedirect

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def listFunc(request):
    gdata = Guest.objects.all()  # 전체 레코드 읽기
    #정렬 처리 방법1
    #gdata = Guest.objects.all().order_by('title')  # title별 asc
    #gdata = Guest.objects.all().order_by('-title')  # title별 desc
    #gdata = Guest.objects.all().order_by('-id')  # id별 desc
    #gdata = Guest.objects.all().order_by('-id')[0:2]
    #gdata = Guest.objects.all().order_by('title', '-id') # title별 asc, id별 desc
    
    # 참고
    print(Guest.objects.get(id = 1))  # Guest object (1)
    print(Guest.objects.filter(id = 1))  # <QuerySet [<Guest: Guest object (1)>]>
    print(Guest.objects.filter(title = '연습')) # <QuerySet [<Guest: Guest object (1)>]>
    print(Guest.objects.filter(title__contains = '가을'))
    
    return render(request, 'list.html', {'gdatas':gdata})

def insertFunc(request):
    return render(request, 'insert.html')

def insertokFunc(request):
    if request.method == 'POST':
        #print(request.POST.get('title'))
        #print(request.POST['content'])
        
        # 추가 : insert into 테이블명 ... 를 ORM으로 처리
        Guest(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            regdate = datetime.now()
        ).save()
        
        # 수정
        # g = Guest.objects.get(id = 수정할id)
        # g.title = '수정할 값'
        # g.save()
        
        # 삭제
        # g = Guest.objects.get(id = 삭제할id)
        # g.delete()
    
    return HttpResponseRedirect('/guest/')  # 추가 후 목록 보기



    
