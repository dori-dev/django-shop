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


sudo apt install supervisor
sudo pacman -S supervisor
all supervisor processes goes here in: /etc/supervisor.d/

touch /etc/supervisor.d/shop.init
nano /etc/supervisor.d/shop.init

[program:shop]
user=user
directory=/var/www/shop/src/
command=/var/www/shop/env/bin/celery -A config worker -l info
numprocs=1
autostart=true
autorestart=true
stdout_logfile=/var/log/shop/celery.log
stderr_logfile=/var/log/shop/celery.err.log

create log files:
touch /var/log/shop/celery.log
touch /var/log/shop/celery.err.log

supervisorctl reread
supervisorctl update

supervisorctl {status|start|stop|restart} shop
