from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MysqlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'connector_apps.Mysql'
    verbose_name = _('Mysql')
