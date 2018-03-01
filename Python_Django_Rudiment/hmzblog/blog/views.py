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


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')
    article = models.Artical.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})


def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', 0)
    if article_id == '0':
        models.Artical.objects.create(title=title, content=content)
        arts = models.Artical.objects.all()
        return render(request, 'blog/index.html', {'articles': arts})

    article = models.Artical.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog/article_page.html', {'article': article})
