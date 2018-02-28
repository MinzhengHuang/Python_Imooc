from django.shortcuts import render
from django.http import HttpResponse
from . import models


def hello(request):
    return HttpResponse("Hello, Hmz!")

# def index(request):
#     return render(request, 'blog/index.html', {'hello': 'hello,hmz blog haha'})

# def index(request):
#     article = models.Artical.objects.get(pk=1)
#     return render(request, 'blog/index.html', {'article': article})


def index(request):
    arts = models.Artical.objects.all()
    return render(request, 'blog/index.html', {'articles': arts})


def article_page(request, article_id):
    art = models.Artical.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': art})
