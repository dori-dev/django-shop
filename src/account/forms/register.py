from django import forms


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
