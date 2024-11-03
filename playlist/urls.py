'''Url patterns for the playlist app'''
from django.urls import path
from .views import PlaylistAddView
from .views import PlaylistGetByCategoryView
from .views import PlaylistDeleteItemView
from .views import PlaylistUpdateItemView
from .views import PlaylistGetAllView


urlpatterns = [   
    path('get-all/<str:filter>/', PlaylistGetAllView.as_view(), name='playlist_get_all'),
    path('get-by-category/<str:category>/', PlaylistGetByCategoryView.as_view(), name='playlist_get'),        
    path('add/', PlaylistAddView.as_view(), name='playlist_post'),
    path('delete/<int:id>/', PlaylistDeleteItemView.as_view(), name='playlist_delete_item'),
    path('update/<int:id>/', PlaylistUpdateItemView.as_view(), name='playlist_update_item'),
]

