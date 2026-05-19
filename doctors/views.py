from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Doctor
from .forms import DoctorForm
from rest_framework import viewsets
from .serializers import DoctorSerializer
from appointments.models import Appointment
from notifications.models import Notification

# Create your views here.

@login_required
def doctor_profile(request):
    doctor, created = Doctor.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('doctor_profile')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctors/doctor_profile.html', {'form': form})

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors})

@login_required
def doctor_dashboard(request):
    doctor = get_object_or_404(Doctor, user=request.user)
    appointments = Appointment.objects.filter(doctor=doctor).order_by('date')
    appointment_counts = {
        'upcoming': appointments.filter(status='pending').count() + appointments.filter(status='confirmed').count(),
        'completed': appointments.filter(status='completed').count(),
        'pending': appointments.filter(status='pending').count(),
    }
    notifications = Notification.objects.filter(user=request.user, is_read=False).order_by('-sent_at')[:5]
    return render(request, 'doctors/doctor_dashboard.html', {
        'doctor': doctor,
        'appointments': appointments,
        'notifications': notifications,
        'appointment_counts': appointment_counts,
    })

def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'doctors/doctor_detail.html', {'doctor': doctor})

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
