from django.urls import path, include
from .views import Index, SignUpView, ActivateView

urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    path('login/index', Index.as_view(), name='login_index'),
    path('activate/<uidb64>/<token>/', ActivateView.as_view(), name='activate'),
    path('', include('django.contrib.auth.urls')),
]