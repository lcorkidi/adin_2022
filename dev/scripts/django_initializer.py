# Not working

import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AAccounting.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
APPDIR = os.environ('APPDIR')

django.setup()

# figure out how to load project models as shell_plus does