# Web Email with Django project

Root account:
- user: admin
- password: root


In settings need to change for email (smtp.biz):
- EMAIL_HOST_USER = 'YOUR_HOST_NAME'
- EMAIL_HOST_PASSWORD = 'YOUR_PASS_HOST'

In settings need to change for Celery:
- CELERY_BROKER_URL = 'redis://:password@host:11535/0'
- CELERY_RESULT_BACKEND = 'redis://:password@host:11535/0'