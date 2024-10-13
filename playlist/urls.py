'''Url patterns for the playlist app'''
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import PlaylistPostView
from .views import PlaylistGetView
from .views import PlaylistDeleteCategoryView
from .views import PlaylistDeleteItemView
from .views import PlaylistUpdateItemView

urlpatterns = [
    path('post/', PlaylistPostView.as_view(), name='playlist_post_view'),
    path('get/<str:category>/<str:api_key>', PlaylistGetView.as_view(), name='playlist_get_view'),    
    path('delete-category/<str:category>/', PlaylistDeleteCategoryView.as_view(), name='playlist_delete_category_view'),
    path('delete-item/<int:id>/', PlaylistDeleteItemView.as_view(), name='playlist_delete_item_view'),
    path('update-item/<int:id>/', PlaylistUpdateItemView.as_view(), name='playlist_update_item_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)