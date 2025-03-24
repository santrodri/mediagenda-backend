from django.db import models
from django.contrib.auth.models import User

from user_locale.models import UserLocaleModel

class AvatarModel(models.Model):
    # Base user
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Avatar details
    full_name = models.CharField(max_length=128)
    photo = models.ImageField(upload_to='avatars/images')
    identify = models.CharField(max_length=11, primary_key=True)
    birthdate = models.DateField()
    gender = models.CharField(max_length=6, choices=(
        ('male', 'Male'),
        ('female', 'Female'),
    ))
    fk_user_locale = models.ManyToManyField(UserLocaleModel)
    phone_number = models.CharField(max_length=18)
    status = models.CharField(max_length=500)
    # avatar details controller
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
