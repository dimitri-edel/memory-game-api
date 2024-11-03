# pylint: disable=E1101
# pylint: disable=too-few-public-methods
# pylint: disable=E0611

from rest_framework import serializers
from .models import Category
from playlist.models import Playlist
from quiz.models import Quiz

class CategorySerializer(serializers.ModelSerializer):
    '''Serializer for Category model'''
    playlist_count = serializers.SerializerMethodField()
    quiz_exists = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {
            'image': {'required': False, 'allow_null': True},
        }

    def get_playlist_count(self, obj):
        return Playlist.objects.filter(category=obj).count()
    
    def get_quiz_exists(self, obj):
        return Quiz.objects.filter(category=obj).exists()