from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Documentation API",
      default_version='v1',
      description="API canarinho",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="dtcontreras@drz.global"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('api-auth/', include('rest_framework.urls')),
   #path('api/v1/aws/', include('connector_apps.Aws.urls')),
   #path('api/v1/bigquery/', include('connector_apps.Bigquery.urls')),
   path('api/v1/csv/', include("connector_apps.Csv.urls")),
   #path('api/v1/html/', include('connector_apps.Html.urls')),
   #path('api/v1/json/', include('connector_apps.Json.urls')),
   #path('api/v1/mariadb/', include('connector_apps.Mariadb.urls')),
   #path('api/v1/mongodb/', include('connector_apps.Mongodb.urls')),
   #path('api/v1/mysql/', include('connector_apps.Mysql.urls')),
   #path('api/v1/postgres/', include('connector_apps.Postgres.urls')),
   #path('api/v1/xls/', include('connector_apps.Xls.urls')),
   #path('api/v1/xlsx/', include('connector_apps.Xlsx.urls')),

    
]
