from django.shortcuts import redirect
from django.http import HttpRequest


class SuperUserRequireMixin:
    def dispatch(self, request: HttpRequest, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        return redirect('home:index')
