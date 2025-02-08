from django.urls import path
from .views import PredictImage  # Correct import path

urlpatterns = [
    path('predict/', PredictImage.as_view(), name='predict_image'),
]