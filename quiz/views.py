# import APIView from rest_framework.views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from game_admin.authentication import User
import os
from memory_game_api.settings import API_MEDIA_STORAGE
from memory_game_api.settings import MEDIA_ROOT
from .models import Quiz
from .serializers import QuizSerializer


# Class for view that gets a list of all the quizzes
class QuizListView(APIView):
    '''Get method for Quiz model'''
    def get(self, request, filter, api_key):
        if(api_key != os.environ["API_KEY"]):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        '''Get all items from the Quiz model'''
        quiz = Quiz.objects.all()
        if filter != 'none':
            quiz = Quiz.objects.filter(
                category__name__icontains=filter
            ) 
        quiz_serializer = QuizSerializer(quiz, many=True)
        return Response(quiz_serializer.data)

''' A class for adding a new quiz to the Quiz model.
    The user must be authorized to add a new quiz.
    The user must have the correct tokens in the request headers to be authorized.
    If the user tries to add a quiz without the correct tokens, they will receive a 401 unauthorized response.
    If the user tries to add a quiz with the correct tokens, the quiz will be added to the Quiz model.
    If the quiz is added successfully, the user will receive a 201 created response.
    If the quiz is not added successfully, the user will receive a 400 bad request response.
    If the user tries to add a quiz that already exists in the Quiz model, the user will receive a 404 Alredy exists repoonse.'''
class QuizAddView(APIView):
    '''Post view for Quiz model'''
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request): 
        # Get token1 and token2 from the request headers
        # If the tokens are not valid, return a access denied response
        token1 = request.headers.get('Token1')
        token2 = request.headers.get('Token2')
        
        user = User()        

        if not user.is_authorized(token1, token2):
            return Response(status=status.HTTP_401_UNAUTHORIZED)        
        '''Post method for Quiz model'''
        quiz_serializer = QuizSerializer(data=request.data)
        '''If the quiz for the submitted category already exists in the Quiz model, return a 404 Already exists response'''
        if Quiz.objects.filter(category=request.data['category']).exists():
            return Response(status=status.HTTP_409_CONFLICT)
        '''If the quiz is valid, save the quiz and return a 201 created response'''
        if quiz_serializer.is_valid():
            quiz_serializer.save()
            return Response(quiz_serializer.data, status=status.HTTP_201_CREATED)
        return Response(quiz_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
''' A class for updating a quiz in the Quiz model.'''
class QuizUpdateView(APIView):
    '''Put method for Quiz model'''
    parser_classes = (MultiPartParser, FormParser)
    def put(self, request, id):
         # Get token1 and token2 from the request headers
        # If the tokens are not valid, return a access denied response
        token1 = request.headers.get('Token1')
        token2 = request.headers.get('Token2')
        
        user = User()        

        if not user.is_authorized(token1, token2):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        '''Put method for Quiz model'''
        try:
            quiz = Quiz.objects.get(id=id)
        except Quiz.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        quiz_serializer = QuizSerializer(quiz, data=request.data)
        if quiz_serializer.is_valid():
            quiz_serializer.save()
            return Response(quiz_serializer.data)
        return Response(quiz_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
''' A class for deleting a quiz from the Quiz model.'''
class QuizDeleteView(APIView):
    '''Delete method for Quiz model'''
    def delete(self, request, id):
        '''Delete method for Quiz model'''
         # Get token1 and token2 from the request headers
        # If the tokens are not valid, return a access denied response
        token1 = request.headers.get('Token1')
        token2 = request.headers.get('Token2')
        
        user = User()        

        if not user.is_authorized(token1, token2):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        quiz = Quiz.objects.get(id=id)

        if API_MEDIA_STORAGE == 'MEDIA_FOLDER':
            '''If the quiz is deleted, delete the media file associated with the quiz'''
            media_json_path = os.path.join(MEDIA_ROOT, str(quiz.json))            
            if os.path.exists(media_json_path):                
                os.remove(media_json_path)
            else:
                print("The file does not exist")
        '''Delete the quiz'''
        quiz.delete()
        '''Return a 204 no content response'''
        return Response(status=status.HTTP_204_NO_CONTENT)