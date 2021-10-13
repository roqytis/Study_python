from django.shortcuts import render
from myapp.models import Article

# Create your views here.
def main(request):
    return render(request, 'main.html')

def dbtest(request):
    datas = Article.objects.all()  # Django의 ORM  SQL의 select * from Article과 동일
    print(datas)
    
    return render(request, 'articlelist.html', {'articles':datas})