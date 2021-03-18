from rest_framework import serializers
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ('id', 'author', 'target_article', 'body', 'creation_date')