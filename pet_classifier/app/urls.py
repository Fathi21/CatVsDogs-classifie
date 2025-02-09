from django.urls import path
from . import views # Correct import path

urlpatterns = [
    path('Api/uploadImage', views.UploadUpImage, name='uploadImage'),
    path('Api/GetUploadImage', views.GetUploadImage, name='GetUploadImage'),
    path('Api/SaveThePrediction', views.SavePrediction, name='SaveThePrediction'),
]