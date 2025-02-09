from rest_framework import serializers
from .models import *

class ImageUploadSerializer(serializers.ModelSerializer):  # Or serializers.Serializer if not using ModelSerializer
 
    class Meta:
        model = UploadImage
        fields = '__all__'  # Or ['image', 'created_at', ...] - list the fields explicitly


class ThePredictionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = saveThePrediction
        fields = '__all__' 

