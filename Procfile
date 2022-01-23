web: gunicorn desafioTCS.wsgi --log-file -
worker: celery -A desafioTCS beat --loglevel=debug --scheduler django_celery_beat.schedulers:DatabaseScheduler