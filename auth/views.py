from rest_framework.views import APIView
from rest_framework.response import Response    
from rest_framework import status
from .authentication import User
'''
Views for the auth app

Upon loging in the user gets two tokens. The tokens are hashed values of the username and password.
These tokens can be stored in the client's local storage or as a cookie.
The tokens are used to authenticate the user when they make requests to the API.
'''
class UserLoginView(APIView):
    '''Login view for User model'''
    def post(self, request):
        '''Post method for User model'''
        username = request.data.get('username')
        password = request.data.get('password')
        user = User(usernameHash=username, passwordHash=password)
        if not user.login():
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
       
        # Create a response with two tokens. The tokens are hashed values of the username and password.
        response = Response(status=status.HTTP_200_OK, data={'token1': username, 'token2': password})
        return response

class UserLogoutView(APIView):
    '''Logout view for User model'''
    def post(self, request):
        '''Post method for User model'''
        username = request.data.get('token1')
        password = request.data.get('token2')
        user = User(usernameHash=username, passwordHash=password)
        user.logout()
        return Response(status=status.HTTP_200_OK)

