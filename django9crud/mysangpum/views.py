from django.shortcuts import render
from mysangpum.models import Sangdata
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


# Create your views here.
def mainFunc(request):
    return render(request,'main.html')

def listFunc(request):
    ''' 페이지 처리가 없는 경우
    datas = Sangdata.objects.all()
    print(type(datas))
    return render(request, 'list.html', {'sangpums':datas})
    '''
    #페이지 처리가 있는경우
    datas =Sangdata.objects.all().order_by('-code')
    paginator =Paginator(datas, 5)
    
    try:
        page=request.GET.get('page')
    except:
        page = 1
    try:
        data= paginator.page(page)
    except PageNotAnInteger:
        data= paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages())
    
    #개별 페이지 표시용 작업
    allpage = range(paginator.num_pages + 1)
     #print('allpage :', allpage)  
    return render(request, 'list2.html', {'sangpums':data, 'allpage':allpage})
    
def insertFunc(request):
    return render(request,'insert.html')

def insertokFunc(request):
    if request.method =='POST':
        #code = request.POST.get('code')
        #print('code :', code)
        try:
            #새 코드 번호가 테이블에 이미 있으면 등록진해하지 않는다
            Sangdata.objects.get(code=request.POST.get('code'))
            return render(request, 'insert.html', {'msg':'이미 등록된 코드번호 입니다'})
        except Exception as e:
            #새 코드 번호가 없으면 등록 진행
            Sangdata(
                code = request.POST.get("code"),    
                sang = request.POST.get("sang"),    
                su = request.POST.get("su"),    
                dan = request.POST.get("dan"),    
            ).save()

    return HttpResponseRedirect('/sangpum/list')

def updateFunc(request):
    data = Sangdata.objects.get(code=request.GET.get('code'))
    return render(request, 'update.html', {'sang_one':data})

def updateokFunc(request):
    if request.method == 'POST':
        upRec = Sangdata.objects.get(code=request.POST.get('code'))
        upRec.code=request.POST.get('code')
        upRec.sang=request.POST.get('sang')
        upRec.su=request.POST.get('su')
        upRec.dan=request.POST.get('dan')
        upRec.save()
        
    return HttpResponseRedirect('/sangpum/list') #수정후  목록보기

def deleteFunc(request):
    delRec =Sangdata.objects.get(code=request.GET.get('code'))
    delRec.delete()
    return HttpResponseRedirect('/sangpum/list')

