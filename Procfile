release: ./db_init.sh
web: gunicorn manage:app
worker: python manage.py runworker
