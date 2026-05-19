from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views
from users.views import patient_profile

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accounts/login/', views.AdminAwareLoginView.as_view(), name='login'),
    path('accounts/profile/', patient_profile, name='profile'),
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
]