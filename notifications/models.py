from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notification(models.Model):
    TYPE_CHOICES = [
        ('appointment', 'Appointment'),
        ('reminder', 'Reminder'),
        ('general', 'General'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='general')
    is_read = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification to {self.user.username} - {self.notification_type}"
