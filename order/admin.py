from django.contrib import admin
from .models import (
    KindOfOrder,
    OrderTimeRange,
    OrderStatus,
    Order,
    OrderDetails,

)
# Register your models here.
admin.site.register(KindOfOrder)
admin.site.register(OrderTimeRange)
admin.site.register(OrderStatus)
admin.site.register(Order)
admin.site.register(OrderDetails)
