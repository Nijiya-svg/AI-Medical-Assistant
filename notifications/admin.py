from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'notification_type', 'is_read', 'sent_at')
    search_fields = ('user__username', 'message', 'notification_type')
    list_filter = ('notification_type', 'is_read')
