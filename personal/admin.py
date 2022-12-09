from django.contrib import admin
from personal.models import (
    Customers,
    Technician,
    CompanyMembers,
    Mobiles,
    Phones,
    Addresses,
    PersonAuth,
    Supplier,
    TechnicianSkills,
    TechnicianDistricts
    # Person
)
admin.site.register(TechnicianSkills)
admin.site.register(TechnicianDistricts)
admin.site.register(CompanyMembers)
admin.site.register(Supplier)
admin.site.register(Mobiles)
admin.site.register(Phones)
admin.site.register(Addresses)
admin.site.register(PersonAuth)
admin.site.register(Customers)
admin.site.register(Technician)
# admin.site.register(Person)