from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from .views import (
    UserRegisterView,
    UserLoginView,
    UserLogoutView,
    UserProfileView,
    UserListView
)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    # path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('user-list/', UserListView.as_view(), name='user-list'),
]
