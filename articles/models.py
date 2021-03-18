from django.conf import settings
from django.db import models


class Article(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=False,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100)
    body = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now=True)
    moderated = models.BooleanField(default=False)

