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
        user = User(username=username, password=password)
        if not user.login():
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
       
        # Create a response with two tokens. The tokens are hashed values of the username and password.
        response = Response(status=status.HTTP_200_OK, data={'token1': user.get_token1(), 'token2': user.get_token2()})
        return response