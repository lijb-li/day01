from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
# Create your views here.

# Django自带了分页与分页器
from django.core.paginator import Paginator,Page
# 一个Page中有  object_list代表当前页的所有对象
# has_next 是不是有下一页
# has_previous 是否有上一页
# next_page_number 下一页的编号
# previous_page_number 上一页的编号
# self.number 当前页的编号
# self.paginator 当前页的分页器

# 一个Paginator中的object_list 代表所有未分页对象
# self.per_page 每一页有几个对象
# get_page(self, number): 从分页器中取第几页
# page_range(self): 返回分页列表

from .models import *
from .forms import *
def index(request):
    ads = Ads.objects.all()
    # locals可以返回作用域局部变量
    typepage = request.GET.get("type")
    year = None
    month = None
    categoty_id = None
    if typepage == "date":
        year = request.GET.get("year")
        month = request.GET.get("month")
        articles = Article.objects.filter(create_time__year = year,create_time__month = month).order_by("-create_time")
    elif typepage =="category":
        category_id = request.GET.get("category_id")
        try:
            catrgory = Category.objects.get(id=category_id)
            articles = catrgory.article_set.all()
        except Exception as e:
            print(e)
            return HttpResponse("分类不合法")

    elif typepage == "tag":
        tag_id = request.GET.get("tag_id")
        try:
            tag = Tag.objects.get(id=tag_id)
            articles = tag.article_set.all()
        except Exception as e:
            print(e)
            return HttpResponse("标签不合法")

    else:
        articles = Article.objects.all().order_by("-create_time")

    paginator = Paginator(articles, 2)
    # 获取get请求中的页码参数  默认为1
    num = request.GET.get("pagenum", 1)
    page = paginator.get_page(num)
    return render(request,'index.html',locals())
    # return render(request, 'index.html', {"ads": ads, "page": page, "type":typepage,"year":year,"month":month})

def detail(request,articleid):
    if request.method == "GET":
        try:
            article = Article.objects.get(id=articleid)
            cf = CommentForm()
            return render(request,'single.html',locals())
        except Exception as e:
            print(e)
            return HttpResponse("文章不合法")
    elif request.method == "POST":
        cf = CommentForm(request.POST)
        if cf.is_valid():
            print(cf)
            comment = cf.save(commit=False)
            comment.article = Article.objects.get(id=articleid)
            comment.save()
            url = reverse("blogapp:detail",args=(articleid,))
            return redirect(to=url)
        else:
            article = Article.objects.get(id=articleid)
            cf = CommentForm()
            errors = "输入信息有误"
            return render(request,'sing.html',locals())

    # return HttpResponse("文章"+articleid)
def contact(request):
    return render(request,'contact.html')

def favicon(request):
    return redirect(to="/static/favicon.ico")

