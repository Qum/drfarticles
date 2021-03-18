from rest_framework import serializers, permissions
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny, BasePermission
from rest_framework.viewsets import ModelViewSet


class PermissionsModelViewSetMixin(ModelViewSet):
    permission_classes_by_action = {'default': [IsAdminUser],
                                    'create': [IsAdminUser],
                                    'list': [IsAdminUser],
                                    'retrieve': [IsAdminUser],
                                    'destroy': [IsAdminUser],
                                    'update': [IsAdminUser],
                                    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            serializers.CurrentUserDefault()
            return [permission() for permission in self.permission_classes_by_action['default']]


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user
        return obj.pk == user.pk
