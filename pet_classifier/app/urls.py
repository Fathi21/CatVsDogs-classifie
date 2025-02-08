from django.urls import path
from .views import *

urlpatterns = [
    path('predictions/', PredictImage.as_view(), name='prediction-record-list'),
]
