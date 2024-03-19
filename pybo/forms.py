from django import forms
from pybo.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']

        """ 
        forms.as_p 자동 생성하는 부분을 수작업으로 폼 작성하기 위해 주석 처리
        
        widgets = {  # 폼에 부트스트랩 css 적용하기
            'subject' : forms.TextInput(attrs={'class': 'form-control'}),
            'content' : forms.Textarea(attrs={'class': 'form-control', 'rows':4}),
        }
        """

        labels = { # label 속성 수정. Subject,COntent로 한글로 바꾸자
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }