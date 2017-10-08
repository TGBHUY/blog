from ..models import Category, Article
from django import template

register = template.Library()


@register.assignment_tag
def tags_category_list():
    return Category.objects.all()

@register.assignment_tag
def tags_gedit_blog():
    return Article.objects.all()[:3]

@register.assignment_tag
def tags_hotblog_list():
    return Article.objects.order_by("-views")[:5]

    #
    # #类型列表
    # Category_list = Category.objects.all()
    #
    # #博客
    # blog_list = Article.objects.all()
    #
    # # 修改文章前三的列表
    # gedit_blog = blog_list[:3]
    # # gedit_blog = Article.objects.all()[:3]#最近修改的三篇
    #
    # # #最热门的五篇的列表
    # # hot_blog = Article.objects.order_by("-views")[:5]