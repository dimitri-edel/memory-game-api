from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Style
from category.models import Category
from .serializers import StyleSerializer
from game_admin.authentication import User
from memory_game_api.settings import ALLOWED_CLIENT_HOSTS

# View for listing all styles
class StyleList(APIView):
    '''View for listing all styles'''
    def get(self, request, format=None):
        '''Get request for listing all styles'''
        if(request.META['HTTP_ORIGIN'] not in ALLOWED_CLIENT_HOSTS):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        styles = Style.objects.all()
        serializer = StyleSerializer(styles, many=True)
        return Response(serializer.data)

# View for getting a style baded on category id
class StyleByCategory(APIView):
    '''View for getting a style based on category id''' 
    def get(self, request, category_id):
        '''Get request for getting a style based on category id'''
        print("HTTP_ORIGIN : ")
        print(request.META['HTTP_ORIGIN'])
        if(request.META['HTTP_ORIGIN'] not in ALLOWED_CLIENT_HOSTS):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        category = Category.objects.get(id=category_id)
        style = Style.objects.get(category=category)
        serializer = StyleSerializer(style)
        return Response(serializer.data)

# class for creating a new style
class StyleCreate(APIView):
    '''View for creating a new style'''
    def post(self, request):
        '''Post request for creating a new style'''
        # Get token1 and token2 from the request headers
        # If the tokens are not valid, return a access denied response
        token1 = request.headers.get('Token1')
        token2 = request.headers.get('Token2')
        user = User()
        if not user.is_authorized(token1, token2):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        # if a style for the same category already exists, return a 409 conflict response
        category = Category.objects.get(id=request.data['category'])
        if Style.objects.filter(category=category).exists():
            return Response(status=status.HTTP_409_CONFLICT)
        # if the data is valid, save the style and return a 201 created response
        serializer = StyleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class for updating a style
class StyleUpdate(APIView):
    '''View for updating a style'''
    def put(self, request, id):
        '''Put request for updating a style'''
        # Get token1 and token2 from the request headers
        # If the tokens are not valid, return a access denied response
        token1 = request.headers.get('Token1')
        token2 = request.headers.get('Token2')
        user = User()
        if not user.is_authorized(token1, token2):
            return Response(status=status.HTTP_401_UNAUTHORIZED)        
        style = Style.objects.get(id=id)
        serializer = StyleSerializer(style, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class for deleting a style
class StyleDelete(APIView):
    '''View for deleting a style'''
    def delete(self, request, id):
        '''Delete request for deleting a style'''
        # Get token1 and token2 from the request headers
        # If the tokens are not valid, return a access denied response
        token1 = request.headers.get('Token1')
        token2 = request.headers.get('Token2')
        user = User()
        if not user.is_authorized(token1, token2):
            return Response(status=status.HTTP_401_UNAUTHORIZED)        
        style = Style.objects.get(id=id)
        style.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)