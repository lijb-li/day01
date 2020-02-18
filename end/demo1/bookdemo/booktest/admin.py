from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.

# django自带的后台管理操作需要在此实现
from .models import Book,Hero,User

class HeroInline(admin.StackedInline):
    model = Hero
    extra = 1

class HeroAdmin(ModelAdmin):
    list_display = ('name','gender','content')

    search_fields = ('name', 'gender','content','book')

admin.site.register(Hero,HeroAdmin)

class BookAdmin(ModelAdmin):
    list_display = ('title','price','pub_date')

    search_fields = ('title','price')

    list_filter = ('title','price')
admin.site.register(Book,BookAdmin)


admin.site.register(User)

