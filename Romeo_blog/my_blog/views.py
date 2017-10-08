# encoding: utf-8
import re

from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator,Page
from django.http import JsonResponse
from bs4 import BeautifulSoup
import requests
import json
from lxml import etree
# import jsonpath
# Create your views here.
#Article
def fun(x):
    #用来给ｃｓｄｎ解析
    return (''.join((x.xpath('string(.)').strip()).split()))

def bloglist(request,pindex):
    #博客
    blog_list = Article.objects.all()

    paginator=Paginator(blog_list,2)
    # 取到当前页

    page_blog=paginator.page(int(pindex))

    context = {
        "page_blog":page_blog,#当前页博客
        "paginator":paginator,#页
    }

    return render(request, "bloglist.html", context)

def index(request):

    return render(request,"index.html",{"index":True})

def blog(request,id):
    print("－－进入博客视图－－")
    blog = Article.objects.filter(id=id)
    comments = Comment.objects.filter(blog_id=id)
    context = {
        "blogs":blog,
        "comments":comments,
        "comment_len":len(comments)
    }
    print("－－博客加载完毕－－")
    return render(request,"blog.html",context)

def comment(request):
    print("－－评论写入数据库中－－")
    data = request.GET

    #保存评论名字，内容，博客的Ｉｄ
    username = data.get("username")
    id = data.get("id")
    textarea = data.get("textarea")
    obj = Comment.objects.create(name=username, comment_con=textarea,blog_id=id)
    obj.save()

    #读取写入数据的时间
    latest_obj = Comment.objects.filter(blog_id=id).latest("id")
    latest_time = latest_obj.created_time.strftime('%Y-%m-%d %H:%M:%S')

    context={
        "latest_time":latest_time
    }
    print("－－评论视图结束－－")
    return JsonResponse(context)

def csdn_spider(request):
    print("－－CSDN－－ajax－－开始")
    data = request.GET.get("name")
    url_base = "http://so.csdn.net/so/search/s.do?"
    headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/58.0.3029.110Safari/537.36",
                    }
    datas={"q":data}
    page_html = requests.get(url_base,headers=headers,params=datas )
    html = etree.HTML(page_html.text)
    url_list = html.xpath("//dl[@class='search-list J_search']/dt/a[1]/@href")
    name_list=html.xpath("//dl[@class='search-list J_search']/dt")
    new_name_list = map(fun,name_list)
    context = dict(map(lambda x,y:[x,y],  new_name_list,url_list))
    print("－－CSDN－－ajax－－结束")
    return JsonResponse(context)

def notfound(request):
    return render(request,"notfound.html")