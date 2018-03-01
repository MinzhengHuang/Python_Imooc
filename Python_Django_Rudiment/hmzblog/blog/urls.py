from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'article_page'

urlpatterns = [
    path('hello/', views.hello),
    url(r'^index/$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page, name='edit_page'),
    url(r'^edit/action$', views.edit_action, name='edit_action'),
]
