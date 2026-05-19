from django import forms
from .models import Symptom

class SymptomForm(forms.ModelForm):
    class Meta:
        model = Symptom
        fields = ['symptoms']
        widgets = {
            'symptoms': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe your symptoms...'}),
        }