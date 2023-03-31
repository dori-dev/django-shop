from datetime import timedelta
from django.utils.timezone import now
from django.core.management.base import BaseCommand
from account.models import OtpCode


class Command(BaseCommand):
    help = 'remove all expired otp codes.'

    def handle(self, *args, **options):
        expired_time = now() - timedelta(minutes=2)
        otp_qs = OtpCode.objects.filter(
            created__lt=expired_time,
        )
        count = otp_qs.count()
        otp_qs.delete()
        self.stdout.write(
            f'{count} expired otp objects removed successfully.'
        )
