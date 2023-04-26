from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BigqueryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'connector_apps.Bigquery'
    verbose_name = _('Bigquery')
