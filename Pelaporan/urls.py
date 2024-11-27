from django.urls import path

from .views import Main, Login

urlpatterns = [
    path('', Main, name='index'),
    path('Login/', Login, name='Login')
]