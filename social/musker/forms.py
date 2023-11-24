from django import forms
from .models import Meep
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MeepForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter Your Musker Meep!',
                'class': 'form-control',
                }
                ),
                label='',)
    
    class Meta:
        model = Meep
        exclude = ('user',)


