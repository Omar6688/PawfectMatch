from django.shortcuts import render, get_object_or_404
from .models import AdoptablePet

def adoptable_list(request):
    pets = AdoptablePet.objects.all()
    return render(request, 'adoptions/adoptable_list.html', {'pets': pets})

def adoptable_detail(request, pk):
    pet = get_object_or_404(AdoptablePet, pk=pk)
    return render(request, 'adoptions/adoptable_detail.html', {'pet': pet})
