from django.db import models

class UserLocaleModel(models.Model):
    postal_code = models.CharField(max_length=9)
    state = models.CharField(max_length=32)
    locale = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=128)
    number = models.CharField(max_length=8)
