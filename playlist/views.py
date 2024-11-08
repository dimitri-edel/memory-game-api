"""Views for the playlist app"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Playlist
from .serializers import PlaylistSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from game_admin.authentication import User
from memory_game_api.settings import ALLOWED_CLIENT_HOSTS

""" A class for retrieving all the items from the Playlist model
 and if a filter is passed in the url, it will return all the items
   from the Playlist model whose category, title or description contains the filter"""


class PlaylistGetAllView(APIView):
    """Get method for Playlist model"""

    def get(self, request, filter):
        if(request.META['HTTP_ORIGIN'] not in ALLOWED_CLIENT_HOSTS):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        """Get all items from the Playlist model"""
        playlist = Playlist.objects.all()
        if filter != "none":
            playlist = (
                Playlist.objects.filter(category__name__icontains=filter)
                | Playlist.objects.filter(title__icontains=filter)
                | Playlist.objects.filter(description__icontains=filter)
            )
        playlist_serializer = PlaylistSerializer(playlist, many=True)
        return Response(playlist_serializer.data)


class PlaylistAddView(APIView):
    """Post view for Playlist model"""

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        """Post method for Playlist model"""
        # Get token1 and token2 from the request headers
        # If the tokens are not valid, return a access denied response
        token1 = request.headers.get("Token1")
        token2 = request.headers.get("Token2")
        user = User()
        if not user.is_authorized(token1, token2):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        playlist_serializer = PlaylistSerializer(data=request.data)
        if playlist_serializer.is_valid():
            playlist_serializer.save()
            return Response(playlist_serializer.data, status=status.HTTP_201_CREATED)
        return Response(playlist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlaylistGetByCategoryView(APIView):
    # get all items from playlist that are in the category that has been passed in the url
    def get(self, request, category):
        """Get method for Playlist model"""
        if(request.META['HTTP_ORIGIN'] not in ALLOWED_CLIENT_HOSTS):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        playlist = Playlist.objects.filter(category=category)
        playlist_serializer = PlaylistSerializer(playlist, many=True)
        return Response(playlist_serializer.data)


class PlaylistDeleteItemView(APIView):
    """Delete view for Playlist model"""

    """Delete the item from playlist that has been passed in the url"""

    def delete(self, request, id):
        # Get token1 and token2 from the request headers
        # If the tokens are not valid, return a access denied response
        token1 = request.headers.get("Token1")
        token2 = request.headers.get("Token2")
        user = User()
        if not user.is_authorized(token1, token2):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        """Delete item from the Playlist"""
        try:
            playlist = Playlist.objects.get(id=id)
        except Playlist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        playlist.delete()        
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlaylistUpdateItemView(APIView):
    """Update view for Playlist model"""

    """Update the item from playlist that has been passed in the url"""

    def put(self, request, id):
        # Get token1 and token2 from the request headers
        # If the tokens are not valid, return a access denied response
        token1 = request.headers.get("Token1")
        token2 = request.headers.get("Token2")
        user = User()
        if not user.is_authorized(token1, token2):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        """Update item from the Playlist"""
        playlist = Playlist.objects.get(id=id)
        playlist_serializer = PlaylistSerializer(playlist, data=request.data)
        if playlist_serializer.is_valid():
            playlist_serializer.save()
            return Response(playlist_serializer.data)
        return Response(playlist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
