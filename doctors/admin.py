from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'experience_years', 'available_timings', 'consultation_fee')
    search_fields = ('user__username', 'specialization')
    list_filter = ('specialization',)
