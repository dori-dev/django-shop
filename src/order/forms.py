from django import forms


class ApplyCouponForm(forms.Form):
    code = forms.CharField(
        max_length=64,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter coupon...',
            }
        )
    )
