'''Serializer for Playlist model'''
# pylint: disable=E1101
# pylint: disable=too-few-public-methods
# pylint: disable=E0611

from rest_framework import serializers
from .models import Playlist
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    '''Serializer for Category model'''
    playlist_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {
            'image': {'required': False, 'allow_null': True},
        }

    def get_playlist_count(self, obj):
        return Playlist.objects.filter(category=obj).count()


class PlaylistSerializer(serializers.ModelSerializer):
    '''Serializer for Playlist model'''
    class Meta:
        model = Playlist
        fields = '__all__'
        
        extra_kwargs = {
            'audio': {'required': False, 'allow_null': True},
            'image': {'required': False, 'allow_null': True},
            'quiz': {'required': False, 'allow_null': True},
        }
        ''' These fields are left optional because they are not required for updating the playlist item.
            Validation is left up to the client side to decide whether to update these fields or not.
        '''

