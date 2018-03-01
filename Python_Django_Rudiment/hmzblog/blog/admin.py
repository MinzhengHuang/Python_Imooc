from django.contrib import admin
from .models import Artical


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_time')
    list_filter = ('pub_time',)


admin.site.register(Artical, ArticleAdmin)
