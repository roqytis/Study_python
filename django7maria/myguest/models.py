from django.db import models

# Create your models here.
class Guest(models.Model):
    # myno = models.AutoField(auto_created = True, primary_key = True)  # 자동 생성 id 대신 pk를 직접 줌
    title = models.CharField(max_length=50)
    content = models.TextField()
    regdate = models.DateTimeField()
    
    class Meta:   # 정렬 처리 방법2
        #ordering=('title',)
        ordering=('-id',)
        