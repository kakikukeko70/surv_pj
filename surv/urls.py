from unicodedata import name
from django.urls import path, include

import registration
from .views import Category_toko_list, Home, Profile, Detail, Your_toko, New_category, Category_toko_list, Result, Setting
from . import views

app_name = 'surv'
urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('', include('registration.urls')),
    path('profile', Profile.as_view(), name='profile'),
    path('your_toko', Your_toko.as_view(), name='your_tokos'),
    path('<int:pk>/detail', Detail.as_view(), name='detail'),
    path('<int:toko_id>/send', views.send, name='send'),
    path('new_category', New_category.as_view(), name='new_category'),
    path('<int:pk>/category_toko_list', Category_toko_list.as_view(), name='category_toko_list'),
    path('<int:pk>/result', Result.as_view(), name='result'),
    path('setting', Setting.as_view(), name='setting'),
]