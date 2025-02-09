from django.urls import path
from . import views # Correct import path

urlpatterns = [
    path('uploadImage/', views.UploadImage, name='uploadImage'),
    path('SaveThePrediction/', views.SavePrediction, name='SaveThePrediction')
]