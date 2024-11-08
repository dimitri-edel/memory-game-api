from django.urls import path
from .views import StyleList
from .views import StyleByCategory
from .views import StyleCreate
from .views import StyleUpdate
from .views import StyleDelete

urlpatterns = [
    path('get-all/', StyleList.as_view(), name='style-list'),
    path('get-by-category/<int:category_id>/', StyleByCategory.as_view(), name='style-by-category'),
    path('add/', StyleCreate.as_view(), name='style-create'),
    path('update/<int:id>/', StyleUpdate.as_view(), name='style-update'),
    path('delete/<int:id>/', StyleDelete.as_view(), name='style-delete'),
]