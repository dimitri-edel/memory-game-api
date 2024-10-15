'''Views for the playlist app'''
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer
from .models import Playlist
from .serializers import PlaylistSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from game_admin.authentication import User
import os

''' A class for retrieiving all the items from the Category model'''
class CategoryGetAllView(APIView):
    '''Get method for Category model'''
    def get(self, request, api_key):
        if(api_key != os.environ["API_KEY"]):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        '''Get all items from the Category model'''
        category = Category.objects.all()
        category_serializer = CategorySerializer(category, many=True)
        return Response(category_serializer.data)
    
''' A class for retrieving the item from the Category model that has been passed in the url'''
class CategoryGetView(APIView):
    '''Get method for Category model'''
    def get(self, request, id, api_key):
        if(api_key != os.environ["API_KEY"]):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        '''Get item from the Category model'''
        category = Category.objects.get(id=id)
        category_serializer = CategorySerializer(category)
        return Response(category_serializer.data)

''' A class for posting the item to the Category model'''
class CategoryPostView(APIView):
    '''Post method for Category model'''
    def post(self, request):
        # Get token1 and token2 from the request headers
        # If the tokens are not valid, return a access denied response
        token1 = request.headers.get('Token1')
        token2 = request.headers.get('Token2')
        user = User()
        if not user.is_authorized(token1, token2):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        '''Post method for Category model'''
        category_serializer = CategorySerializer(data=request.data)
        if category_serializer.is_valid():
            category_serializer.save()
            return Response(category_serializer.data, status=status.HTTP_201_CREATED)
        return Response(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
''' A class for deleting the item from the Category model that has been passed in the url'''
class CategoryDeleteView(APIView):
    '''Delete method for Category model'''
    def delete(self, request, id):
        # Get token1 and token2 from the request headers
        # If the tokens are not valid, return a access denied response
        token1 = request.headers.get('Token1')
        token2 = request.headers.get('Token2')
        user = User()
        if not user.is_authorized(token1, token2):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        '''Delete method for Category model'''
        category = Category.objects.get(id=id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

''' A class for retrieving all the items from the Playlist model
 and if a filter is passed in the url, it will return all the items
   from the Playlist model whose category, title or description contains the filter'''
class PlaylistGetAllView(APIView):
    '''Get method for Playlist model'''
    def get(self, request, filter, api_key):
        if(api_key != os.environ["API_KEY"]):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        '''Get all items from the Playlist model'''
        playlist = Playlist.objects.all()
        if filter != 'none':
            playlist = Playlist.objects.filter(
                category__name__icontains=filter
            ) | Playlist.objects.filter(
                title__icontains=filter
            ) | Playlist.objects.filter(
                description__icontains=filter
            )
        playlist_serializer = PlaylistSerializer(playlist, many=True)
        return Response(playlist_serializer.data)

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
        token1 = request.headers.get('Token1')
        token2 = request.headers.get('Token2')
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
        token1 = request.headers.get('Token1')
        token2 = request.headers.get('Token2')
        user = User()
        if not user.is_authorized(token1, token2):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        '''Delete item from the Playlist'''        
        playlist = Playlist.objects.filter(id=id)
        playlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlaylistUpdateItemView(APIView):
    '''Update view for Playlist model'''
    '''Update the item from playlist that has been passed in the url'''
    def put(self, request, id):
         # Get token1 and token2 from the request headers
        # If the tokens are not valid, return a access denied response
        token1 = request.headers.get('Token1')
        token2 = request.headers.get('Token2')
        user = User()
        if not user.is_authorized(token1, token2):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        '''Update item from the Playlist'''
        playlist = Playlist.objects.get(id=id)
        playlist_serializer = PlaylistSerializer(playlist, data=request.data)
        if playlist_serializer.is_valid():
            playlist_serializer.save()
            return Response(playlist_serializer.data)
        return Response(playlist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)