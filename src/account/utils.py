from django.conf import settings
from kavenegar import KavenegarAPI, APIException, HTTPException


def send_otp_code(phone, code):
    try:
        api = KavenegarAPI(settings.KAVENEGAR_API_KEY)
        params = {
            'sender': '',
            'receptor': phone,
            'message': f'کد تایید شما: {code}\nفروشگاه دری شاپ',
        }
        api.sms_send(params)
    except APIException as err:
        print(err)
    except HTTPException as err:
        print(err)
