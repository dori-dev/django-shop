from django.urls import reverse
from django.conf import settings


if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'

BASE_URL = f"https://{sandbox}.zarinpal.com/pg"
ZP_API_REQUEST = f"{BASE_URL}/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"{BASE_URL}/rest/WebGate/PaymentVerification.json"
ZP_API_START_PAY = f"{BASE_URL}/StartPay/"

DESCRIPTION = "Pay {cost} Toman for {quantity} products."

CALLBACK_URL = None


def verify_absolute_url(request):
    path = reverse('payment:verify')
    host = request.META.get('HTTP_HOST')
    return f"{request.scheme}://{host}{path}"
