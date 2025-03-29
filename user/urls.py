from django.urls import path

from . import views

urlspatterns = [
    path('', views.UserView.as_view(), name='user'),
]