from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

#视图函数
def movie_list(request):
    return HttpResponse("电影列表")

def movie_detial(request,movie_id):
    return HttpResponse(f"您查找的电影id是:{movie_id}")

def index(request):
    return render(request,"index.html")

def info(request):
    print(request)
    #1.普通用法
    username = '我不是jack'
    #2.字典类型
    book = {'name':"水浒传",'author':"施耐庵"}
    #3.列表
    books = [
        {'name':"水浒传",'author':"施耐庵"},
        {'name':"三国演义",'author':"罗贯中"}
    ]
    #4.对象
    class Person:
        def __init__(self,name):
            self.name = name
      
    #为了美观,可以将render中的context参数,单独提取出来
    context = {
        "username":username,
        "book":book,
        "books":books,
        "person":Person("我是jack")
    }
    
    return render(request,"info.html",context=context)

    
    