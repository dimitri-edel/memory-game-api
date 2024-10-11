'''Views for the playlist app'''
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Playlist
from .serializers import PlaylistSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class PlaylistPostView(APIView):
    '''Post view for Playlist model'''
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request):        
        '''Post method for Playlist model'''
        playlist_serializer = PlaylistSerializer(data=request.data)
        if playlist_serializer.is_valid():
            playlist_serializer.save()
            return Response(playlist_serializer.data, status=status.HTTP_201_CREATED)
        return Response(playlist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PlaylistGetView(APIView):
    # get all items from playlist that are in the category that has been passed in the url
    def get(self, request, category):
        '''Get method for Playlist model'''
        print(category)
        playlist = Playlist.objects.filter(category=category)
        playlist_serializer = PlaylistSerializer(playlist, many=True)
        return Response(playlist_serializer.data)
    
class PlaylistDeleteCategoryView(APIView):
    '''Delete view for Playlist model'''
    '''Delete all items from playlist that are in the category that has been passed in the url'''
    def delete(self, request, category):
        '''Delete method for Playlist model'''
        playlist = Playlist.objects.filter(category=category)
        playlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlaylistDeleteItemView(APIView):
    '''Delete view for Playlist model'''
    '''Delete the item from playlist that has been passed in the url'''
    def delete(self, request, id):
        '''Delete method for Playlist model'''
        playlist = Playlist.objects.filter(id=id)
        playlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)