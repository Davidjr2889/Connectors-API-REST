from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class XlsxConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'connector_apps.Xlsx'
    verbose_name = _('Xlsx')
