from rest_framework import serializers
from .models import ChatHistory
from users.serializers import UserSerializer

class ChatHistorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ChatHistory
        fields = '__all__'