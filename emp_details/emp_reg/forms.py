from django.core import validators
from django import forms
from .models import emp_details

class EmpDetailsForm(forms.ModelForm):
    class Meta:
        model = emp_details
        fields = ['name', 'email', 'password']
        widgets = {
           'name': forms.TextInput(attrs={'class':'form-control'}),
           'email': forms.EmailInput(attrs={'class':'form-control'}),
           'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'})
        }
        