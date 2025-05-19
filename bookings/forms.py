from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )

    class Meta:
        model = Booking
        fields = ['name', 'email', 'service', 'date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
        }
