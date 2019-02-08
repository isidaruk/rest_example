from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include

from rest_framework.schemas import get_schema_view


schema_view = get_schema_view(title='House For Rent API')

urlpatterns = [
    path('', include('houses.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('schema/', schema_view),
    path('admin/', admin.site.urls),
]
