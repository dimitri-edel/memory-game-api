# URL patterns for this app
from django.urls import path
from .views import UserLoginView
from .views import UserLogoutView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user_login_view'),
    path('logout/', UserLogoutView.as_view(), name='user_logout_view'),
]