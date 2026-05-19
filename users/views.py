from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Patient
from .forms import PatientForm
from rest_framework import viewsets
from .serializers import PatientSerializer

# Create your views here.

@login_required
def patient_profile(request):
    patient, created = Patient.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('patient_profile')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'users/patient_profile.html', {'form': form})

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
