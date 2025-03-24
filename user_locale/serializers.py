from rest_framework import serializers
from .models import UserLocaleModel

class UserLocaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocaleModel
        exclude = ['id']
