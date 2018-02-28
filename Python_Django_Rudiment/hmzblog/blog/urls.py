from django.urls import path
from django.conf.urls import url
from . import views

# urlpatterns = [
#     path('index/', views.index),
# ]

app_name = 'article_page'

urlpatterns = [
    url(r'^hello/$', views.hello),
    url(r'^index/$', views.index),
    url(r'^article/(?P<article_id>[0-9])$', views.article_page, name='article_page'),
]
