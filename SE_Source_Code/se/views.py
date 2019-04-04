from django.shortcuts import render
from .forms import UserForm,UserForm1,add_question,add_answer,comment_form,upvote_downvote
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from .models import Topic,Question,Answer,Comment,AnswerFlag
from django.shortcuts import redirect
import datetime as dt


def login_page(request):
    return render(request, 'se/login.html')
def home_page(request):
    hi = request.user
    if hi.is_authenticated :
        topics = Topic.objects.all()
        return render(request, 'se/index.html',{'topics': topics})
    return render(request, 'se/login.html')
def topic_page(request):
    hi = request.user
    if hi.is_authenticated:
        questions = Question.objects.all()
        answers = Answer.objects.all()
        comments = Comment.objects.all()
        return render(request, 'se/question.html', {'questions': questions,'answers': answers, 'user':hi ,'comments':comments} )
    return render(request, 'se/login.html')

def UserFormView(request):
    form = UserForm(request.POST)
    if form.is_valid():

        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/home/', user)

    return render(request, 'se/login.html')

def logout_view(request):
    logout(request)
    return redirect('/index/')

def question(request):
    form = add_question(request.POST)
    if form.is_valid():
        question = form.cleaned_data['question']
        qdt = str(dt.datetime.now())
        Question.objects.create(
            question=question,
            q_dt=qdt
        )
        questions = Question.objects.all()
        answers = Answer.objects.all()
        return redirect('/topic', questions,answers)

def answer(request):
    form = add_answer(request.POST)
    if form.is_valid():
        q_id = form.cleaned_data['q_id']
        qdt = form.cleaned_data['q_dt']
        adt = str(dt.datetime.now())
        username = form.cleaned_data['username']
        question = form.cleaned_data['question']
        answer = form.cleaned_data['answer']
        Question.objects.filter(id = q_id).delete()
        Answer.objects.create(
            q_id=q_id,
            q_dt=qdt,
            a_dt=adt,
            username=username,
            question=question,
            answer=answer

        )
        questions = Question.objects.all()
        answers = Answer.objects.all()
        return redirect('/topic', questions,answers)

def comment_view(request):
    form = comment_form(request.POST)
    if form.is_valid():
        comment = form.cleaned_data['comment']
        ans_id = form.cleaned_data['ans_id']
        Comment.objects.create(
            comment = comment,
            ans_id = ans_id

        )
        questions = Question.objects.all()
        answers = Answer.objects.all()
        return redirect('/topic', questions,answers)

def upvote_view(request):
    form = upvote_downvote(request.POST)
    if form.is_valid():
        q_id = form.cleaned_data['q_id']
        username = form.cleaned_data['username']
        if not AnswerFlag.objects.filter(q_id=q_id, username=username):
            AnswerFlag.objects.create(
                q_id = q_id,
                username= username,
                up_flag=True,
                down_flag=False
            )
            temp = Answer.objects.filter(q_id=q_id)[:1].get().upvotes
            Answer.objects.filter(q_id=q_id).update(upvotes=temp+1)

        else:
            if AnswerFlag.objects.filter(q_id=q_id, username=username)[:1].get().up_flag==True and AnswerFlag.objects.filter(q_id=q_id, username=username)[:1].get().down_flag==False:

                AnswerFlag.objects.filter(q_id=q_id, username=username).update(up_flag=False)

                temp = Answer.objects.filter(q_id=q_id)[:1].get().upvotes
                Answer.objects.filter(q_id=q_id).update(upvotes=temp - 1)
            elif AnswerFlag.objects.filter(q_id=q_id, username=username)[:1].get().up_flag==False and AnswerFlag.objects.filter(q_id=q_id, username=username)[:1].get().down_flag==True:

                AnswerFlag.objects.filter(q_id=q_id, username=username).update(up_flag=True)

                temp = Answer.objects.filter(q_id=q_id)[:1].get().upvotes
                Answer.objects.filter(q_id=q_id).update(upvotes=temp + 1)

                AnswerFlag.objects.filter(q_id=q_id, username=username).update(down_flag=False)

                temp = Answer.objects.filter(q_id=q_id)[:1].get().downvotes
                Answer.objects.filter(q_id=q_id).update(downvotes=temp - 1)
            else:

                AnswerFlag.objects.filter(q_id=q_id, username=username).update(up_flag=True)

                temp = Answer.objects.filter(q_id=q_id)[:1].get().upvotes
                Answer.objects.filter(q_id=q_id).update(upvotes=temp + 1)
        questions = Question.objects.all()
        answers = Answer.objects.all()
        return redirect('/topic', questions, answers)


def downvote_view(request):
    form = upvote_downvote(request.POST)
    if form.is_valid():
        q_id = form.cleaned_data['q_id']
        username = form.cleaned_data['username']
        if not AnswerFlag.objects.filter(q_id=q_id, username=username):
            AnswerFlag.objects.create(
                q_id=q_id,
                username=username,
                up_flag=False,
                down_flag=True
            )
            temp = Answer.objects.filter(q_id=q_id)[:1].get().downvotes
            Answer.objects.filter(q_id=q_id).update(downvotes=temp + 1)

        else:
            if AnswerFlag.objects.filter(q_id=q_id, username=username)[:1].get().up_flag == True and \
                    AnswerFlag.objects.filter(q_id=q_id, username=username)[:1].get().down_flag == False:

                AnswerFlag.objects.filter(q_id=q_id, username=username).update(up_flag=False)

                temp = Answer.objects.filter(q_id=q_id)[:1].get().upvotes
                Answer.objects.filter(q_id=q_id).update(upvotes=temp - 1)

                AnswerFlag.objects.filter(q_id=q_id, username=username).update(down_flag=True)

                temp = Answer.objects.filter(q_id=q_id)[:1].get().downvotes
                Answer.objects.filter(q_id=q_id).update(downvotes=temp + 1)
            elif AnswerFlag.objects.filter(q_id=q_id, username=username)[:1].get().up_flag == False and \
                    AnswerFlag.objects.filter(q_id=q_id, username=username)[:1].get().down_flag == True:

                AnswerFlag.objects.filter(q_id=q_id, username=username).update(down_flag=False)

                temp = Answer.objects.filter(q_id=q_id)[:1].get().downvotes
                Answer.objects.filter(q_id=q_id).update(downvotes=temp - 1)
            else:

                AnswerFlag.objects.filter(q_id=q_id, username=username).update(down_flag=True)

                temp = Answer.objects.filter(q_id=q_id)[:1].get().downvotes
                Answer.objects.filter(q_id=q_id).update(downvotes=temp + 1)
        questions = Question.objects.all()
        answers = Answer.objects.all()
        return redirect('/topic', questions, answers)

