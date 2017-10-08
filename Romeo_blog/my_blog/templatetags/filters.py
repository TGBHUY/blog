from ..models import Comment
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

#使用装饰器进行注册

@register.filter
@stringfilter
def com_sum(value):
    return len(Comment.objects.filter(blog_id=value))