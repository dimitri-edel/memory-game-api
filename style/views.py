from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Style
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
        serializer = StyleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
