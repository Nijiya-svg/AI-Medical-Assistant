from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import RegistrationForm
from appointments.models import Appointment
from doctors.models import Doctor
from symptoms.models import Symptom
from notifications.models import Notification
from users.models import Patient

def home(request):
    return render(request, 'main/home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            age = form.cleaned_data.get('age')
            Patient.objects.create(user=user, age=age)
            login(request, user)
            messages.success(request, 'Registration successful. Welcome!')
            return redirect('dashboard')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

class AdminAwareLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        redirect_to = self.get_redirect_url()
        if redirect_to:
            return redirect_to
        if Doctor.objects.filter(user=self.request.user).exists():
            return reverse_lazy('doctor_dashboard')
        if self.request.user.is_active and self.request.user.is_staff:
            return reverse_lazy('admin:index')
        return reverse_lazy('dashboard')

@login_required
def dashboard(request):
    if Doctor.objects.filter(user=request.user).exists():
        return redirect('doctor_dashboard')
    if request.user.is_staff:
        return redirect('admin:index')

    appointments = Appointment.objects.filter(patient=request.user).order_by('date')
    symptoms = Symptom.objects.filter(user=request.user).order_by('-created_at')[:5]
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    return render(request, 'main/dashboard.html', {
        'appointments': appointments,
        'symptoms': symptoms,
        'notifications': notifications,
    })

@login_required
def doctor_dashboard(request):
    doctor = Doctor.objects.get(user=request.user)
    appointments = Appointment.objects.filter(doctor=doctor).order_by('date')
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    return render(request, 'doctors/doctor_dashboard.html', {
        'doctor': doctor,
        'appointments': appointments,
        'notifications': notifications,
    })