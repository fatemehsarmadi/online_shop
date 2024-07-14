from django.urls import path, re_path
from . import views

urlpatterns = [
    path('user_register/', views.user_register),
    path('user_login/', views.user_login),
    path('user_logout/', views.user_logout),
]