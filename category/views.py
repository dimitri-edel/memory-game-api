'''Views for the playlist app'''
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer
from game_admin.authentication import User
import os
from memory_game_api.settings import API_MEDIA_STORAGE
from memory_game_api.settings import MEDIA_ROOT
from memory_game_api.settings import ALLOWED_CLIENT_HOSTS

''' A class for retrieiving all the items from the Category model'''
class CategoryGetAllView(APIView):
    '''Get method for Category model'''
    def get(self, request):
        if(request.META['HTTP_ORIGIN'] not in ALLOWED_CLIENT_HOSTS):
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
class CategoryAddView(APIView):
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

''' A class for updating the item from the Category model that has been passed in the url'''
class CategoryUpdateView(APIView):
    '''Put method for Category model'''
    def put(self, request, id):
        # Get token1 and token2 from the request headers
        # If the tokens are not valid, return a access denied response
        token1 = request.headers.get('Token1')
        token2 = request.headers.get('Token2')
        user = User()
        if not user.is_authorized(token1, token2):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        '''Put method for Category model'''
        category = Category.objects.get(id=id)
        category_serializer = CategorySerializer(category, data=request.data)
        if category_serializer.is_valid():
            category_serializer.save()
            return Response(category_serializer.data)
        return Response(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
''' A class for deleting the item from the Category model that has been passed in the url'''
class CategoryDeleteView(APIView):
    '''Delete method for Category model'''
    def delete(self, request, id):
        category = None
        # Get token1 and token2 from the request headers
        # If the tokens are not valid, return a access denied response
        token1 = request.headers.get('Token1')
        token2 = request.headers.get('Token2')
        user = User()
        if not user.is_authorized(token1, token2):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        '''Delete method for Category model'''
        try:
            category = Category.objects.get(id=id)
        except Category.DoesNotExist:
        # If the category does not exist return a 404 response        
            return Response(status=status.HTTP_404_NOT_FOUND)
        category.delete()        
        return Response(status=status.HTTP_204_NO_CONTENT)
