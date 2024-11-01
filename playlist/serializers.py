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
        
        extra_kwargs = {
            'audio': {'required': False, 'allow_null': True},
            'image': {'required': False, 'allow_null': True},            
        }
        ''' These fields are left optional because they are not required for updating the playlist item.
            Validation is left up to the client side to decide whether to update these fields or not.
        '''

