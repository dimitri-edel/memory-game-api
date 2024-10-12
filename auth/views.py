from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .authentication import User

class UserLoginView(APIView):
    '''Login view for User model'''
    def post(self, request):
        '''Post method for User model'''
        username = request.data.get('username')
        password = request.data.get('password')
        user = User(usernameHash=username, passwordHash=password)
        if not user.login():
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        cookie = user.generate_cookie()
        response = Response.set_cookie(Response(status=status.HTTP_200_OK), 'memory-game-token', cookie)
        return response
    
class UserLogoutView(APIView):
    '''Logout view for User model'''
    def post(self, request):
        '''Post method for User model'''
        cookie = request.COOKIES.get('memory-game-token')
        if not cookie:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user = User(usernameHash=None, passwordHash=None)
        user.cookie = cookie
        user.logout()
        response = Response(status=status.HTTP_200_OK)
        response.delete_cookie('memory-game-token')
        return response

