from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'phone', 'student_type', 'preferred_day', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Your phone'}),
            'message': forms.Textarea(attrs={'placeholder': 'Any additional info'}),
        }