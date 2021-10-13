from django.urls import path
from gpapp import views

urlpatterns = [    
    path('insert', views.insertFunc),  # 위임 받은 urls
  
]
