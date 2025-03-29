from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserSerializerResponse(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'last_name']

class UserSerializerRequest(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
