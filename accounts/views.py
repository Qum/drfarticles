from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from accounts.models import User
from accounts.serializers import MyUserSerializer
from drfarticles.permittions import PermissionsModelViewSetMixin, IsOwner


class UserViewSet(PermissionsModelViewSetMixin):
    queryset = User.objects.all()
    serializer_class = MyUserSerializer
    permission_classes_by_action = {'default': [IsAuthenticated],
                                    'create': [IsAuthenticated],
                                    'list': [AllowAny],
                                    'retrieve': [AllowAny],
                                    'destroy': [IsAdminUser],
                                    'update': [IsOwner],
                                    }
