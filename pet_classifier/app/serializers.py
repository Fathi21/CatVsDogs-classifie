from rest_framework import serializers
from .models import *

class ImageUploadSerializer(serializers.Serializer):
    model = UploadImage
    fields ='__all__' 


class ThePredictionSerializer(serializers.Serializer):
    model = saveThePrediction
    fields ='__all__' 

