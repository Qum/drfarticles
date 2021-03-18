from djoser.permissions import CurrentUserOrAdmin
from rest_framework.permissions import AllowAny, IsAuthenticated
from comments.models import Comment
from comments.serializers import CommentSerializer
from drfarticles.permittions import IsOwner, PermissionsModelViewSetMixin


class CommentViewSet(PermissionsModelViewSetMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes_by_action = {'default': [IsAuthenticated],
                                    'create': [IsAuthenticated],
                                    'list': [AllowAny],
                                    'retrieve': [AllowAny],
                                    'destroy': [IsOwner],
                                    'update': [IsOwner],
                                    }
