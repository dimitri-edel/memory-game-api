from django.urls import path
from .views import StyleList

urlpatterns = [
    path('get-all/', StyleList.as_view(), name='style-list'),
]