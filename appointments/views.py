from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Appointment
from .forms import AppointmentForm
from doctors.models import Doctor
from rest_framework import viewsets
from .serializers import AppointmentSerializer

# Create your views here.

@login_required
def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.doctor = doctor
            appointment.save()
            messages.success(request, 'Appointment booked successfully.')
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/book_appointment.html', {'form': form, 'doctor': doctor})

@login_required
def appointment_list(request):
    appointments = Appointment.objects.filter(patient=request.user)
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})

@login_required
def cancel_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk, patient=request.user)
    if request.method == 'POST':
        appointment.status = 'cancelled'
        appointment.save()
        messages.success(request, 'Appointment cancelled.')
        return redirect('appointment_list')
    return render(request, 'appointments/cancel_appointment.html', {'appointment': appointment})

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
