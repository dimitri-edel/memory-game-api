from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from category.models import Category
from face.models import Face
from face.serializers import FaceSerializer
from game_admin.authentication import User
import os
from memory_game_api.settings import API_MEDIA_STORAGE
from memory_game_api.settings import MEDIA_ROOT
from memory_game_api.settings import ALLOWED_CLIENT_HOSTS

class FaceList(APIView):
    '''View for listing all faces or creating a new face'''
    def get(self, request, format=None):
        '''Get request for listing all faces'''
        if(request.META['HTTP_ORIGIN'] not in ALLOWED_CLIENT_HOSTS):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        faces = Face.objects.all()
        serializer = FaceSerializer(faces, many=True)
        return Response(serializer.data)
