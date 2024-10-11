'''Views for the playlist app'''
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Playlist
from .serializers import PlaylistSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class PlayListPostView(APIView):
    '''Post view for Playlist model'''
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request):
        '''Post method for Playlist model'''
        playlist_serializer = PlaylistSerializer(data=request.data)
        if playlist_serializer.is_valid():
            playlist_serializer.save()
            return Response(playlist_serializer.data, status=status.HTTP_201_CREATED)
        return Response(playlist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)