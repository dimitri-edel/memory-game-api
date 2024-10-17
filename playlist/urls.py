'''Url patterns for the playlist app'''
from django.urls import path
from .views import PlaylistPostView
from .views import PlaylistGetView
from .views import PlaylistDeleteCategoryView
from .views import PlaylistDeleteItemView
from .views import PlaylistUpdateItemView
from .views import PlaylistGetAllView


urlpatterns = [   
    path('get-all/<str:filter>/<str:api_key>', PlaylistGetAllView.as_view(), name='playlist_get_all_view'),
    path('post/', PlaylistPostView.as_view(), name='playlist_post_view'),
    path('get/<str:category>/<str:api_key>', PlaylistGetView.as_view(), name='playlist_get_view'),    
    path('delete-category/<str:category>/', PlaylistDeleteCategoryView.as_view(), name='playlist_delete_category_view'),
    path('delete-item/<int:id>/', PlaylistDeleteItemView.as_view(), name='playlist_delete_item_view'),
    path('update-item/<int:id>/', PlaylistUpdateItemView.as_view(), name='playlist_update_item_view'),
]

