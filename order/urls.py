from django.urls import path
from django.conf.urls import *
from rest_framework.views import View
from .views import GetAllOrders

urlpatterns = [
    path('getallorders/', GetAllOrders.as_view()),
]