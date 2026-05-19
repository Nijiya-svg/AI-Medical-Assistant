from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Symptom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symptoms = models.TextField()
    predicted_condition = models.CharField(max_length=255, blank=True)
    recommended_specialist = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Symptom check by {self.user.username} - {self.predicted_condition}"
