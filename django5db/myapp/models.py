from django.db import models

# Create your models here.  # 테이블을 클래스로 정의
class Article(models.Model):
    code = models.CharField(max_length=10)  # CharField, TextField, DateTimeField, IntegerField, ...
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    pub_date = models.DateTimeField()
    #아이디 japan123
    #비번 korea123
    '''
    1번 . cd C:\work\psou\django5db
    2번 . dir
    3번 . python manage.py createsuperuser *이거 꼭 알아두기
    4번 . 그리고 아이디 비번 외우기
    5번 . http://127.0.0.1:8000/admin/ 그리고 들어가기
    '''