# url patterns for the quiz app
'''Url patterns for the playlist app'''
from django.urls import path
from .views import QuizView

urlpatterns = [
    path('get-all-quizzes/<str:filter>/<str:api_key>', QuizView.as_view(), name='get-all-quizzes'),
]