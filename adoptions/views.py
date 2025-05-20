from django.shortcuts import render, redirect, get_object_or_404
from .models import AdoptablePet
from django.contrib.admin.views.decorators import staff_member_required
from .forms import AdoptablePetForm
from .forms import AdoptionInterestForm
from django.http import HttpResponseServerError
import traceback


def adoptable_list(request):
    pets = AdoptablePet.objects.all()
    return render(request, 'adoptions/adoptable_list.html', {'pets': pets})


def adoptable_detail(request, pk):
    pet = get_object_or_404(AdoptablePet, pk=pk)
    return render(request, 'adoptions/adoptable_detail.html', {'pet': pet})


@staff_member_required
def add_pet(request):
    if request.method == 'POST':
        form = AdoptablePetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adoptable_list')
    else:
        form = AdoptablePetForm()
    return render(request, 'adoptions/adoptable_form.html', {'form': form, 'action': 'Add'})


@staff_member_required
def edit_pet(request, pk):
    pet = get_object_or_404(AdoptablePet, pk=pk)
    if request.method == 'POST':
        form = AdoptablePetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('adoptable_list')
    else:
        form = AdoptablePetForm(instance=pet)
    return render(request, 'adoptions/adoptable_form.html', {'form': form, 'action': 'Edit'})


@staff_member_required
def delete_pet(request, pk):
    pet = get_object_or_404(AdoptablePet, pk=pk)
    if request.method == 'POST':
        pet.delete()
        return redirect('adoptable_list')
    return render(request, 'adoptions/adoptable_confirm_delete.html', {'pet': pet})


import logging

logger = logging.getLogger(__name__)

def express_interest(request, pk):
    pet = get_object_or_404(AdoptablePet, pk=pk)

    if request.method == 'POST':
        form = AdoptionInterestForm(request.POST)
        if form.is_valid():
            interest = form.save(commit=False)
            interest.pet = pet
            interest.save()
            try:
                logger.info("Trying to render interest_success.html for pet: %s", pet.name)
                return render(request, 'adoptions/interest_success.html', {'pet': pet})
            except Exception as e:
                logger.error("Failed to render interest_success.html: %s", e)
                return render(request, 'core/500.html')  # fallback template if needed
    else:
        form = AdoptionInterestForm()

    return render(request, 'adoptions/express_interest.html', {
        'form': form,
        'pet': pet
    })
