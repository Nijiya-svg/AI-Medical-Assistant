from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification
from rest_framework import viewsets
from .serializers import NotificationSerializer

# Create your views here.

@login_required
def notification_list(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-sent_at')
    return render(request, 'notifications/notification_list.html', {'notifications': notifications})

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
