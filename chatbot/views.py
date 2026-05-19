from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import ChatHistory
from .utils import get_chat_response
from rest_framework import viewsets
from .serializers import ChatHistorySerializer

# Create your views here.

@login_required
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = get_chat_response(message)
        ChatHistory.objects.create(user=request.user, message=message, response=response)
        return JsonResponse({'response': response})
    return render(request, 'chatbot/chatbot.html')

@login_required
def chat_history(request):
    chats = ChatHistory.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'chatbot/chat_history.html', {'chats': chats})

class ChatHistoryViewSet(viewsets.ModelViewSet):
    queryset = ChatHistory.objects.all()
    serializer_class = ChatHistorySerializer
