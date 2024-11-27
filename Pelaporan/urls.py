from django.urls import path

from .views import Main, Login, Signin

urlpatterns = [
    path('', Main, name='index'),
    path('Login/', Login, name='Login'),
    path('Signin/', Signin, name='Signin')

]