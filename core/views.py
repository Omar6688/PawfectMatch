from django.shortcuts import render
from adoptions.models import AdoptablePet

def home(request):
    pets = AdoptablePet.objects.all()
    return render(request, 'core/home.html', {'pets': pets})
