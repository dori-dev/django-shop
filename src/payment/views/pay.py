import json
import requests

from django.shortcuts import redirect, get_object_or_404
from django.http import Http404, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.conf import settings

from order.models import Order
from payment.views import variables


class PayOrderView(LoginRequiredMixin, View):
    def get(self, request, pk):
        order = get_object_or_404(
            Order,
            pk=pk,
        )
        if order.user != request.user:
            raise Http404
        data, headers = self.set_data(request, order)
        response = self.send_request(data, headers)
        return response

    @staticmethod
    def set_data(request, order: Order):
        if variables.CALLBACK_URL is None:
            variables.CALLBACK_URL = variables.verify_absolute_url(request)
        amount = order.get_total_price()
        description = variables.DESCRIPTION.format(
            amount,
            order.get_total_quantity()
        )
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": amount * 10,  # Rial
            "Description": description,
            "Phone": request.user.phone,
            "CallbackURL": variables.CALLBACK_URL,
        }
        data = json.dumps(data)
        headers = {
            'content-type': 'application/json',
            'content-length': str(len(data))
        }
        return data, headers

    @staticmethod
    def send_request(data, headers):
        try:
            response = requests.post(
                variables.ZP_API_REQUEST,
                data=data,
                headers=headers,
                timeout=10
            )
            if response.status_code == 200:
                response = response.json()
                if response['Status'] == 100:
                    return redirect(
                        variables.ZP_API_START_PAY + str(response['Authority'])
                    )
                else:
                    return HttpResponse(
                        f"There was a error with code {response['Status']}"
                    )
        except requests.exceptions.Timeout:
            return HttpResponse(
                'There is a problem with ZarinPal.'
                ' Please apply later.'
            )
        except requests.exceptions.ConnectionError:
            return HttpResponse('You are not connected to the Internet.')
        # TODO: response['errors']
        return HttpResponse(
            'There was a problem with the payment'
        )
