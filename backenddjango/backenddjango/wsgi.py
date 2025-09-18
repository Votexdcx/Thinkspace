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
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))  # add project root to path

from cloudwatch_logging import setup_cloudwatch
setup_cloudwatch()
patch_all()
xray_recorder.configure(
    service='MyDjangoService',
    daemon_address='xray-daemon:2000',
)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backenddjango.settings')

application = get_wsgi_application()
