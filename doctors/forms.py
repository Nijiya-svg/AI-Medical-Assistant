from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['specialization', 'experience_years', 'available_timings', 'consultation_fee', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }