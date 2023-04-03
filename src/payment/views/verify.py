import json
import requests

from django.shortcuts import redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.conf import settings
from django.contrib import messages

from order.models import Order
from payment.views import variables


class VerifyPaymentView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        pk = request.session.get('order')
        if pk is None or not isinstance(pk, int):
            messages.warning(
                request,
                'You should checkout your cart.'
                'warning',
            )
            return redirect('cart:detail')
        order_qs = Order.objects.filter(
            pk=pk,
        )
        if not order_qs.exists():
            # TODO: redirect to order list
            messages.error(
                request,
                f'Order with code {pk} not found to verify!'
                'danger',
            )
            return redirect('cart:detail')
        order = order_qs.first()
        if order.user != request.user:
            raise Http404
        self.order = order
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        status = request.GET.get('Status')
        if status == 'OK':
            data, headers = self.set_data(request)
            response = self.status_ok(data, headers)
            return response
        # TODO
        print('status')
        return HttpResponse('Transaction failed or canceled by user.')

    def set_data(self, request):
        authority = request.GET.get('Authority')
        amount = self.order.total_price or self.order.get_total_price()
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": amount,
            "Authority": authority,
        }
        data = json.dumps(data)
        headers = {
            'content-type': 'application/json',
            'content-length': str(len(data)),
        }
        return data, headers

    def status_ok(self, data, headers):
        response = requests.post(
            variables.ZP_API_VERIFY,
            data=data,
            headers=headers
        )
        if response.status_code == 200:
            response = response.json()
            # TODO
            print(response)
            if response['Status'] == 100:
                self.order.paid = True
                self.order.save()
                return HttpResponse(
                    f"Transaction success.\nRefID:{response['RefID']}"
                )
            elif response['Status'] == 101:
                return HttpResponse(
                    f"Transaction submitted.\nMessage:{response['Message']}"
                )
            else:
                return HttpResponse(
                    f"Transaction Field with code {response['Status']}"
                )
        return HttpResponse(
            f'Error code {response.status_code}'
        )
