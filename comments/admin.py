from django.contrib import admin
from comments.models import Comment

# admin.site.register(Comment)


def make_published(modeladmin, request, queryset):
    queryset.update(moderated=True)


make_published.short_description = "Already moderated"


class CommentAdmin(admin.ModelAdmin):
    list_display = ['body', 'moderated']
    ordering = ['body']
    actions = [make_published]


admin.site.register(Comment, CommentAdmin)
