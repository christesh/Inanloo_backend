from django.contrib import admin

from .models import (
    IndividualDevice,
    SoldIndividualDevice
)
# Register your models here.
admin.site.register(IndividualDevice)
admin.site.register(SoldIndividualDevice)