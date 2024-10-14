'''Serializer for Playlist model'''
# pylint: disable=E1101
# pylint: disable=too-few-public-methods
# pylint: disable=E0611

from rest_framework import serializers
from .models import Playlist
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    '''Serializer for Category model'''
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {
            'image': {'required': False, 'allow_null': True},
        }


class PlaylistSerializer(serializers.ModelSerializer):
    '''Serializer for Playlist model'''
    class Meta:
        model = Playlist
        fields = '__all__'
        extra_kwargs = {
            'audio': {'required': False, 'allow_null': True},
            'image': {'required': False, 'allow_null': True},
        }

