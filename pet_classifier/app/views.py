import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.files.storage import default_storage
from .predict import CatDogClassifier
from .serializers import *
from .models import UploadImage
import os
import numpy as np

##os.chdir("Models")
# Load the model
model_path = os.path.join(os.path.dirname(__file__), 'Model', 'cat_dog_classifier.h5')
classifier = CatDogClassifier(model_path)

@api_view(['POST'])
def UploadUpImage(request):
    # Validate the uploaded file
    serializer = ImageUploadSerializer(data=request.data)
    print(serializer.is_valid())
    if serializer.is_valid():
        serializer.save()  # <--- THIS IS THE KEY: Save the serializer!
        return Response({'message': 'Image uploaded successfully', 'image_url': serializer.data['image']}, status=status.HTTP_201_CREATED) # 201 Created is better

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def GetUploadedImages(request):
    
    if request.method == 'GET':
        # Get the data from the database.
        images = UploadImage.objects.all()

        # Serialize the data.
        serializer = ImageUploadSerializer(images, many=True)

        # Return the data.
        return Response(serializer.data)

@api_view(['GET'])
def GetUploadedImageById(request, pk):
    
    if request.method == 'GET':
        # Get the data from the database.
        image = UploadImage.objects.filter(id=pk)
        
        # Serialize the data.
        serializer = ImageUploadSerializer(image, many=True)

        # Return the data.
        return Response(serializer.data)

@api_view(['POST'])
def SavePrediction(request):
    try:
        data = request.data
        print("Received data:", data)  # Debug print

        if 'imageId' not in data:
            return Response({'error': 'imageId is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            image_id = int(data['imageId'])  # Convert to integer immediately
            upload_image = UploadImage.objects.get(pk=image_id)
        except (ValueError, TypeError):
            return Response({'error': 'Invalid imageId (must be an integer)'}, status=status.HTTP_400_BAD_REQUEST)
        except UploadImage.DoesNotExist:
            return Response({'error': 'Invalid imageId'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if a prediction already exists for this imageId
        existing_prediction = saveThePrediction.objects.filter(imageId=upload_image).first()
        if existing_prediction:
            return Response({'error': 'Prediction already exists for this imageId'}, status=status.HTTP_400_BAD_REQUEST)

        image_path = upload_image.image.path  # Get path AFTER checking ID

        prediction_result = classifier.predict(image_path)

        if prediction_result == "Error":
            return Response({'error': 'Prediction failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        data['prediction'] = prediction_result[0]
        data['confidence'] = prediction_result[1]
        data['imageId'] = upload_image.id  # Use upload_image.id

        serializer = ThePredictionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Serializer errors:", serializer.errors)  # Print serializer errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except json.JSONDecodeError:
        return Response({'error': 'Invalid JSON data'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(f"An error occurred: {e}")
        return Response({'error': 'An error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET'])
def getPredictions(request):
    predictions = saveThePrediction.objects.all()
    serializer = ThePredictionSerializer(predictions, many=True)
    return Response(serializer.data) 


@api_view(['GET'])
def getPredictionsByImageid(request, image_id):
    try:
        predictions = saveThePrediction.objects.filter(imageId=image_id)
        if not predictions.exists():
            return Response({"error": "No predictions found for this imageId"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ThePredictionSerializer(predictions, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)