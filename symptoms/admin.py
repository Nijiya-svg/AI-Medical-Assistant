from django.contrib import admin
from .models import Symptom

@admin.register(Symptom)
class SymptomAdmin(admin.ModelAdmin):
    list_display = ('user', 'predicted_condition', 'recommended_specialist', 'created_at')
    search_fields = ('user__username', 'predicted_condition', 'recommended_specialist')
    list_filter = ('recommended_specialist',)
