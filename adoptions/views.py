from django.shortcuts import render, get_object_or_404
from .models import AdoptablePet
from django.contrib.admin.views.decorators import staff_member_required
from .forms import AdoptablePetForm


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
