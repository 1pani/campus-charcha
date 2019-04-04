from django import forms
from django.contrib.auth.models import User
from .models import Question,Answer,Comment,AnswerFlag

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserForm1(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

class upvote_downvote(forms.ModelForm):

    class Meta:
        model = AnswerFlag
        fields = ['q_id', 'username', 'up_flag', 'down_flag']

class add_question(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['question', 'q_dt']

class add_answer(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['q_id', 'q_dt', 'a_dt', 'username', 'question', 'answer']

class comment_form(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'ans_id']
