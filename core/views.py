from django.shortcuts import render
from .models import Pet

def home(request):
    pets = Pet.objects.all()
    return render(request, 'core/home.html', {'pets': pets})
