from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'chats', views.ChatHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('chat/', views.chatbot, name='chatbot'),
    path('history/', views.chat_history, name='chat_history'),
]