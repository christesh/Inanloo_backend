from django.shortcuts import render
from .models import Order
from .serializers import *
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
import jdatetime
from personal.models import *
from django.contrib.auth.models import User, Group
from baseinfo.models import *
from .models import *
# Create your views here.

class GetAllOrders (APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

class GetCustomerOrders (APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request,*args,**kwargs):
        orders = Order.objects.filter(customer=Customers.objects.get(id=self.request.data.get('cid')))
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

class CreateOrder (APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request,*args,**kwargs):
        order = self.request.data.get('order')
        customer =Customers.objects.get(id=order['customerID'])
        registerBy =User.objects.get(id=order['registerID'])
        registerDateTime=datetime.now()

        brand =ApplianceBrands.objects.get(id=order['brandID'])
        od=order['orderDate'].split('/')
        orderDate =jdatetime.date(int(od[0]),int(od[1]),int(od[2])).togregorian()
        orderTimeRange=OrderTimeRange.objects.get(id=order['timeRange'])
        orderAddress =Addresses.objects.get(id=order['orderAddressID'])
        orderStatus =OrderStatus.objects.get(id=1)
        print('salam')
        orderobj=Order(
            customer = customer,
            registerBy =registerBy,
            registerDateTime=registerDateTime,
            applianceBrand=brand,
            orderDate = orderDate,
            orderTimeRange=orderTimeRange,
            orderAddress=orderAddress,
            orderStatus=orderStatus,
        )
        print(12)
        orderobj.save()
        return Response(orderobj.id)


class uploadCustomersProblemsPic(APIView):
    parser_class = (CustomerOrderProblemPic,)

    def post(self, request, *args, **kwargs):
        print(request.data)
        file_serializer = CustomerOrderProblemPic(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            print('salam')
            return Response({'response':'upload pics success'})
        else:
            print('bye')
            return Response({'response':'upload pics fialed'})

class CreateCustomerAppliance(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        customer = Customers.objects.get(id=self.request.data.get('cid'))
        applianceModel =Appliances.objects.get(id=self.request.data.get('aid'))
        applianceSerial=self.request.data.get('aserial')
        ca=CustomerAppliance(customer=customer,applianceModel=applianceModel,applianceSerial=applianceSerial)
        ca.save()
        return Response(ca.id)



class uploadGuaranteePic(APIView):
    parser_class = (CustomerOrderApplianceGuarantee,)

    def post(self, request, *args, **kwargs):
        print(request.data)
        file_serializer = CustomerOrderApplianceGuarantee(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            print('salam')
            return Response({'response':'upload pics success'})
        else:
            print('bye')
            return Response({'response':'upload pics fialed'})



class uploadGuaranteeInvoicePic(APIView):
    parser_class = (CustomerOrderApplianceInvoice,)

    def post(self, request, *args, **kwargs):
        print(request.data)
        file_serializer = CustomerOrderApplianceInvoice(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            print('salam')
            return Response({'response':'upload pics success'})
        else:
            print('bye')
            return Response({'response':'upload pics fialed'})