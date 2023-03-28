from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import login

from account import forms, models


class VerifyView(View):
    form_class = forms.VerifyCodeForm

    def dispatch(self, request, *args, **kwargs):
        user_info = request.session.get('user')
        if user_info is None:
            messages.error(
                request,
                'First send a request to get verification code.',
                'danger',
            )
            return redirect('account:register')
        self.user_info = user_info
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        context = {
            'forms': form,
        }
        return render(request, 'account/verify.html', context)

    def post(self, request):
        otp = self.get_otp_obj(request)
        if otp is None:
            redirect('account:register')
        form = self.form_class(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get('code')
            user = self.form_valid(request, otp, code)
            if user:
                login(request, user)
                return redirect('home:index')
        context = {
            'forms': form,
        }
        return render(request, 'account/verify.html', context)

    def get_otp_obj(self, request):
        phone = self.user_info.get('phone')
        otp_qs = models.OtpCode.objects.filter(phone=phone)
        if not otp_qs.exists():
            messages.error(
                request,
                'First send a request to get verification code.',
                'danger',
            )
            return None
        return otp_qs.first()

    def form_valid(self, request, otp_obj, code):
        if code == otp_obj.code:
            user = models.User.objects.create_user(**self.user_info)
            messages.success(
                request,
                'Welcome to our shop.',
                'success',
            )
            return user
        messages.error(
            request,
            'You entered wrong verification code.',
            'danger',
        )
        return None
