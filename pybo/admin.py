from django.contrib import admin
from .models import Question # 2024.03.14 추가

# Register your models here.

class QuestionAdmin(admin.ModelAdmin): # 2024.03.14 장고Admin에 데이터 검색기능추가하기
    search_fields = ['subject']

# admin.site.register(Question) # 2024.03.14 admin에서 관리 가능하도록 추가
admin.site.register(Question, QuestionAdmin) # class 내용으로 변경