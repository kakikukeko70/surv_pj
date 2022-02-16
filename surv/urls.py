from django.urls import path
from .views import Home, Profile, Detail, Your_toko
from . import views

app_name = 'surv'
urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('profile', Profile.as_view(), name='profile'),
    path('your_toko', Your_toko.as_view(), name='your_toko'),
    path('<int:pk>/detail', Detail.as_view(), name='detail'),
    path('<int:toko_id>/send', views.send, name='send'),
]