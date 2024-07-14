from django.urls import path, re_path
from . import views

app_name = 'products'
urlpatterns = [
    path('all_mobiles/', views.all_mobiles, name='all_mobiles'),
    re_path(r'^mobile/(?P<id>\d+)/$', views.get_mobile),
    path('add_mobile/', views.add_new_mobile),
    re_path(r'^edit_mobile/(?P<id>\d+)/$', views.edit_book),
]