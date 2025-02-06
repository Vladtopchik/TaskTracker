from django.urls import path
from .views import UserRegisterView, UserLoginView, logout_page

urlpatterns = [
    path('login', UserLoginView.as_view(), name='login'),
    path('register', UserRegisterView.as_view(), name='register'),
    path('logout', logout_page, name='logout'),
]
