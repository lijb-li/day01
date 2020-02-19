from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):
    questions = Question.objects.all()
    return render(request,'polls/index.html',{"questions":questions})

def detail(request,qid):
    if request.method == "GET":
        try:
            question = Question.objects.get(id=qid)
            return render(request, 'polls/detail.html', {"question": question})
        except:
            return HttpResponse("问题不合法")
    elif request.method == "POST":
        choiceid = request.POST.get("num")
        try:
            choice = Choices.objects.get(id=choiceid)
            choice.votes += 1
            choice.save()
            # 返回当前投票问题的投票结果页
            url = reverse("polls:result",args=(qid,))
            # 投票成功 返回投票结果
            return redirect(to=url)

        except:
            return HttpResponse("选项不合法")

def result(request,qid):
    question = Question.objects.get(id=qid)
    return render(request,'polls/result.html',{"question":question})


