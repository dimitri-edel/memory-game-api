from rest_framework import serializers
from .models import Style

class StyleSerializer(serializers.ModelSerializer):
    '''Serializer for Style model'''
    class Meta:
        model = Style
        fields = '__all__'
        extra_kwargs = {
            'background_image': {'required': False, 'allow_null': True},
        }
    