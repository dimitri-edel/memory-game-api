# url patterns for the quiz app
'''Url patterns for the playlist app'''
from django.urls import path
from .views import QuizListView
from .views import QuizAddView
from .views import QuizUpdateView
from .views import QuizDeleteView
from .views import QuizGetByCategoryView

urlpatterns = [
    path('get-all/<str:filter>/', QuizListView.as_view(), name='get-all-quizzes'),
    path('get-by-category/<str:category>/', QuizGetByCategoryView.as_view(), name='get-by-category'),
    path('add/', QuizAddView.as_view(), name='add-quiz'),
    path('update/<int:id>/', QuizUpdateView.as_view(), name='update-quiz'),
    path('delete/<int:id>/', QuizDeleteView.as_view(), name='delete-quiz'),
]