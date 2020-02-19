"""bookdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# 项目的所有路由地址配置文件
# admin路由是 django 自带的后台管理路由

from django.contrib import admin
from django.urls import path,include

#路由 网址 每一个网址均需要绑定视图函数 视图函数给与页面返回
# 每一个路由都需要和视图函数绑定
# mvt V视图函数  3个作用 接受请求  处理数据  返回响应

# from django.http import HttpResponse
# def index(request):
#     return HttpResponse("这里是首页")
# def list(request):
#     return HttpResponse("这是列表页")
# def jsondata(request):
#     return HttpResponse("{'name':'lijiabin','age':'25'}")


urlpatterns = [
    path('admin/', admin.site.urls),
    #使用path将booktest的路由 进行包含

    path('polls/',include('polls.urls',namespace='polls')),
    path('',include('booktest.urls',namespace='booktest')),


    # 将admin路由与index视图数据绑定
    # path('index/',index),
    # path('list/',list),
    # path('json/',jsondata)
]

