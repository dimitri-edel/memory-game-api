from rest_framework import serializers
from .models import Face

class FaceSerializer(serializers.ModelSerializer):
    '''Serializer for Face model'''
    class Meta:
        model = Face
        fields = '__all__'        