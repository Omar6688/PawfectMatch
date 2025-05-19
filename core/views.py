from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from adoptions.models import AdoptablePet


def home(request):
    pets = AdoptablePet.objects.all()
    return render(request, 'core/home.html', {'pets': pets})


@login_required
def profile_view(request):
    """View for displaying user profile."""
    return render(request, 'core/profile.html')


def error_403(request, exception):
    return render(request, 'errors/403.html', status=403)


def error_404(request, exception):
    return render(request, 'errors/404.html', status=404)


def error_500(request):
    return render(request, 'errors/500.html', status=500)
