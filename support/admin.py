from django.contrib import admin
from .models import (
    TechnicianNegativePoints,
    TechnicianPositivePoints,
    TechnicianSurvey,
    CustomerNegativePoints,
    CustomerPositivePoints,
    CustomerSurvey,
    TicketStatus,
    TicketPriority,
    Tickets,
    TicketChats,
)
# Register your models here.
admin.site.register(TechnicianNegativePoints)
admin.site.register(TechnicianPositivePoints)
admin.site.register(TechnicianSurvey)
admin.site.register(CustomerNegativePoints)
admin.site.register(CustomerPositivePoints)
admin.site.register(CustomerSurvey)
admin.site.register(TicketStatus)
admin.site.register(TicketPriority)
admin.site.register(Tickets)
admin.site.register(TicketChats)