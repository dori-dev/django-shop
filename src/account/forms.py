from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from account import models


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput,
    )

    class Meta:
        model = models.User
        fields = [
            'email',
            'phone',
            'full_name',
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Confirm password don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text=(
            'You can change password using'
            ' <a href="../password/">this form</a>.'
        ),
    )

    class Meta:
        model = models.User
        fields = [
            'email',
            'phone',
            'full_name',
            'password',
            'last_login',
        ]


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
