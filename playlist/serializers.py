'''Serializer for Playlist model'''
# pylint: disable=E1101
# pylint: disable=too-few-public-methods
# pylint: disable=E0611

from rest_framework import serializers
from .models import Playlist

class PlaylistSerializer(serializers.ModelSerializer):
    '''Serializer for Playlist model'''
    class Meta:
        model = Playlist
        fields = '__all__'

