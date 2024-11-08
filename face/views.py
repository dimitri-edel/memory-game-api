from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from category.models import Category
from face.models import Face
from face.serializers import FaceSerializer
from game_admin.authentication import User
import os
from memory_game_api.settings import API_MEDIA_STORAGE
from memory_game_api.settings import MEDIA_ROOT
from memory_game_api.settings import ALLOWED_CLIENT_HOSTS
