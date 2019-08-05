from django.urls import path
from polls import views as polls_views

urlpatterns = [
    path('index/', polls_views.index),
    path('data/', polls_views.data),
    path('login/', polls_views.login),
    path('loginview/', polls_views.loginview),
]