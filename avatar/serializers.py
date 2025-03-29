from rest_framework import serializers
from django.contrib.auth.models import User

from .models import AvatarModel
from user_locale import serializers as user_locale_serializers

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email',)


class AvatarCreationSerializer(serializers.ModelSerializer):
    fk_user = UserCreateSerializer()
    fk_user_locale = user_locale_serializers.UserLocaleSerializer

    class Meta:
        model = AvatarModel
        exclude = ('created_at', 'updated_at', 'deleted_at')

class AvatarResponseSerializer(serializers.ModelSerializer):
    fk_user = UserResponseSerializer()
    fk_user_locale = user_locale_serializers.UserLocaleSerializer

    class Meta:
        model = AvatarModel
        fields = '__all__'