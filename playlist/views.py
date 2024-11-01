"""Views for the playlist app"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Playlist
from .serializers import PlaylistSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from game_admin.authentication import User
import os
from memory_game_api.settings import API_MEDIA_STORAGE
from memory_game_api.settings import MEDIA_ROOT

""" A class for retrieving all the items from the Playlist model
 and if a filter is passed in the url, it will return all the items
   from the Playlist model whose category, title or description contains the filter"""


class PlaylistGetAllView(APIView):
    """Get method for Playlist model"""

    def get(self, request, filter, api_key):
        if api_key != os.environ["API_KEY"]:
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


class PlaylistGetView(APIView):
    # get all items from playlist that are in the category that has been passed in the url
    def get(self, request, category, api_key):
        """Get method for Playlist model"""
        if api_key != os.environ["API_KEY"]:
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
        """ If the API_MEDIA_STORAGE (in settings.py) is set to MEDIA_FOLDER, delete the image and audio files from the media folder"""
        if API_MEDIA_STORAGE == "MEDIA_FOLDER":
            self.remove_associated_files(playlist)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def remove_associated_files(self, playlist):
        """Remove the associated files from the media folder"""
        try:
            # Delete the image and audio files from the media folder
            media_image_path = os.path.join(MEDIA_ROOT, "images", playlist.image.name)            
            if os.path.exists(media_image_path):
                os.remove(media_image_path)
        except:
            pass

        try:
            media_audio_path = os.path.join(MEDIA_ROOT, "audio", playlist.audio.name)            
            if os.path.exists(media_audio_path):
                os.remove(media_audio_path)
        except:
            pass

        try:
            media_quiz_path = os.path.join(MEDIA_ROOT, "json", playlist.quiz.name)
            if os.path.exists(media_quiz_path):
                os.remove(media_quiz_path)
        except:
            pass


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
