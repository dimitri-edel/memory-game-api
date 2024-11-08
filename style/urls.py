from django.urls import path
from .views import StyleList
from .views import StyleCreate

urlpatterns = [
    path('get-all/', StyleList.as_view(), name='style-list'),
    path('add/', StyleCreate.as_view(), name='style-create'),
]