from django.urls import path
from .views import FaceList
from .views import FaceCreate
from .views import FaceUpdate
from .views import FaceDelete

urlpatterns = [
    path('get-all/', FaceList.as_view(), name='face-list'),
    path('add/', FaceCreate.as_view(), name='face-create'),
    path('update/<int:id>/', FaceUpdate.as_view(), name='face-update'),
    path('delete/<int:id>/', FaceDelete.as_view(), name='face-delete'),
]