"""
WSGI config for backenddjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all
from django.core.wsgi import get_wsgi_application
patch_all()
xray_recorder.configure(
    service='MyDjangoService',
    daemon_address='xray-daemon:2000',
)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backenddjango.settings')

application = get_wsgi_application()
