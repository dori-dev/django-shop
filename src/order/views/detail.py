from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from order import models


class OrderDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        order = get_object_or_404(
            models.Order,
            pk=pk,
        )
        if order.user != request.user:
            raise Http404
        context = {
            'order': order,
        }
        return render(request, 'order/detail.html', context)
