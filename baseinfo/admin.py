from django.contrib import admin
from baseinfo.models import (
    Regions,
    ProvinceGeofence,
    # Provinces,
    RegionsGeofence,
)

admin.site.register(Regions)
admin.site.register(ProvinceGeofence)
# admin.site.register(Provinces)
admin.site.register(RegionsGeofence)
