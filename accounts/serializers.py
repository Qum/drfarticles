from accounts.models import User
from rest_framework import serializers


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'username', 'first_name', 'phone_number', 'about')
