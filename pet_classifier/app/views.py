from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
from .predict import CatDogClassifier

from .serializers import ImageUploadSerializer
import os

##os.chdir("Models")
# Load the model
model_path = os.path.join(os.path.dirname(__file__), 'Model', 'cat_dog_classifier.h5')
classifier = CatDogClassifier(model_path)

class PredictImage(APIView):
    def post(self, request, *args, **kwargs):
        # Validate the uploaded file
        serializer = ImageUploadSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Save the uploaded image
        uploaded_image = serializer.validated_data['image']
        file_name = default_storage.save(uploaded_image.name, uploaded_image)
        file_path = default_storage.path(file_name)

        try:
            # Make a prediction
            result = classifier.predict(file_path)
            response_data = {'result': result}
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        #finally:
            # Delete the uploaded image after prediction
            #default_storage.delete(file_name)