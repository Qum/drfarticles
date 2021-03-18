from django.contrib import admin

from articles.models import Article


def make_published(modeladmin, request, queryset):
    queryset.update(moderated=True)

make_published.short_description = "Already moderated"


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'moderated']
    ordering = ['title']
    actions = [make_published]


admin.site.register(Article, ArticleAdmin)
