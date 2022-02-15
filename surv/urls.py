from unicodedata import name
from django.urls import path
from .views import Home, Profile
from . import views

app_name = 'surv'
urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('profile', Profile.as_view(), name='profile'),
    path('your_toko', views.your_toko, name='your_toko'),
]