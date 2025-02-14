from rest_framework import serializers
from .models import *

class ImageUploadSerializer(serializers.ModelSerializer):  # Or serializers.Serializer if not using ModelSerializer
 
    class Meta:
        model = UploadImage
        fields = '__all__'  # Or ['image', 'created_at', ...] - list the fields explicitly


class ThePredictionSerializer(serializers.ModelSerializer):
    confidence = serializers.FloatField(required=False)
    imageId = serializers.PrimaryKeyRelatedField(queryset=UploadImage.objects.all())

    class Meta:
        model = saveThePrediction
        fields = ('imageId', 'prediction', 'confidence', 'created_at')  # Correct: Tuple of field names

