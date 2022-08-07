from django.contrib import admin
from baseinfo.models import (
    Regions,
    ProvinceGeofence,
    Provinces,
    RegionsGeofence,
    CustomerCategory,
    TechnicianCategory,
    TechnicianSkills,
    DeviceCategories,
    DeviceBrands,
    Devices,
    DesignJson,
    DesignModels,
    sms,
    MembersGroup,
    ApplianceCategories,
    ApplianceBrands,
    Appliances,
    DevicesPrice,

)
admin.site.register(MembersGroup)
admin.site.register(ApplianceCategories)
admin.site.register(ApplianceBrands)
admin.site.register(Appliances)
admin.site.register(DevicesPrice)
admin.site.register(Regions)
admin.site.register(ProvinceGeofence)
admin.site.register(Provinces)
admin.site.register(RegionsGeofence)
admin.site.register(CustomerCategory)
admin.site.register(TechnicianCategory)
admin.site.register(TechnicianSkills)
admin.site.register(DeviceCategories)
admin.site.register(DeviceBrands)
admin.site.register(Devices)
admin.site.register(DesignJson)
admin.site.register(DesignModels)
admin.site.register(sms)

