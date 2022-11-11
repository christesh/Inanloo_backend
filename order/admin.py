from django.contrib import admin
from .models import (
    KindOfOrder,
    OrderTimeRange,
    OrderStatus,
    Order,
    OrderDetails,
    CustomerProblems,
    TechnicianProblems,CustomerProblemPic,

)
# Register your models here.
admin.site.register(KindOfOrder)
admin.site.register(OrderTimeRange)
admin.site.register(OrderStatus)
admin.site.register(Order)
admin.site.register(OrderDetails)
admin.site.register(CustomerProblems)
admin.site.register(TechnicianProblems)
admin.site.register(CustomerProblemPic)
