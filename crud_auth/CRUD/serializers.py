from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from .models import User


class SpecialUserCreateSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'is_active')


class ReadOnlyUserSerializer(BaseUserSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'is_active', 'last_login', 'is_superuser')


class WriteOnlyUserSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'is_active')
