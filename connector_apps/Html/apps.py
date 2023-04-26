from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HtmlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'connector_apps.Html'
    verbose_name = _('Html')
