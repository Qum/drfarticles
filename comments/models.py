from django.conf import settings
from django.db import models
from articles.models import Article


class Comment(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=False,
        on_delete=models.CASCADE,
    )
    target_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    body = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now=True)
    moderated = models.BooleanField(default=False)