from django.urls import path
from .views import CategoryGetAllView
from .views import CategoryPostView
from .views import CategoryUpdateView
from .views import CategoryGetView
from .views import CategoryDeleteView

urlpatterns = [
    path('get-all/<str:api_key>', CategoryGetAllView.as_view(), name='category_get_all_view'),
    path('post/', CategoryPostView.as_view(), name='category_post_view'),
    path('put/<int:id>/', CategoryUpdateView.as_view(), name='category_put_view'),
    path('get/<str:name>/<str:api_key>', CategoryGetView.as_view(), name='category_get_view'),
    path('delete/<int:id>/', CategoryDeleteView.as_view(), name='category_delete_view'),    
]