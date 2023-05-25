from django.core import validators
from django import forms 
from .models import user
class studentregistration(forms.ModelForm):
    class Meta:
        model = user
        fields=['Name','Email','Password']
        widgets={'Name':forms.TextInput(attrs={'class':'form-control'}),
                 'Email':forms.EmailInput(attrs={'class':'form-control'}),
                 'Password':forms.PasswordInput(attrs={'class':'form-control'}),}

