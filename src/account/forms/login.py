from django import forms


class UserLoginForm(forms.Form):
    phone = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput,
    )
