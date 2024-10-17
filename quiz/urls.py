# url patterns for the quiz app
'''Url patterns for the playlist app'''
from django.urls import path
from .views import QuizListView
from .views import QuizAddView

urlpatterns = [
    path('get-all-quizzes/<str:filter>/<str:api_key>', QuizListView.as_view(), name='get-all-quizzes'),
    path('post/', QuizAddView.as_view(), name='add-quiz'),
]