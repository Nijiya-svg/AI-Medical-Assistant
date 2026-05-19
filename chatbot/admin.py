from django.contrib import admin
from .models import ChatHistory

@admin.register(ChatHistory)
class ChatHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'message')
    search_fields = ('user__username', 'message', 'response')
    list_filter = ('timestamp',)
