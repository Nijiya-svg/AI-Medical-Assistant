from rest_framework import serializers
from .models import Appointment
from doctors.serializers import DoctorSerializer
from users.serializers import UserSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    patient = UserSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = Appointment
        fields = '__all__'