from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from face.models import Face
from category.models import Category
from face.serializers import FaceSerializer
from game_admin.authentication import User
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
    
# class for getting a list of faces for a category
class FaceListByCategory(APIView):
    '''View for listing all faces for a category'''
    def get(self, request, category_id):
        '''Get request for listing all faces for a category'''
        if(request.META['HTTP_ORIGIN'] not in ALLOWED_CLIENT_HOSTS):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        faces = Face.objects.filter(category=category_id)
        serializer = FaceSerializer(faces, many=True)
        return Response(serializer.data)
    

# class for creating a new face
class FaceCreate(APIView):
    '''View for creating a new face'''
    def post(self, request):
        '''Post request for creating a new face'''
        # Get token1 and token2 from the request headers
        # If the tokens are not valid, return a access denied response
        token1 = request.headers.get('Token1')
        token2 = request.headers.get('Token2')
        user = User()
        if not user.is_authorized(token1, token2):
            return Response(status=status.HTTP_401_UNAUTHORIZED)        
        serializer = FaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class for updating a face
class FaceUpdate(APIView):
    '''View for updating a face'''
    def put(self, request, id):
        '''Put request for updating a face'''
        # Get token1 and token2 from the request headers
        # If the tokens are not valid, return a access denied response
        token1 = request.headers.get('Token1')
        token2 = request.headers.get('Token2')
        user = User()
        if not user.is_authorized(token1, token2):
            return Response(status=status.HTTP_401_UNAUTHORIZED)        
        face = Face.objects.get(id=id)
        serializer = FaceSerializer(face, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class for deleting a face
class FaceDelete(APIView):
    '''View for deleting a face'''
    def delete(self, request, id):
        '''Delete request for deleting a face'''
        # Get token1 and token2 from the request headers
        # If the tokens are not valid, return a access denied response
        token1 = request.headers.get('Token1')
        token2 = request.headers.get('Token2')
        user = User()
        if not user.is_authorized(token1, token2):
            return Response(status=status.HTTP_401_UNAUTHORIZED)        
        face = Face.objects.get(id=id)
        face.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)