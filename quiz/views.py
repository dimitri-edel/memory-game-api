# import APIView from rest_framework.views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from game_admin.authentication import User
import os
from memory_game_api.settings import API_MEDIA_STORAGE
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
