from django import forms
from .models import AdoptablePet, AdoptionInterest


class AdoptablePetForm(forms.ModelForm):
    class Meta:
        model = AdoptablePet
        fields = '__all__'

class AdoptionInterestForm(forms.ModelForm):
    class Meta:
        model = AdoptionInterest
        fields = ['name', 'email', 'phone', 'message']
