"""
WSGI config for rockolapi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from rockola.PlayListThread import PlayListThread

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rockolapi.settings")

application = get_wsgi_application()

cola = PlayListThread()
cola.setName('Cola')
cola.start()
cola.join()
