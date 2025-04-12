from django.urls import path

from . import views

urlspatterns = [
    path('user', views.UserView.as_view(), name='user'),
    path('code', views.CodeView.as_view(), name='user_code'),
]