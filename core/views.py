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
