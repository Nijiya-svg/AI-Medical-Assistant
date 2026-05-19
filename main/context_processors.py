from doctors.models import Doctor


def dashboard_url(request):
    if not request.user.is_authenticated:
        return {'dashboard_url': 'dashboard'}

    if Doctor.objects.filter(user=request.user).exists():
        return {'dashboard_url': 'doctor_dashboard'}

    if request.user.is_staff:
        return {'dashboard_url': 'admin:index'}

    return {'dashboard_url': 'dashboard'}
