from django.urls import path
from .views import FaceList
from .views import FaceCreate

urlpatterns = [
    path('get-all/', FaceList.as_view(), name='face-list'),
    path('add/', FaceCreate.as_view(), name='face-create'),
]