from django.urls import path, include
from .views import Index

#app_name = 'registration'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login/index', Index.as_view(), name='login_index'),
]