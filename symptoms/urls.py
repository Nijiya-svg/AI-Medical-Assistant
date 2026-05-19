from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'symptoms', views.SymptomViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('checker/', views.symptom_checker, name='symptom_checker'),
    path('history/', views.symptom_history, name='symptom_history'),
]