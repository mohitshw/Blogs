from django import forms
from .models import CustomUser

class SignupStepOneForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'date_of_birth']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }

class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6)

class SignupStepTwoForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username'] 