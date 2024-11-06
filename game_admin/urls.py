# URL patterns for this app
from django.urls import path
from .views import UserLoginView
from .views import FileManager

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user_login_view'),   
    path('files/', FileManager.as_view(), name='file_manager'), 
]