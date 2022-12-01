from django.urls import path
from django.conf.urls import *
from rest_framework.views import View
from .views import *

urlpatterns = [
    path('getallorders/', GetAllOrders.as_view()),
    path('createorder/', CreateOrder.as_view()),
    path('uploadcustomersproblemspic/', uploadCustomersProblemsPic.as_view()),
    path('uploadguaranteepic/', uploadGuaranteePic.as_view()),
    path('createcustomerappliance/', CreateCustomerAppliance.as_view()),
    path('uploaduaranteeinvoicepic/', uploadGuaranteeInvoicePic.as_view()),
    path('getcustomerorders/', GetCustomerOrders.as_view()),
    path('sendnotif/', sendnotif.as_view()),
    path('gettimerange/', GetTimeRange.as_view())
]