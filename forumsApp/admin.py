from django.contrib import admin
from forumsApp.models import Article, Comment

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['title', 'description', 'author']
    # fields to filter the change list with
    list_filter = ['published', 'created']
    # fields to search in change list
    search_fields = ['title', 'description', 'content']
    # enable the date drill down on change list
    date_hierarchy = 'created'
    # enable the save buttons on top on change form
    save_on_top = True

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)