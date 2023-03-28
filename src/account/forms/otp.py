from django import forms


class VerifyCodeForm(forms.Form):
    code = forms.CharField(max_length=4)
