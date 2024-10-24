'''Url patterns for the playlist app'''
from django.urls import path
from .views import PlaylistAddView
from .views import PlaylistGetView
from .views import PlaylistDeleteItemView
from .views import PlaylistUpdateItemView
from .views import PlaylistGetAllView


urlpatterns = [   
    path('get-all/<str:filter>/<str:api_key>', PlaylistGetAllView.as_view(), name='playlist_get_all'),
    path('add/', PlaylistAddView.as_view(), name='playlist_post_view'),
    path('get/<str:category>/<str:api_key>', PlaylistGetView.as_view(), name='playlist_get'),        
    path('delete/<int:id>/', PlaylistDeleteItemView.as_view(), name='playlist_delete_item'),
    path('update/<int:id>/', PlaylistUpdateItemView.as_view(), name='playlist_update_item'),
]

