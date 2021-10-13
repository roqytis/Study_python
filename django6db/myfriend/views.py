from django.shortcuts import render
from myfriend.models import Friend


# Create your views here.
def main(request):
    return render(request, 'main.html')

def dbtest(request):
    datas = Friend.objects.all()  # Django의 ORM  SQL의 select * from Article과 동일
    print(datas)
    
    return render(request, 'friendlist.html', {'friends':datas})

#아이디, 비번 friend1 ,end12345