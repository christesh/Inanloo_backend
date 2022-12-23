import requests
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
# from websocket.consumers import ChatConsumer
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.db.models import Q,F
# Create your views here.
from fcm_django.models import FCMDevice
from rest_framework.authtoken.models import Token

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
        # try:
        order = self.request.data.get('order')
        print(type(order))
        if isinstance(order, str):
            order=json.loads(order)
            print(type(order))
        customer =Customers.objects.get(id=order['customerID'])
        registerBy=self.request.user
        registerDateTime=datetime.now()
        try:
            problemPics = dict((request.data).lists())['problemPics']
            if (order['hasGuarantee']):
                customer = Customers.objects.get(id=order['customerID'])
                applianceModel = Appliances.objects.get(id=order['modelID'])
                applianceSerial = order['deviceSerial']
                ca = CustomerAppliance(customer=customer, applianceModel=applianceModel,
                                       applianceSerial=applianceSerial)
                ca.save()
                customerAppliance = ca.id

                guaranteePic=dict((request.data).lists())(order['guaranteePic'])
                for gpic in guaranteePic:
                    sd = order['guaranteeStartDate'].split('/')
                    gsd = jdatetime.date(int(sd[0]), int(sd[1]), int(sd[2])).togregorian()
                    ed = order['guaranteeEndDate'].split('/')
                    esd = jdatetime.date(int(ed[0]), int(ed[1]), int(ed[2])).togregorian()
                    modified_data = g_files(customerAppliance,gpic,gsd,esd)
                    file_serializer = CustomerOrderApplianceGuarantee(data=modified_data)
                    if file_serializer.is_valid():
                        file_serializer.save()

                invoicePic = dict((request.data).lists())(order['invoicePic'])
                for ipic in invoicePic:
                    modified_data = i_files(customerAppliance, ipic)
                    file_serializer = CustomerOrderApplianceInvoice(data=modified_data)
                    if file_serializer.is_valid():
                        file_serializer.save()
        except:
            problemPics=[]
        brand =ApplianceBrands.objects.get(id=order['brandID'])
        od=order['orderDate'].split('/')
        orderDate =jdatetime.date(int(od[0]),int(od[1]),int(od[2])).togregorian()
        orderTimeRange=OrderTimeRange.objects.get(id=order['timeRange'])
        orderAddress =Addresses.objects.get(id=order['orderAddressID'])
        orderStatus =OrderStatus.objects.get(id=1)
        orderobj=Order(
            customer = customer,
            registerBy =registerBy,
            registerDateTime=registerDateTime,
            applianceBrand=brand,
            orderDate = orderDate,
            orderTimeRange=orderTimeRange,
            orderAddress=orderAddress,
            orderStatus=orderStatus,
            hasGuarantee=order['hasGuarantee'],
            applianceModel_id=order['modelID'],
            applianceSerial=order['modelSerial']
        )
        orderobj.save()
        # order problem pic
        cnt = 0
        arr = []
        print("problem pic:")
        print(problemPics)
        for img_name in problemPics:
            modified_data = modify_input_for_multiple_files(orderobj.id,
                                                            img_name)
            file_serializer = CustomerOrderProblemPic(data=modified_data)
            if file_serializer.is_valid():
                cnt += 1
                file_serializer.save()
                arr.append(file_serializer.data)

        # order customer problem
        for problem in order['problem']:
            if problem['type']=='category':
                cp=CustomerProblems(
                    order_id=orderobj.id,
                    categoryProblem_id=problem['pID'],
                )
                cp.save()
            if problem['type']=='brand':
                cp=CustomerProblems(
                    order_id=orderobj.id,
                    brandproblem_id=problem['pID'],
                )
                cp.save()
            if problem['type']=='model':
                cp=CustomerProblems(
                    order_id=orderobj.id,
                    modelProblem_id=problem['pID'],
                )
                cp.save()
        # cept Exception as e:
        #   print(e)
        #   return Response({'result': 'error ' + str(e)})
        return Response({'result':'order id:'+str(orderobj.id)})


def modify_input_for_multiple_files(property_id, image):
    dict = {}
    dict['order'] = property_id
    dict['problemImage'] = image
    return dict

def g_files(property_id, image,startdate,enddate):
    dict = {}
    dict['customerAppliance'] = property_id
    dict['guaranteePic'] = image
    dict['guaranteeStartDate'] = startdate
    dict['guaranteeEndDate'] = enddate
    return dict

def i_files(property_id, image):
    dict = {}
    dict['customerAppliance'] = property_id
    dict['invoicePic'] = image
    return dict


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


