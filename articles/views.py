from rest_framework.permissions import AllowAny, IsAuthenticated
from articles.models import Article
from articles.serializers import ArticleSerializer
from drfarticles.permittions import IsOwner, PermissionsModelViewSetMixin


class ArticleViewSet(PermissionsModelViewSetMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes_by_action = {'default': [IsAuthenticated],
                                    'create': [IsAuthenticated],
                                    'list': [AllowAny],
                                    'retrieve': [AllowAny],
                                    'destroy': [IsOwner],
                                    'update': [IsOwner],
                                    }
