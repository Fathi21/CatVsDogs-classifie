from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
from .predict import CatDogClassifier
from .serializers import *
from .models import UploadImage
import os

##os.chdir("Models")
# Load the model
model_path = os.path.join(os.path.dirname(__file__), 'Model', 'cat_dog_classifier.h5')
classifier = CatDogClassifier(model_path)

@api_view(['POST'])
def UploadUpImage(request):
    # Validate the uploaded file
    serializer = ImageUploadSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    return Response(serializer.errors, status=status.HTTP_200_OK)


        # # Save the uploaded image
        # uploaded_image = serializer.validated_data['image']
        # file_name = default_storage.save(uploaded_image.name, uploaded_image)
        # file_path = default_storage.path(file_name)

        # try:
        #     # Make a prediction
        #     result = classifier.predict(file_path)
        #     response_data = {'result': result}
        #     return Response(response_data, status=status.HTTP_200_OK)
        # except Exception as e:
        #     return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        # #finally:
        #     # Delete the uploaded image after prediction
        #     #default_storage.delete(file_name)

@api_view(['GET'])
def GetUploadImage(request):
    
    if request.method == 'GET':
        # Get the data from the database.
        data = UploadImage.objects.all()

        # Serialize the data.
        serializer = ImageUploadSerializer(data, many=True)

        # Return the data.
        return Response(serializer.data)


@api_view(['POST'])
def SavePrediction(request):
    try:
        data = request.data  # Data is already parsed by JSONParser
        print(data)

        # Check if imageId exists and is valid
        if 'imageId' not in data:
            return Response({'error': 'imageId is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            upload_image = UploadImage.objects.get(pk=data['imageId'])
        except UploadImage.DoesNotExist:
            return Response({'error': 'Invalid imageId'}, status=status.HTTP_400_BAD_REQUEST)

        # Modify data to include the UploadImage instance
        data['imageId'] = upload_image

        serializer = ThePredictionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)  # Print errors for debugging
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except json.JSONDecodeError:
        return Response({'error': 'Invalid JSON data'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)  # Print errors for debugging
        return Response({'error': 'An error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)