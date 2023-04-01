expire in otp
5 times enter code
login
user creation form
    def link(self, model):
        url = model.get_absolute_url()
        return format_html(
            f'<a target="_blank" href="{url}">Url</a>'
        )
admin category and product url

redis-server
celery -A config worker -l INFO
async otp send with celery
login with otp
forgot password
python manage.py clean_otp


class OtpCode(models.Model):
    phone = models.CharField(
        max_length=11,
        unique=True
    )

for celery beat:
celery -A config beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
