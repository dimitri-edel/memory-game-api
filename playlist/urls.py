'''Url patterns for the playlist app'''
from django.urls import path
from .views import PlaylistPostView

urlpatterns = [
    path('playlist/', PlaylistPostView.as_view(), name='playlist_post_view'),
]