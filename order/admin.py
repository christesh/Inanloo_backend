from django.contrib import admin
from personal.models import (
    Person,
    Mobiles,
    Provinces,
    Phones,
    Addresses,
    PersonAuth
)

admin.site.register(Person)
admin.site.register(Mobiles)
admin.site.register(Provinces)
admin.site.register(Phones)
admin.site.register(Addresses)
admin.site.register(PersonAuth)