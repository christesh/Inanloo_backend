from django.contrib import admin
from .models import (
    KindOfOrder,
    OrderTimeRange,
    OrderStatus,
    Order,
    OrderDetails,
    CustomerProblems,
    TechnicianProblems,CustomerProblemPic,
    TechnicianOrdersSended,
    CustomerApplianceGuarantee,
    CustomerApplianceInvoice,
    CustomerAppliance,
    TechnicianProblemPic,
    CanselReason,
    OrderCancelReason,
    OrderLog
)
# Register your models here.
admin.site.register(KindOfOrder)
admin.site.register(TechnicianOrdersSended)
admin.site.register(OrderTimeRange)
admin.site.register(OrderStatus)
admin.site.register(Order)
admin.site.register(OrderDetails)
admin.site.register(CustomerProblems)
admin.site.register(TechnicianProblems)
admin.site.register(CustomerProblemPic)
admin.site.register(CustomerApplianceGuarantee)
admin.site.register(CustomerApplianceInvoice)
admin.site.register(CustomerAppliance)
admin.site.register(TechnicianProblemPic)
admin.site.register(CanselReason)
admin.site.register(OrderCancelReason)
admin.site.register(OrderLog)
