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

    path('gettimerange/', GetTimeRange.as_view()),
    path('getallorders/', GetAllOrders.as_view()),
    path('getuserstatusorders/', GetUserStatusOrders.as_view()),
    path('getalluserorders/', GetAllUserOrders.as_view()),
    path('getalltechorders/', GetAllTechOrders.as_view()),
    path('gettechstatusorders/', GetTechStatusOrders.as_view()),
    path('gettechopenorders/', GetTechOpenOrders.as_view()),
    path('sendordertotechnician/',SendOrderToTechnician.as_view()),
    path('sendordernotification/',SendOrderNotification.as_view()),
    path('sendmessagenotification/',SendMessageNotification.as_view()),
    path('sendcallnotification/',SendCallNotification.as_view()),
    path('getorder/',GetOrder.as_view()),
    path('accepetorder/',AccepetOrder.as_view()),
    path('cancelorderbytechnician/',CancelOrderByTechnician.as_view()),
    path('RejectOrder/',RejectOrder.as_view()),
    path('CancelOrderByUser/',CancelOrderByUser.as_view()),
    path('getallorderstatus/',GetAllOrderStatus.as_view()),
    path('gettechnicianchecklist/',GetTechnicianChecklist.as_view()),

]