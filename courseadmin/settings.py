import os

if os.environ.get('DJANGO_SETTINGS_MODULE') == 'courseadmin.settings_production':
    from .settings_production import *
else:
    from .settings_local import *
