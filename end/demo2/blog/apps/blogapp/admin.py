from django.contrib import admin
from django.contrib.admin import ModelAdmin
# Register your models here.
from .models import Ads,Category,Tag,Article,Comment

admin.site.register(Ads)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(Comment)


