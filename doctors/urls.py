from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'doctors', views.DoctorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('profile/', views.doctor_profile, name='doctor_profile'),
    path('dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('list/', views.doctor_list, name='doctor_list'),
    path('<int:pk>/', views.doctor_detail, name='doctor_detail'),
]