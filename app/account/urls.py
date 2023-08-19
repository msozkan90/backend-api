"""
URL mappings for the user API.
"""
from django.urls import path
from account import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = 'account'

urlpatterns = [
    path('profiles', views.UserListView.as_view(), name='profile-list'),
    path('register', views.UserCreateView.as_view(), name='register'),
    path('profile/<int:pk>', views.UserDetailView.as_view(), name='profile-detail'),
    path('login', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('breweries', views.BreweryListView.as_view(), name='brewery-list'),

]
