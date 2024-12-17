"""
WSGI config for app_config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_config.settings')

# application = get_wsgi_application()

import os
import sys

from django.core.wsgi import get_wsgi_application

print("FILE_PATH: ", os.path.dirname(__file__))
print("PROJECT_NAME: ", os.path.basename(os.path.dirname(__file__)))

FILE_PATH = os.path.dirname(__file__)
PROJECT_NAME = os.path.basename("~/waripoke.xyz/public_html/waripoke/app_config")

sys.path.append(os.path.dirname("~/waripoke.xyz/public_html/waripoke/app_config"))
sys.path.append("~/waripoke.xyz/public_html/waripoke/app_config")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_config" + ".settings")

application = get_wsgi_application()
