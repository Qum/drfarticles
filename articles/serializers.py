from rest_framework import serializers
from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Article
        fields = ('id', 'author', 'title', 'body', 'creation_date')