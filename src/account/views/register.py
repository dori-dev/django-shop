from django.shortcuts import render
from django.views import View

from account import forms


class RegisterView(View):
    form_class = forms.RegistrationForm

    def get(self, request):
        form = self.form_class
        context = {
            'form': form,
        }
        return render(request, 'account/register.html', context)

    def post(self, request):
        pass
