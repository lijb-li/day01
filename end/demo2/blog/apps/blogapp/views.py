from django.shortcuts import render,redirect
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

def index(request):
    ads = Ads.objects.all()
    # locals可以返回作用域局部变量
    articles = Article.objects.all()
    paginator = Paginator(articles, 2)
    # 获取get请求中的页码参数  默认为1
    num = request.GET.get("pagenum", 1)
    page = paginator.get_page(num)
    return render(request, 'index.html', {"ads": ads, "page": page})

def detail(request,articleid):
    return render(request,'single.html')
    # return HttpResponse("文章"+articleid)
def contact(request):
    return render(request,'contact.html')

def favicon(request):
    return redirect(to="/static/favicon.ico")

