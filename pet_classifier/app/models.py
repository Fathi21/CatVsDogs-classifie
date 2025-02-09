from django.db import models

# Create your models here.

class UploadImage(models.Model):
    image = models.ImageField(upload_to='uploads/')  # Images saved to MEDIA_ROOT/uploads/
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.image})"
    

class saveThePrediction(models.Model):
    imageId = models.ForeignKey(UploadImage, on_delete=models.CASCADE)
    prediction = models.CharField(max_length=10)     # 'cat' or 'dog'
    confidence = models.FloatField()                 # e.g., 0.92
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prediction} ({self.confidence:.2f})"