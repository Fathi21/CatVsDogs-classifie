from django.urls import path
from . import views # Correct import path

urlpatterns = [
    path('uploadImage/', views.UploadUpImage, name='UploadUpImage'),
    path('GetUploadImage/', views.GetUploadImage, name='GetUploadImage'),
    path('SaveThePrediction/', views.SavePrediction, name='SaveThePrediction')
]