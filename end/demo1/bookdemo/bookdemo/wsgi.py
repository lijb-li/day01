"""
WSGI config for bookdemo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

#django自带的web服务器  web Service Gate interface  网管服务接口


import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookdemo.settings')

application = get_wsgi_application()
