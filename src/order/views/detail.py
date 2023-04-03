from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from django.contrib import messages

from order import models
from order.forms import ApplyCouponForm


class OrderDetailView(LoginRequiredMixin, View):
    form_class = ApplyCouponForm
    template_name = 'order/detail.html'

    def dispatch(self, request, *args, **kwargs):
        order = get_object_or_404(
            models.Order,
            pk=kwargs.get('pk'),
        )
        if order.user != request.user:
            raise Http404
        self.order = order
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        context = {
            'order': self.order,
            'form': self.form_class,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        form = self.form_class(request.POST)
        if form.is_valid():
            code = form.cleaned_data.get('code')
            coupon = models.Coupon.get(code, request.user)
            if coupon is None:
                messages.error(
                    request,
                    "This coupon does not exists!",
                    'danger',
                )
            else:
                self.order.discount = coupon.discount
                self.order.save()
            return redirect('order:detail', pk=pk)
        context = {
            'order': self.order,
            'form': form,
        }
        return render(request, self.template_name, context)
