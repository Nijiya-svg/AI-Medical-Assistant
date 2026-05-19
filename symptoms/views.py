from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Symptom
from .forms import SymptomForm
from .utils import analyze_symptoms
from rest_framework import viewsets
from .serializers import SymptomSerializer

# Create your views here.

@login_required
def symptom_checker(request):
    if request.method == 'POST':
        form = SymptomForm(request.POST)
        if form.is_valid():
            symptom = form.save(commit=False)
            symptom.user = request.user
            # Simple AI logic
            symptom.predicted_condition, symptom.recommended_specialist = analyze_symptoms(symptom.symptoms)
            symptom.save()
            messages.success(request, f'Possible condition: {symptom.predicted_condition}. Recommended: {symptom.recommended_specialist}')
            return redirect('symptom_history')
    else:
        form = SymptomForm()
    return render(request, 'symptoms/symptom_checker.html', {'form': form})

@login_required
def symptom_history(request):
    symptoms = Symptom.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'symptoms/symptom_history.html', {'symptoms': symptoms})

class SymptomViewSet(viewsets.ModelViewSet):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer
