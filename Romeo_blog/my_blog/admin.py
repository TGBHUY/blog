from django.contrib import admin
from .models import *



class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','body','created_time','last_modified_time','likes','views','abstract','status','address','category']
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','created_time','last_modified_time']

admin.site.register(Article,ArticleAdmin)
admin.site.register(Category,CategoryAdmin)