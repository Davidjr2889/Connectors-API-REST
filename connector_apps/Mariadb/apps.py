from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MariadbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'connector_apps.Mariadb'
    verbose_name = _('Mariadb')