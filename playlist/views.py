'''Views for the playlist app'''
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Playlist
from .serializers import PlaylistSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from game_admin.authentication import User
import os

class PlaylistPostView(APIView):
    '''Post view for Playlist model'''
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request): 
        # Get token1 and token2 from the request headers
        # If the tokens are not valid, return a access denied response
        token1 = request.headers.get('Token1')
        token2 = request.headers.get('Token2')
        
        user = User()        

        if not user.is_authorized(token1, token2):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        print("request.data", request.data) 
        
        '''Post method for Playlist model'''
        playlist_serializer = PlaylistSerializer(data=request.data)
        if playlist_serializer.is_valid():
            playlist_serializer.save()
            return Response(playlist_serializer.data, status=status.HTTP_201_CREATED)
        return Response(playlist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PlaylistGetView(APIView):
    # get all items from playlist that are in the category that has been passed in the url
    def get(self, request, category, api_key):
        '''Get method for Playlist model'''
        if(api_key != os.environ["API_KEY"]):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        playlist = Playlist.objects.filter(category=category)
        playlist_serializer = PlaylistSerializer(playlist, many=True)
        return Response(playlist_serializer.data)
    
class PlaylistDeleteCategoryView(APIView):
    '''Delete view for Playlist model'''
    '''Delete all items from playlist that are in the category that has been passed in the url'''
    def delete(self, request, category):
         # Get token1 and token2 from the request headers
        # If the tokens are not valid, return a access denied response
        token1 = request.headers.get('token1')
        token2 = request.headers.get('token2')
        user = User()
        if not user.is_authorized(token1, token2):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        '''Delete category from the Playlist'''
        playlist = Playlist.objects.filter(category=category)
        playlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlaylistDeleteItemView(APIView):
    '''Delete view for Playlist model'''
    '''Delete the item from playlist that has been passed in the url'''
    def delete(self, request, id):
         # Get token1 and token2 from the request headers
        # If the tokens are not valid, return a access denied response
        token1 = request.headers.get('token1')
        token2 = request.headers.get('token2')
        user = User()
        if not user.is_authorized(token1, token2):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        '''Delete item from the Playlist'''        
        playlist = Playlist.objects.filter(id=id)
        playlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)