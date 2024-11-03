from django.urls import path
from .views import CategoryGetAllView
from .views import CategoryAddView
from .views import CategoryUpdateView
from .views import CategoryGetView
from .views import CategoryDeleteView

urlpatterns = [
    path('get-all/', CategoryGetAllView.as_view(), name='category_get_all'),
    path('add/', CategoryAddView.as_view(), name='category_add'),
    path('update/<int:id>/', CategoryUpdateView.as_view(), name='category_update'),
    path('get/<str:name>/<str:api_key>', CategoryGetView.as_view(), name='category_get'),
    path('delete/<int:id>/', CategoryDeleteView.as_view(), name='category_delete'),    
]