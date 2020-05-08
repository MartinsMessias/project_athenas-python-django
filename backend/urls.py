from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.login),
    path('index/', views.index),
    path('api/<str:u>/<str:p>', views.api),

]
