from django.urls import path
from coffeeSurvey import views

urlpatterns = [
    path('survey/', views.surveyFunc),
    path('surveyprocess', views.surveyProcess),
]