class GetTimeRange(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        tr=OrderTimeRange.objects.all().values()
        return Response(tr)

class GetAllOrders(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        order=Order.objects.all()
        orders=OrderSerializer(order,many=True)
        encoder = DjangoJSONEncoder()
        allOrder = encoder.encode(orders.data)
        json_orders = json.loads(allOrder)
        all=[]
        for order in json_orders:
            cp = CustomerProblems.objects.filter(order_id=order['id']).values()
            cpall = []
            for p in cp:
                print(p)
                if p['categoryProblem_id'] != None:
                    catp = ApllianceCategoryProblems.objects.filter(id=p['categoryProblem_id']).values()
                    for ctp in catp:
                        cpall.append(ctp)
                if p['brandproblem_id'] != None:
                    catp = BarndsProblems.objects.filter(id=p['brandproblem_id']).values()
                    for ctp in catp:
                        cpall.append(ctp)
                if p['modelProblem_id'] != None:
                    catp = Problems.objects.filter(id=p['modelProblem_id']).values()
                    for ctp in catp:
                        cpall.append(ctp)

            tp = TechnicianProblems.objects.filter(order_id=order['id']).values()
            tpall = []
            for p in tp:
                if p['categoryProblem_id'] != None:
                    catp = ApllianceCategoryProblems.objects.filter(id=p['categoryProblem_id']).values()
                    for ctp in catp:
                        tpall.append(ctp)
                if p['brandproblem_id'] != None:
                    catp = BarndsProblems.objects.filter(id=p['brandproblem_id']).values()
                    for ctp in catp:
                        tpall.append(ctp)
                if p['modelProblem_id'] != None:
                    catp = Problems.objects.filter(id=p['modelProblem_id']).values()
                    for ctp in catp:
                        tpall.append(ctp)
            cpPic0 = CustomerProblemPic.objects.filter(order_id=order['id'])
            cpPic = CustomerProblemPicSerializer(cpPic0, many=True).data
            tpPic0 = TechnicianProblemPic.objects.filter(order_id=order['id'])
            tpPic = TechnicianProblemPicSerializer(tpPic0, many=True).data
            cag = []
            cai = []
            if order['applianceModel'] is not None:
                capp = CustomerAppliance.objects.filter(Q(applianceModel=order['applianceModel']['ID']),
                                                        Q(applianceSerial=order['applianceSerial'])).values('id')
                if capp.exists():
                    cag0 = CustomerApplianceGuarantee.objects.filter(customerAppliance_id=capp[0]['id'])
                    cag = CustomerOrderApplianceGuarantee(cag0, many=True).data
                    cai0 = CustomerApplianceInvoice.objects.filter(customerAppliance_id=capp[0]['id'])
                    cai = CustomerOrderApplianceInvoice(cai0, many=True).data
                else:
                    cag = []
                    cai = []
            order['applianceGuarantee'] = cag
            order['applianceInvoice'] = cai
            order['customerProblem']=cpall
            order['customerProblemPic'] = cpPic
            order['technicianProblem']=tpall
            order['technicianProblemPic']=tpPic
            all.append(order)
        return Response(all)


class GetAllUserOrders(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request, *args, **kwargs):
        uid=self.request.data.get('userID')
        order=Order.objects.filter(customer_id=uid)
        orders=OrderSerializer(order,many=True)
        encoder = DjangoJSONEncoder()
        allOrder = sorted(
            orders.data, key=lambda k: k['registerDateTime'], reverse=True)
        allOrder = encoder.encode(allOrder)
        json_orders = json.loads(allOrder)
        all=[]
        for order in json_orders:
            cp = CustomerProblems.objects.filter(order_id=order['id']).values()
            cpall=[]
            for p in cp:
                print(p)
                if p['categoryProblem_id'] != None:
                    catp=ApllianceCategoryProblems.objects.filter(id=p['categoryProblem_id']).values()
                    for ctp in catp:
                        cpall.append(ctp)
                if p['brandproblem_id'] != None:
                    catp=BarndsProblems.objects.filter(id=p['brandproblem_id']).values()
                    for ctp in catp:
                        cpall.append(ctp)
                if p['modelProblem_id'] != None:
                    catp=Problems.objects.filter(id=p['modelProblem_id']).values()
                    for ctp in catp:
                        cpall.append(ctp)

            tp = TechnicianProblems.objects.filter(order_id=order['id']).values()
            tpall = []
            for p in tp:
                if p['categoryProblem_id'] != None:
                    catp = ApllianceCategoryProblems.objects.filter(id=p['categoryProblem_id']).values()
                    for ctp in catp:
                        tpall.append(ctp)
                if p['brandproblem_id'] != None:
                    catp = BarndsProblems.objects.filter(id=p['brandproblem_id']).values()
                    for ctp in catp:
                        tpall.append(ctp)
                if p['modelProblem_id'] != None:
                    catp = Problems.objects.filter(id=p['modelProblem_id']).values()
                    for ctp in catp:
                        tpall.append(ctp)
            cpPic0 = CustomerProblemPic.objects.filter(order_id=order['id'])
            cpPic = CustomerProblemPicSerializer(cpPic0, many=True).data
            tpPic0 = TechnicianProblemPic.objects.filter(order_id=order['id'])
            tpPic = TechnicianProblemPicSerializer(tpPic0, many=True).data
            cag = []
            cai = []
            if order['applianceModel'] is not None:
                capp = CustomerAppliance.objects.filter(Q(applianceModel=order['applianceModel']['ID']),
                                                    Q(applianceSerial=order['applianceSerial'])).values('id')
                if capp.exists():
                    cag0 = CustomerApplianceGuarantee.objects.filter(customerAppliance_id=capp[0]['id'])
                    cag=CustomerOrderApplianceGuarantee(cag0,many=True).data
                    cai0 = CustomerApplianceInvoice.objects.filter(customerAppliance_id=capp[0]['id'])
                    cai = CustomerOrderApplianceInvoice(cai0, many=True).data
                else:
                    cag = []
                    cai = []

            order['applianceGuarantee'] = cag
            order['applianceInvoice'] = cai
            order['customerProblem']=cpall
            order['customerProblemPic'] = cpPic
            order['technicianProblem']=tpall
            order['technicianProblemPic']=tpPic
            all.append(order)
        return Response(all)

class GetUserStatusOrders(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request, *args, **kwargs):
        uid=self.request.data.get('userID')
        st=self.request.data.get('status')
        order=Order.objects.filter(customer_id=uid,orderStatus_id=st)
        orders=OrderSerializer(order,many=True)
        encoder = DjangoJSONEncoder()
        allOrder = encoder.encode(orders.data)
        json_orders = json.loads(allOrder)
        all=[]
        for order in json_orders:
            cp = CustomerProblems.objects.filter(order_id=order['id']).values()
            cpall = []
            for p in cp:
                print(p)
                if p['categoryProblem_id'] != None:
                    catp = ApllianceCategoryProblems.objects.filter(id=p['categoryProblem_id']).values()
                    for ctp in catp:
                        cpall.append(ctp)
                if p['brandproblem_id'] != None:
                    catp = BarndsProblems.objects.filter(id=p['brandproblem_id']).values()
                    for ctp in catp:
                        cpall.append(ctp)
                if p['modelProblem_id'] != None:
                    catp = Problems.objects.filter(id=p['modelProblem_id']).values()
                    for ctp in catp:
                        cpall.append(ctp)

            tp = TechnicianProblems.objects.filter(order_id=order['id']).values()
            tpall = []
            for p in tp:
                if p['categoryProblem_id'] != None:
                    catp = ApllianceCategoryProblems.objects.filter(id=p['categoryProblem_id']).values()
                    for ctp in catp:
                        tpall.append(ctp)
                if p['brandproblem_id'] != None:
                    catp = BarndsProblems.objects.filter(id=p['brandproblem_id']).values()
                    for ctp in catp:
                        tpall.append(ctp)
                if p['modelProblem_id'] != None:
                    catp = Problems.objects.filter(id=p['modelProblem_id']).values()
                    for ctp in catp:
                        tpall.append(ctp)
            cpPic0 = CustomerProblemPic.objects.filter(order_id=order['id'])
            cpPic = CustomerProblemPicSerializer(cpPic0, many=True).data
            tpPic0 = TechnicianProblemPic.objects.filter(order_id=order['id'])
            tpPic = TechnicianProblemPicSerializer(tpPic0, many=True).data
            cag = []
            cai = []
            if order['applianceModel'] is not None:
                capp = CustomerAppliance.objects.filter(Q(applianceModel=order['applianceModel']['ID']),
                                                        Q(applianceSerial=order['applianceSerial'])).values('id')
                if capp.exists():
                    cag0 = CustomerApplianceGuarantee.objects.filter(customerAppliance_id=capp[0]['id'])
                    cag = CustomerOrderApplianceGuarantee(cag0, many=True).data
                    cai0 = CustomerApplianceInvoice.objects.filter(customerAppliance_id=capp[0]['id'])
                    cai = CustomerOrderApplianceInvoice(cai0, many=True).data
                else:
                    cag = []
                    cai = []

            order['applianceGuarantee'] = cag
            order['applianceInvoice'] = cai
            order['customerProblem']=cp
            order['customerProblemPic'] = cpPic
            order['technicianProblem']=tpall
            order['technicianProblemPic']=tpPic
            all.append(order)
        return Response(all)


class GetAllTechOrders(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request, *args, **kwargs):
        tid=self.request.data.get('techID')
        order=Order.objects.filter(technician_id=tid)
        orders=OrderSerializer(order,many=True)
        encoder = DjangoJSONEncoder()
        allOrder = sorted(
            orders.data, key=lambda k: k['registerDateTime'], reverse=True)
        allOrder = encoder.encode(orders.data)
        json_orders = json.loads(allOrder)
        all=[]
        for order in json_orders:
            cp = CustomerProblems.objects.filter(order_id=order['id']).values()
            cpall = []
            for p in cp:
                print(p)
                if p['categoryProblem_id'] != None:
                    catp = ApllianceCategoryProblems.objects.filter(id=p['categoryProblem_id']).values()
                    for ctp in catp:
                        cpall.append(ctp)
                if p['brandproblem_id'] != None:
                    catp = BarndsProblems.objects.filter(id=p['brandproblem_id']).values()
                    for ctp in catp:
                        cpall.append(ctp)
                if p['modelProblem_id'] != None:
                    catp = Problems.objects.filter(id=p['modelProblem_id']).values()
                    for ctp in catp:
                        cpall.append(ctp)

            tp = TechnicianProblems.objects.filter(order_id=order['id']).values()
            tpall = []
            for p in tp:
                if p['categoryProblem_id'] != None:
                    catp = ApllianceCategoryProblems.objects.filter(id=p['categoryProblem_id']).values()
                    for ctp in catp:
                        tpall.append(ctp)
                if p['brandproblem_id'] != None:
                    catp = BarndsProblems.objects.filter(id=p['brandproblem_id']).values()
                    for ctp in catp:
                        tpall.append(ctp)
                if p['modelProblem_id'] != None:
                    catp = Problems.objects.filter(id=p['modelProblem_id']).values()
                    for ctp in catp:
                        tpall.append(ctp)
            cpPic0 = CustomerProblemPic.objects.filter(order_id=order['id'])
            cpPic = CustomerProblemPicSerializer(cpPic0, many=True).data
            tpPic0 = TechnicianProblemPic.objects.filter(order_id=order['id'])
            tpPic = TechnicianProblemPicSerializer(tpPic0, many=True).data
            cag = []
            cai = []
            if order['applianceModel'] is not None:
                capp = CustomerAppliance.objects.filter(Q(applianceModel=order['applianceModel']['ID']),
                                                        Q(applianceSerial=order['applianceSerial'])).values('id')
                if capp.exists():
                    cag0 = CustomerApplianceGuarantee.objects.filter(customerAppliance_id=capp[0]['id'])
                    cag = CustomerOrderApplianceGuarantee(cag0, many=True).data
                    cai0 = CustomerApplianceInvoice.objects.filter(customerAppliance_id=capp[0]['id'])
                    cai = CustomerOrderApplianceInvoice(cai0, many=True).data
                else:
                    cag = []
                    cai = []
            order['applianceGuarantee'] = cag
            order['applianceInvoice'] = cai
            order['customerProblem']=cpall
            order['customerProblemPic'] = cpPic
            order['technicianProblem']=tpall
            order['technicianProblemPic']=tpPic
            all.append(order)
        return Response(all)


class GetOrder(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request, *args, **kwargs):
        orderid=self.request.data.get('orderID')
        order=Order.objects.filter(id=orderid)
        orders=OrderSerializer(order,many=True)
        encoder = DjangoJSONEncoder()
        allOrder = sorted(
            orders.data, key=lambda k: k['registerDateTime'], reverse=True)
        allOrder = encoder.encode(orders.data)
        json_orders = json.loads(allOrder)
        all=[]
        for order in json_orders:
            cp = CustomerProblems.objects.filter(order_id=order['id']).values()
            cpall = []
            for p in cp:

                if p['categoryProblem_id'] != None:
                    catp = ApllianceCategoryProblems.objects.filter(id=p['categoryProblem_id']).values()
                    for ctp in catp:
                        cpall.append(ctp)
                if p['brandproblem_id'] != None:
                    catp = BarndsProblems.objects.filter(id=p['brandproblem_id']).values()
                    for ctp in catp:
                        cpall.append(ctp)
                if p['modelProblem_id'] != None:
                    catp = Problems.objects.filter(id=p['modelProblem_id']).values()
                    for ctp in catp:
                        cpall.append(ctp)

            tp = TechnicianProblems.objects.filter(order_id=order['id']).values()
            tpall = []
            for p in tp:
                if p['categoryProblem_id'] != None:
                    catp = ApllianceCategoryProblems.objects.filter(id=p['categoryProblem_id']).values()
                    for ctp in catp:
                        tpall.append(ctp)
                if p['brandproblem_id'] != None:
                    catp = BarndsProblems.objects.filter(id=p['brandproblem_id']).values()
                    for ctp in catp:
                        tpall.append(ctp)
                if p['modelProblem_id'] != None:
                    catp = Problems.objects.filter(id=p['modelProblem_id']).values()
                    for ctp in catp:
                        tpall.append(ctp)
            cpPic0 = CustomerProblemPic.objects.filter(order_id=order['id'])
            cpPic = CustomerProblemPicSerializer(cpPic0, many=True).data
            tpPic0 = TechnicianProblemPic.objects.filter(order_id=order['id'])
            tpPic = TechnicianProblemPicSerializer(tpPic0, many=True).data
            cag = []
            cai = []
            if order['applianceModel'] is not None:
                capp = CustomerAppliance.objects.filter(Q(applianceModel=order['applianceModel']['ID']),
                                                        Q(applianceSerial=order['applianceSerial'])).values('id')
                if capp.exists():
                    cag0 = CustomerApplianceGuarantee.objects.filter(customerAppliance_id=capp[0]['id'])
                    cag = CustomerOrderApplianceGuarantee(cag0, many=True).data
                    cai0 = CustomerApplianceInvoice.objects.filter(customerAppliance_id=capp[0]['id'])
                    cai = CustomerOrderApplianceInvoice(cai0, many=True).data
                else:
                    cag = []
                    cai = []

            order['applianceGuarantee'] = cag
            order['applianceInvoice'] = cai
            order['customerProblem']=cpall
            order['customerProblemPic'] = cpPic
            order['technicianProblem']=tpall
            order['technicianProblemPic']=tpPic
            all.append(order)
        return Response(all)


class GetTechStatusOrders(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request, *args, **kwargs):
        tid=self.request.data.get('techID')
        st = self.request.data.get('status')
        order=Order.objects.filter(technician_id=tid,orderStatus_id=st)
        orders=OrderSerializer(order,many=True)
        encoder = DjangoJSONEncoder()
        allOrder = encoder.encode(orders.data)
        json_orders = json.loads(allOrder)
        all=[]
        for order in json_orders:
            cp = CustomerProblems.objects.filter(order_id=order['id']).values()
            cpall = []
            for p in cp:
                print(p)
                if p['categoryProblem_id'] != None:
                    catp = ApllianceCategoryProblems.objects.filter(id=p['categoryProblem_id']).values()
                    for ctp in catp:
                        cpall.append(ctp)
                if p['brandproblem_id'] != None:
                    catp = BarndsProblems.objects.filter(id=p['brandproblem_id']).values()
                    for ctp in catp:
                        cpall.append(ctp)
                if p['modelProblem_id'] != None:
                    catp = Problems.objects.filter(id=p['modelProblem_id']).values()
                    for ctp in catp:
                        cpall.append(ctp)

            tp = TechnicianProblems.objects.filter(order_id=order['id']).values()
            tpall = []
            for p in tp:
                if p['categoryProblem_id'] != None:
                    catp = ApllianceCategoryProblems.objects.filter(id=p['categoryProblem_id']).values()
                    for ctp in catp:
                        tpall.append(ctp)
                if p['brandproblem_id'] != None:
                    catp = BarndsProblems.objects.filter(id=p['brandproblem_id']).values()
                    for ctp in catp:
                        tpall.append(ctp)
                if p['modelProblem_id'] != None:
                    catp = Problems.objects.filter(id=p['modelProblem_id']).values()
                    for ctp in catp:
                        tpall.append(ctp)
            cpPic0=CustomerProblemPic.objects.filter(order_id=order['id'])
            cpPic=CustomerProblemPicSerializer(cpPic0,many=True)
            tpPic0=TechnicianProblemPic.objects.filter(order_id=order['id'])
            tpPic = TechnicianProblemPicSerializer(tpPic0, many=True)
            cag = []
            cai = []
            if order['applianceModel'] is not None:
                capp = CustomerAppliance.objects.filter(Q(applianceModel=order['applianceModel']['ID']),
                                                        Q(applianceSerial=order['applianceSerial'])).values('id')
                if capp.exists():
                    cag0 = CustomerApplianceGuarantee.objects.filter(customerAppliance_id=capp[0]['id'])
                    cag = CustomerOrderApplianceGuarantee(cag0, many=True).data
                    cai0 = CustomerApplianceInvoice.objects.filter(customerAppliance_id=capp[0]['id'])
                    cai = CustomerOrderApplianceInvoice(cai0, many=True).data
                else:
                    cag = []
                    cai = []

            order['applianceGuarantee'] = cag
            order['applianceInvoice'] = cai
            order['customerProblem']=cp
            order['customerProblemPic'] = cpPic
            order['technicianProblem']=tpall
            order['technicianProblemPic']=tpPic
            all.append(order)
        return Response(all)

class GetTechOpenOrders(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request, *args, **kwargs):
        tid=self.request.data.get('techID')
        order=Order.objects.filter(technician_id=tid).exclude(Q(orderStatus_id=4) | Q(orderStatus_id=5))
        orders = OrderSerializer(order, many=True)
        encoder = DjangoJSONEncoder()
        allOrder = encoder.encode(orders.data)
        json_orders = json.loads(allOrder)
        all = []
        for order in json_orders:
            cp = CustomerProblems.objects.filter(order_id=order['id']).values()
            cpall = []
            for p in cp:
                print(p)
                if p['categoryProblem_id'] != None:
                    catp = ApllianceCategoryProblems.objects.filter(id=p['categoryProblem_id']).values()
                    for ctp in catp:
                        cpall.append(ctp)
                if p['brandproblem_id'] != None:
                    catp = BarndsProblems.objects.filter(id=p['brandproblem_id']).values()
                    for ctp in catp:
                        cpall.append(ctp)
                if p['modelProblem_id'] != None:
                    catp = Problems.objects.filter(id=p['modelProblem_id']).values()
                    for ctp in catp:
                        cpall.append(ctp)

            tp = TechnicianProblems.objects.filter(order_id=order['id']).values()
            tpall = []
            for p in tp:
                if p['categoryProblem_id'] != None:
                    catp = ApllianceCategoryProblems.objects.filter(id=p['categoryProblem_id']).values()
                    for ctp in catp:
                        tpall.append(ctp)
                if p['brandproblem_id'] != None:
                    catp = BarndsProblems.objects.filter(id=p['brandproblem_id']).values()
                    for ctp in catp:
                        tpall.append(ctp)
                if p['modelProblem_id'] != None:
                    catp = Problems.objects.filter(id=p['modelProblem_id']).values()
                    for ctp in catp:
                        tpall.append(ctp)
            cpPic0 = CustomerProblemPic.objects.filter(order_id=order['id'])
            cpPic = CustomerProblemPicSerializer(cpPic0, many=True).data
            tpPic0 = TechnicianProblemPic.objects.filter(order_id=order['id'])
            tpPic = TechnicianProblemPicSerializer(tpPic0, many=True).data
            cag = []
            cai = []
            if order['applianceModel'] is not None:
                capp = CustomerAppliance.objects.filter(Q(applianceModel=order['applianceModel']['ID']),
                                                        Q(applianceSerial=order['applianceSerial'])).values('id')
                if capp.exists():
                    cag0 = CustomerApplianceGuarantee.objects.filter(customerAppliance_id=capp[0]['id'])
                    cag = CustomerOrderApplianceGuarantee(cag0, many=True).data
                    cai0 = CustomerApplianceInvoice.objects.filter(customerAppliance_id=capp[0]['id'])
                    cai = CustomerOrderApplianceInvoice(cai0, many=True).data
                else:
                    cag = []
                    cai = []

            order['applianceGuarantee'] = cag
            order['applianceInvoice'] = cai
            order['customerProblem'] = cp
            order['customerProblemPic'] = cpPic
            order['technicianProblem'] = tpall
            order['technicianProblemPic'] = tpPic
            all.append(order)
        return Response(all)


class SendOrderToTechnician(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            techid=self.request.data.get('techID')
            orderid=self.request.data.get('orderID')
        except:
            print(self.args)
            return
        print("sdasdasdasd")
        order=Order.objects.filter(id=orderid).values('applianceBrand__a_brandName',
                                                      'applianceBrand__a_brandImage',
                                                      'applianceBrand__a_barndCategory__a_categoryName',
                                                      'applianceBrand__a_barndCategory__a_categoryImage',
                                                      'applianceModel__applianceModel',
                                                      'orderDate',
                                                      'orderTimeRange__timeRange',
                                                      'orderAddress__city__cityName',
                                                      'orderAddress__region__regionName',
                                                      'orderKind__orderKind')
        od = str(order[0]['orderDate']).split('-')
        orderDate = jdatetime.date.fromgregorian(year=int(od[0]), month=int(od[1]), day=int(od[2]))
        orderDate=str(orderDate).replace('-','/')
        fcmToken=FCMDevice.objects.filter(user_id=techid).values('registration_id')
        cp = CustomerProblems.objects.filter(order_id=orderid).values()
        cpall = []
        lowp=0
        highp=0

        for p in cp:

            if p['categoryProblem_id'] != None:
                catp = ApllianceCategoryProblems.objects.filter(id=p['categoryProblem_id']).values()
                lowp=lowp+int(catp[0]['lowPrice'])
                highp=highp+int(catp[0]['highPrice'])
                cpall.append(catp[0])
            if p['brandproblem_id'] != None:
                catp = BarndsProblems.objects.filter(id=p['brandproblem_id']).values()
                lowp = lowp + int(catp[0]['lowPrice'])
                highp = highp + int(catp[0]['highPrice'])
                cpall.append(catp[0])
            if p['modelProblem_id'] != None:
                catp = Problems.objects.filter(id=p['modelProblem_id']).values()
                lowp = lowp + int(catp[0]['lowPrice'])
                highp = highp + int(catp[0]['highPrice'])
                cpall.append(catp[0])
        amunt="از"+str(lowp)+"تا"+str(highp)+" ريال"
        print(cpall)
        data={"subtitle":"Elementary School",
              "to":fcmToken[0]['registration_id'],
              "notification" : {
                  "body" : "order",
                  "OrganizationId":"2",
                  "content_available" : "true",
                  "subtitle":"نصب",
                  "title":"سفارش جدید",
                  "priorty" : "high",
                  "click_action": "ir.mersaGroup.inanloService.expert.NewOrderActivity" },
              "data" : {
                  "orderID":orderid,
                  "orderKind":str(order[0]['orderKind__orderKind']),
                  "sound":"app_sound.wav",
                  "content_available" : "true",
                  "bodyText" : "New Announcement assigned",
                  "amount" : amunt,
                  "appliance":str(order[0]['applianceBrand__a_barndCategory__a_categoryName']),
                  "appliancePic":str(order[0]['applianceBrand__a_barndCategory__a_categoryImage']),
                  "brand":str(order[0]['applianceBrand__a_brandName']),
                  "brandPic":str(order[0]['applianceBrand__a_brandImage']),
                  "model":str(order[0]['applianceModel__applianceModel']),
                  "date":str(orderDate),
                  "timerange":str(order[0]['orderTimeRange__timeRange']),
                  "address":str(order[0]['orderAddress__city__cityName'])+", "+str(order[0]['orderAddress__region__regionName'])+", ...",
                  "problems":cpall,
                  "organization" :"Elementary school"},
              "priorty":"high",
              "android":{"priorty":"high"},
              "apns":{"headers":{"apns-priority":"4"}},
              "webpush": {"headers": {"Urgency":"high"}}
              }
        headers = {
            "Content-Type":"application/json",
            "Authorization": "key=AAAABTqObrE:APA91bEI5r_lm3hcG-Cx6e8EOlp7BPG2GEhrMnhIlpH0dPEIy7yzcplh9yilzHv9dK6bSGifdZLUL65wvkF0F2hofjKL_stYpE9m5yz7DavuhqnMvfS0mUSLSdorlgHPAPOYAFDzHhHk"}

        r = requests.post('https://fcm.googleapis.com/fcm/send', data=json.dumps(data), headers=headers)
        return Response(r)



class AccepetOrder(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        uid= self.request.user.id
        order=Order.objects.get(id=self.request.data.get('orderID'))
        pid=PersonAuth.objects.filter(user_id=uid).values('person_id')
        tech=Technician.objects.get(id__in=pid)
        order.technician=tech
        order.orderStatus.id=15
        order.save()
        actionDatetime = datetime.now()
        orderlog=OrderLog(
            order=order,
            editedItems='technician',
            editedValue=tech.id,
            actionDatetime=actionDatetime
        )
        orderlog.save()
        orderlog = OrderLog(
            order=order,
            editedItems='status',
            editedValue='15',
            actionDatetime = actionDatetime
        )
        orderlog.save()
        return Response({'result':'order was accpeted'})


class CancelOrderByTechnician(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        uid= self.request.user.id
        order=Order.objects.get(id=self.request.data.get('orderID'))
        pid=PersonAuth.objects.filter(user_id=uid).values('person_id')
        reason=CanselReason.objects.filter(user_id=uid).values('reason_id')
        tech=Technician.objects.get(id__in=pid)
        order.technician=None
        order.orderStatus.id=5
        order.save()
        ordercancelreason=OrderCancelReason.objects.get(id=self.request.data.get('orderID'))
        ordercancelreason.cancelReason=reason
        ordercancelreason.save()
        orderlog=OrderLog(
            order=order,
            editedItems='technician',
            editedValue=None
        )
        orderlog.save()
        orderlog = OrderLog(
            order=order,
            editedItems='status',
            editedValue='5'
        )
        orderlog.save()
        techid=selectTechnician(order.id)
        r = sendordertotech(techid, order.id)
        return Response({'result':'order was canceled by Tech and open again'})


class CancelOrderByUser(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        uid= self.request.user.id
        order=Order.objects.get(id=self.request.data.get('orderID'))
        order.orderStatus.id=16
        order.save()

        orderlog = OrderLog(
            order=order,
            editedItems='status',
            editedValue='16'
        )
        orderlog.save()
        return Response({'result':'order was canceled by Customer'})

class RejectOrder(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        uid = self.request.user.id
        order = Order.objects.get(id=self.request.data.get('orderID'))
        pid = PersonAuth.objects.filter(user_id=uid).values('person_id')
        tech = Technician.objects.get(id__in=pid)


        rejectorder = RejectedOrders(
            order=order,
            Technician=tech,
            rejectDateTime=datetime.now()
        )
        rejectorder.save()
        return Response({'result':'order was rejected by technician'})

class GetAllOrderStatus(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        res = []
        orderstatus = OrderStatus.objects.all().values()
        res.append({'order_status': orderstatus})
        reason = CanselReason.objects.all().values()
        res.append({'cancel_reason': reason})
        return Response(res)

class SendOrderNotification(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        techid = techid = selectTechnician('orderID')
        orderid = self.request.data.get('orderID')
        r=sendordertotech(techid,orderid)
        return Response(r)

class SendMessageNotification(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        senderID = self.request.data.get('senderID')
        reciverID=self.request.data.get('reciverID')
        message = self.request.data.get('message')

        r=SendMessageToUser(senderID,reciverID,message)
        return Response(r)

class SendCallNotification(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        callerID = self.request.data.get('callerID')
        Number = self.request.data.get('Number')
        r=NewCall(callerID,Number)
        return Response(r)




class GetTechnicianChecklist(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
            categoryID = self.request.data.get('categoryID')
            barndID = self.request.data.get('brandID')
            modelID = self.request.data.get('modelID')
            if categoryID == "":
                categoryID = "-1"
            if barndID == "":
                barndID = "-1"
            if modelID == "":
                modelID = "-1"
            print(modelID)
            catPromble = AppliancesCategoryCheckList.objects.filter(appliancescategory_id=categoryID).values('id',
                                                                                                           'checklistTitle',
                                                                                                           'Description')
            brandPromble = BrandsChecklist.objects.filter(appliancesBrands_id=barndID).values('id',
                                                                                              'checklistTitle',
                                                                                              'Description')
            ModelPromble = ModelsChecklist.objects.filter(appliances_id=modelID).values('id',
                                                                                        'checklistTitle',
                                                                                        'Description')
            qs = []
            for item in catPromble:
                item['pkind'] = 'category'
                qs.append(item)
            for item in brandPromble:
                item['pkind'] = 'brand'
                qs.append(item)
            for item in ModelPromble:
                item['pkind'] = 'model'
                qs.append(item)

            return Response(qs)

def sendordertotech(techid,orderid):
        order=Order.objects.filter(id=orderid).values('applianceBrand__a_brandName',
                                                      'applianceBrand__a_brandImage',
                                                      'applianceBrand__a_barndCategory__a_categoryName',
                                                      'applianceBrand__a_barndCategory__a_categoryImage',
                                                      'applianceModel__applianceModel',
                                                      'orderDate',
                                                      'orderTimeRange__timeRange',
                                                      'orderAddress__city__cityName',
                                                      'orderAddress__region__regionName',
                                                      'orderKind__orderKind')
        od = str(order[0]['orderDate']).split('-')
        orderDate = jdatetime.date.fromgregorian(year=int(od[0]), month=int(od[1]), day=int(od[2]))
        orderDate=str(orderDate).replace('-','/')
        fcmToken=FCMDevice.objects.filter(user_id=techid).values('registration_id')
        cp = CustomerProblems.objects.filter(order_id=orderid).values()
        cpall = []
        lowp=0
        highp=0

        for p in cp:

            if p['categoryProblem_id'] != None:
                catp = ApllianceCategoryProblems.objects.filter(id=p['categoryProblem_id']).values()
                lowp=lowp+int(catp[0]['lowPrice'])
                highp=highp+int(catp[0]['highPrice'])
                cpall.append(catp[0])
            if p['brandproblem_id'] != None:
                catp = BarndsProblems.objects.filter(id=p['brandproblem_id']).values()
                lowp = lowp + int(catp[0]['lowPrice'])
                highp = highp + int(catp[0]['highPrice'])
                cpall.append(catp[0])
            if p['modelProblem_id'] != None:
                catp = Problems.objects.filter(id=p['modelProblem_id']).values()
                lowp = lowp + int(catp[0]['lowPrice'])
                highp = highp + int(catp[0]['highPrice'])
                cpall.append(catp[0])
        amunt="از"+str(lowp)+"تا"+str(highp)+" ريال"
        print(cpall)
        data={"subtitle":"Elementary School",
              "to":fcmToken[0]['registration_id'],
              "notification" : {
                  "body" : "order",
                  "OrganizationId":"2",
                  "content_available" : "true",
                  "subtitle":"نصب",
                  "title":"سفارش جدید",
                  "priorty" : "high",
                  "click_action": "ir.mersaGroup.inanloService.expert.NewOrderActivity" },
              "data" : {
                  "orderID":orderid,
                  "orderKind":str(order[0]['orderKind__orderKind']),
                  "sound":"app_sound.wav",
                  "content_available" : "true",
                  "bodyText" : "New Announcement assigned",
                  "amount" : amunt,
                  "appliance":str(order[0]['applianceBrand__a_barndCategory__a_categoryName']),
                  "appliancePic":str(order[0]['applianceBrand__a_barndCategory__a_categoryImage']),
                  "brand":str(order[0]['applianceBrand__a_brandName']),
                  "brandPic":str(order[0]['applianceBrand__a_brandImage']),
                  "model":str(order[0]['applianceModel__applianceModel']),
                  "date":str(orderDate),
                  "timerange":str(order[0]['orderTimeRange__timeRange']),
                  "address":str(order[0]['orderAddress__city__cityName'])+", "+str(order[0]['orderAddress__region__regionName'])+", ...",
                  "problems":cpall,
                  "organization" :"Elementary school"},
              "priorty":"high",
              "android":{"priorty":"high"},
              "apns":{"headers":{"apns-priority":"4"}},
              "webpush": {"headers": {"Urgency":"high"}}
              }
        headers = {
            "Content-Type":"application/json",
            "Authorization": "key=AAAABTqObrE:APA91bEI5r_lm3hcG-Cx6e8EOlp7BPG2GEhrMnhIlpH0dPEIy7yzcplh9yilzHv9dK6bSGifdZLUL65wvkF0F2hofjKL_stYpE9m5yz7DavuhqnMvfS0mUSLSdorlgHPAPOYAFDzHhHk"}

        r = requests.post('https://fcm.googleapis.com/fcm/send', data=json.dumps(data), headers=headers)
        return r


def SendMessageToUser(senderid,reciverid, message):
    uid=PersonAuth.objects.filter(user_id=senderid).values('person_id','person__firstName','person__lastName','person__picture')
    fcmToken = FCMDevice.objects.filter(user_id=reciverid).values('registration_id')
    data = {"subtitle": "Elementary School",
            "to": fcmToken[0]['registration_id'],
            "notification": {
                "body": "Message",
                "OrganizationId": "2",
                "content_available": "true",
                "subtitle": "پبام",
                "title": "پیام جدید",
                "priorty": "high",
                "click_action": "ir.mersaGroup.inanloService.expert.NewOrderActivity"},
            "data": {
                "message":message,
                "sender":uid[0],
                "datetime":str(datetime.now())
                },
            "priorty": "high",
            "android": {"priorty": "high"},
            "apns": {"headers": {"apns-priority": "4"}},
            "webpush": {"headers": {"Urgency": "high"}}
            }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "key=AAAABTqObrE:APA91bEI5r_lm3hcG-Cx6e8EOlp7BPG2GEhrMnhIlpH0dPEIy7yzcplh9yilzHv9dK6bSGifdZLUL65wvkF0F2hofjKL_stYpE9m5yz7DavuhqnMvfS0mUSLSdorlgHPAPOYAFDzHhHk"}

    r = requests.post('https://fcm.googleapis.com/fcm/send', data=json.dumps(data), headers=headers)
    return r



def NewCall(userid,caller):
    print(caller)
    p=Mobiles.objects.filter(mobileNumber=caller)
    print(p)
    if (p.exists()):
        person=Mobiles.objects.filter(mobileNumber=caller).values('person_id','person__firstName','person__lastName',
                                                                  'person__picture',tel=F('mobileNumber'))
        print(person)
        callperson=person[0]
    else:
        q = Phones.objects.filter(mobileNumber=caller)
        if (q.exits()):
            person = Phones.objects.filter(mobileNumber=caller).values('person_id', 'person__firstName',
                                                                    'person__lastName','person__picture',tel=F('phoneNumber'))
            callperson = person[0]
        else:
            callperson={'tel':caller}


    fcmToken = FCMDevice.objects.filter(user_id=userid).values('registration_id')
    data = {"subtitle": "Elementary School",
            "to": fcmToken[0]['registration_id'],
            "notification": {
                "body": "Call",
                "OrganizationId": "2",
                "content_available": "true",
                "subtitle": "تماس",
                "title": "تماس جدید",
                "priorty": "high",
                "click_action": "ir.mersaGroup.inanloService.expert.NewOrderActivity"},
            "data": {
                "caller":callperson
                },
            "priorty": "high",
            "android": {"priorty": "high"},
            "apns": {"headers": {"apns-priority": "4"}},
            "webpush": {"headers": {"Urgency": "high"}}
            }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "key=AAAABTqObrE:APA91bEI5r_lm3hcG-Cx6e8EOlp7BPG2GEhrMnhIlpH0dPEIy7yzcplh9yilzHv9dK6bSGifdZLUL65wvkF0F2hofjKL_stYpE9m5yz7DavuhqnMvfS0mUSLSdorlgHPAPOYAFDzHhHk"}

    r = requests.post('https://fcm.googleapis.com/fcm/send', data=json.dumps(data), headers=headers)
    return r


def selectTechnician(orderID):
    techid=[]
    return techid
