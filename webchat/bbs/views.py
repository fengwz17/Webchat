from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from bbs import models
from django.contrib.auth.decorators import login_required  # login_required 这是装饰器函数
from django.contrib.auth import authenticate,login,logout
import json
from bbs import comment_hander
from bbs import forms

# Create your views here.

category_list = models.Category.objects.filter(set_as_top_menu =True).order_by('positon_index')

def index(request):
    print(category_list)
    category_obj = models.Category.objects.get(positon_index=1)  # 我们这里定义positon_index=1时,这个就是"全部"这个板块
    article_list = models.Article.objects.filter(status='published')
    return render(request,"bbs/index.html",{ 'category_list':category_list,
                                                'category_obj':category_obj,
                                                'article_list':article_list})

def category(request,id):  # id是URL配置中category/(\d+)/$的(\d+),一个括号就是一个参数
    category_obj = models.Category.objects.get(id=id)
    if category_obj.positon_index == 1:  # 我们把板块"全部"认定为首页显示,把所有的文章都显示出来,首页就认定当position_index 为1时既是首页.
        article_list = models.Article.objects.filter(status='published')  # 把所有状态为"已发布"的查出来
    else:
        article_list = models.Article.objects.filter(category_id=category_obj.id, status='published')
    return render(request,"bbs/index.html",{'category_list':category_list,
                                            'category_obj':category_obj,
                                            'article_list':article_list})

def article_detail(request,id):
    article_obj = models.Article.objects.get(id = id)
    return render(request,'bbs/article_detail.html',{'article_obj':article_obj, 'category_list':category_list})
