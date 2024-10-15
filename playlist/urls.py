'''Url patterns for the playlist app'''
from django.urls import path
from .views import PlaylistPostView
from .views import PlaylistGetView
from .views import PlaylistDeleteCategoryView
from .views import PlaylistDeleteItemView
from .views import PlaylistUpdateItemView
from .views import PlaylistGetAllView
from .views import CategoryGetAllView
from .views import CategoryPostView
from .views import CategoryGetView
from .views import CategoryDeleteView

urlpatterns = [    
    path('category/get-all/<str:api_key>', CategoryGetAllView.as_view(), name='category_get_all_view'),
    path('category/post/', CategoryPostView.as_view(), name='category_post_view'),
    path('category/get/<str:name>/<str:api_key>', CategoryGetView.as_view(), name='category_get_view'),
    path('category/delete/<int:id>/', CategoryDeleteView.as_view(), name='category_delete_view'),    
    path('get-all/<str:filter>/<str:api_key>', PlaylistGetAllView.as_view(), name='playlist_get_all_view'),
    path('post/', PlaylistPostView.as_view(), name='playlist_post_view'),
    path('get/<str:category>/<str:api_key>', PlaylistGetView.as_view(), name='playlist_get_view'),    
    path('delete-category/<str:category>/', PlaylistDeleteCategoryView.as_view(), name='playlist_delete_category_view'),
    path('delete-item/<int:id>/', PlaylistDeleteItemView.as_view(), name='playlist_delete_item_view'),
    path('update-item/<int:id>/', PlaylistUpdateItemView.as_view(), name='playlist_update_item_view'),
]

