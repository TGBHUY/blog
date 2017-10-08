#conding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),      #主页
    url(r'^index/$', views.index),#主页
    url(r'^blog_(\d+)/$', views.blog),  # 博客详情页
    url(r'^blog_comment/$', views.comment),  # 评论
    url(r'^bloglist_(\d+)/$', views.bloglist),  #博客列表
    url(r'^csdn_spider', views.csdn_spider),
    url(r"",views.notfound)
]