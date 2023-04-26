from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class JsonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'connector_apps.Json'
    verbose_name = _('Json')
