from django import forms
from .models import AdoptablePet

class AdoptablePetForm(forms.ModelForm):
    class Meta:
        model = AdoptablePet
        fields = '__all__'
