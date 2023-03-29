from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from account import forms, models, utils


class RegisterView(View):
    form_class = forms.RegistrationForm
    template_name = 'account/register.html'

    def get(self, request):
        form = self.form_class
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('phone')
            otp, _ = models.OtpCode.objects.get_or_create(phone=phone)
            code = otp.generate_code()
            utils.send_otp_code(phone, code)
            request.session['user'] = form.cleaned_data
            messages.success(
                request,
                'We send a verification code to your phone!',
                'success',
            )
            return redirect('account:verify')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)
