from django.shortcuts import redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import logout


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(
            request,
            'You logged out successfully!',
            'success',
        )
        return redirect('home:index')

    def post(self, request):
        return self.get(request)
