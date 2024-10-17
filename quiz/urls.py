# url patterns for the quiz app
'''Url patterns for the playlist app'''
from django.urls import path
from .views import QuizListView
from .views import QuizAddView
from .views import QuizUpdateView
from .views import QuizDeleteView

urlpatterns = [
    path('get-all-quizzes/<str:filter>/<str:api_key>', QuizListView.as_view(), name='get-all-quizzes'),
    path('add/', QuizAddView.as_view(), name='add-quiz'),
    path('update/<int:id>/', QuizUpdateView.as_view(), name='update-quiz'),
    path('delete/<int:id>/', QuizDeleteView.as_view(), name='delete-quiz'),
]