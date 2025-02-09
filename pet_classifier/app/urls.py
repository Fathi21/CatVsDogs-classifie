from django.urls import path
from . import views # Correct import path

urlpatterns = [
    path('Api/uploadImage', views.UploadUpImage, name='uploadImage'),
    path('Api/GetUploadedImages', views.GetUploadedImages, name='GetUploadedImages'),
    path('Api/GetUploadedImageById/<int:pk>', views.GetUploadedImageById, name='GetUploadedImageById'),
    path('Api/SaveThePrediction', views.SavePrediction, name='SaveThePrediction'),
]