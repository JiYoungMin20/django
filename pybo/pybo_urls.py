# 2024.03.14 생성

from django.urls import path
from . import views

app_name = 'pybo'  # 2024.03.14 namespace 추가 

urlpatterns = [
    path('', views.index, name='index'), # 2024.03.13 우아한URL을 위해 name 속성 추가
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'), # 2024.03.15 질문등록기능 추가
]
