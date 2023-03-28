from django import forms
from django.core.exceptions import ValidationError

from account.models import User


class RegistrationForm(forms.Form):
    email = forms.EmailField()
    full_name = forms.CharField(
        label='Full Name',
    )
    phone = forms.CharField(
        max_length=11,
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = User.objects.filter(email=email)
        if user.exists():
            return ValidationError('The user with this email already exists.')
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        user = User.objects.filter(phone=phone)
        if user.exists():
            return ValidationError('The user with this phone already exists.')
        return phone
