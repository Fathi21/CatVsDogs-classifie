from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.

admin.site.register(UploadImage)
admin.site.register(saveThePrediction)