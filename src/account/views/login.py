from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, authenticate

from account import forms


class UserLoginView(View):
    form_class = forms.UserLoginForm
    template_name = 'account/login.html'

    def get(self, request):
        context = {
            'form': self.form_class,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                phone=cd['phone'],
                password=cd['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(
                    request,
                    'You logged in successfully!',
                    'success',
                )
                return redirect('home:index')
            messages.error(
                request,
                'Phone or password is wrong!',
                'danger',
            )
        context = {
            "form": form,
        }
        return render(request, self.template_name, context)
