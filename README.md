# Django Shop
Full modern shop created with Django.


## Celery Beat
```bash
celery -A config beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

## Install Supervisor
```bash
sudo apt install supervisor
sudo pacman -S supervisor
```

all supervisor processes goes here in: `/etc/supervisor.d/`

## Initialize
```bash
touch /etc/supervisor.d/shop.init
nano /etc/supervisor.d/shop.init
```

write this in `shop.init`

```txt
[program:shop]
user=user
directory=/var/www/shop/src/
command=/var/www/shop/env/bin/celery -A config worker -l info
numprocs=1
autostart=true
autorestart=true
stdout_logfile=/var/log/shop/celery.log
stderr_logfile=/var/log/shop/celery.err.log
```


create log files:
```bash
touch /var/log/shop/celery.log
touch /var/log/shop/celery.err.log
```

## Usage

```bash
supervisorctl reread
supervisorctl update

supervisorctl {status|start|stop|restart} shop
```
