from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MongodbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'connector_apps.Mongodb'
    verbose_name = _('Mongodb')
