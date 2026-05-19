from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField()
    available_timings = models.CharField(max_length=255, help_text="e.g., Mon-Fri 9AM-5PM")
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name} - {self.specialization}"
