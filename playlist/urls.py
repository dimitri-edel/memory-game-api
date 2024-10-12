'''Url patterns for the playlist app'''
from django.urls import path
from .views import PlaylistPostView
from .views import PlaylistGetView
from .views import PlaylistDeleteCategoryView
from .views import PlaylistDeleteItemView

urlpatterns = [
    path('post/', PlaylistPostView.as_view(), name='playlist_post_view'),
    path('get/<str:category>/<str:api_key>', PlaylistGetView.as_view(), name='playlist_get_view'),    
    path('delete/<str:category>/', PlaylistDeleteCategoryView.as_view(), name='playlist_delete_category_view'),
    path('delete/<int:id>/', PlaylistDeleteItemView.as_view(), name='playlist_delete_item_view'),
]