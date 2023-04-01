from datetime import timedelta

from django.utils.timezone import now
from celery import shared_task

from account.models import OtpCode


@shared_task
def remove_expired_otp():
    expired_time = now() - timedelta(minutes=2)
    OtpCode.objects.filter(
        created__lt=expired_time,
    ).delete()
