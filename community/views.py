from django.shortcuts import render, redirect
from .forms import VolunteerForm, DonationForm

# --- Volunteer View ---
def volunteer_signup(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('volunteer_thank_you')
    else:
        form = VolunteerForm()
    return render(request, 'community/volunteer.html', {'form': form})

def volunteer_thank_you(request):
    return render(request, 'community/volunteer_thank_you.html')

# --- Donate View ---
def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donation_thank_you')
    else:
        form = DonationForm()
    return render(request, 'community/donate.html', {'form': form})

def donation_thank_you(request):
    return render(request, 'community/donation_thank_you.html')

# --- Share View ---
def share(request):
    return render(request, 'community/share.html')
