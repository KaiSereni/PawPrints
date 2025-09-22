import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pawprints.settings")
django.setup()

from pawprints.routing import application
