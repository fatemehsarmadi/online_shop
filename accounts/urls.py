from django.urls import path, re_path
from . import views

urlpatterns = [
    path('user_register/', views.user_register),
]