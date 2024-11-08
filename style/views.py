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

