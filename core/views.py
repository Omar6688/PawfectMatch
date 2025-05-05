from django.shortcuts import render, get_object_or_404
from .models import Pet

def home(request):
    pets = Pet.objects.all()
    return render(request, 'core/home.html', {'pets': pets})

def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'core/pet_detail.html', {'pet': pet})
