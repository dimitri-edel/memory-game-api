from django.urls import path
from .views import FaceList

urlpatterns = [
    path('get-all/', FaceList.as_view(), name='face-list'),
]