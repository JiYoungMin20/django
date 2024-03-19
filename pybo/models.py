from django.db import models
from django.contrib.auth.models import User # 2024.03.19 author 필드 추가하기 위해

# 2024.03.14 추가
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 글쓴이 추가
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True) # 수정일자 추가

    def __str__(self):
        return self.subject

# 2024.03.14 추가
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 글쓴이 추가
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True) # 수정일자 추가