from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('all_mobiles/', views.all_mobiles, name='all_mobiles'),
]