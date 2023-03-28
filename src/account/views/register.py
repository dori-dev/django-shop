from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from account import forms, models, utils


class RegisterView(View):
    form_class = forms.RegistrationForm

    def get(self, request):
        form = self.form_class
        context = {
            'form': form,
        }
        return render(request, 'account/register.html', context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            phone = form.changed_data.get('phone')
            otp = models.OtpCode.objects.create(phone=phone)
            code = otp.generate_code()
            utils.send_otp_code(phone, code)
            request.session['phone'] = phone
            messages.success(
                request,
                'We send a verification code to your phone!',
                'success',
            )
            return redirect('account:verify')
        context = {
            'form': form,
        }
        return render(request, 'account/register.html', context)
