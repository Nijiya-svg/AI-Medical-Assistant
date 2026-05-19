from rest_framework import serializers
from .models import Symptom
from users.serializers import UserSerializer

class SymptomSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Symptom
        fields = '__all__'