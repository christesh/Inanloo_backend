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
from websocket.consumers import ChatConsumer
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.db.models import Q
# Create your views here.
from fcm_django.models import FCMDevice

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
        problemPics = order['problemPics']
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
        )
        orderobj.save()
        # order problem pic
        cnt = 0
        arr = []
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
            if problem['class']=='category':
                print(problem['pID'])
                print(orderobj.id)
                cp=CustomerProblems(
                    order_id=orderobj.id,
                    categoryProblem_id=problem['pID'],
                )
                cp.save()
            if problem['class']=='brand':
                print(problem['pID'])
                cp=CustomerProblems(
                    order_id=orderobj.id,
                    brandproblem_id=problem['pID'],
                )
                cp.save()
            if problem['class']=='model':
                print(problem['pID'])
                cp=CustomerProblems(
                    order_id=orderobj.id,
                    modelProblem_id=problem['pID'],
                )
                cp.save()

        return Response({'result':'order id:'+str(orderobj.id)})


def modify_input_for_multiple_files(property_id, image):
    dict = {}
    dict['order'] = property_id
    dict['problemImage'] = image
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
                    cpall.append(catp)
                if p['brandproblem_id'] != None:
                    catp = BarndsProblems.objects.filter(id=p['brandproblem_id']).values()
                    cpall.append(catp)
                if p['modelProblem_id'] != None:
                    catp = Problems.objects.filter(id=p['modelProblem_id']).values()
                    cpall.append(catp)

            tp=TechnicianProblems.objects.filter(order_id=order['id']).values()
            cpPic=CustomerProblemPic.objects.filter(order_id=order['id']).values()
            tpPic=TechnicianProblemPic.objects.filter(order_id=order['id']).values()
            order['customerProblem']=cp
            order['customerProblemPic'] = cpPic
            order['technicianProblem']=tp
            order['technicianProblemPic']=tpPic
            all.append(order)
        return Response(all)


class GetAllUserOrders(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request, *args, **kwargs):
        uid=self.request.data.get('userID')
        print(uid)
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
                    cpall.append(catp)
                if p['brandproblem_id'] != None:
                    catp=BarndsProblems.objects.filter(id=p['brandproblem_id']).values()
                    cpall.append(catp)
                if p['modelProblem_id'] != None:
                    catp=Problems.objects.filter(id=p['modelProblem_id']).values()
                    cpall.append(catp)

            tp=TechnicianProblems.objects.filter(order_id=order['id']).values()
            cpPic=CustomerProblemPic.objects.filter(order_id=order['id']).values()
            tpPic=TechnicianProblemPic.objects.filter(order_id=order['id']).values()
            order['customerProblem']=cpall
            order['customerProblemPic'] = cpPic
            order['technicianProblem']=tp
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
                    cpall.append(catp)
                if p['brandproblem_id'] != None:
                    catp = BarndsProblems.objects.filter(id=p['brandproblem_id']).values()
                    cpall.append(catp)
                if p['modelProblem_id'] != None:
                    catp = Problems.objects.filter(id=p['modelProblem_id']).values()
                    cpall.append(catp)

            tp=TechnicianProblems.objects.filter(order_id=order['id']).values()
            cpPic=CustomerProblemPic.objects.filter(order_id=order['id']).values()
            tpPic=TechnicianProblemPic.objects.filter(order_id=order['id']).values()
            order['customerProblem']=cp
            order['customerProblemPic'] = cpPic
            order['technicianProblem']=tp
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
                    cpall.append(catp)
                if p['brandproblem_id'] != None:
                    catp = BarndsProblems.objects.filter(id=p['brandproblem_id']).values()
                    cpall.append(catp)
                if p['modelProblem_id'] != None:
                    catp = Problems.objects.filter(id=p['modelProblem_id']).values()
                    cpall.append(catp)

            tp=TechnicianProblems.objects.filter(order_id=order['id']).values()
            cpPic=CustomerProblemPic.objects.filter(order_id=order['id']).values()
            tpPic=TechnicianProblemPic.objects.filter(order_id=order['id']).values()
            order['customerProblem']=cp
            order['customerProblemPic'] = cpPic
            order['technicianProblem']=tp
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
                    cpall.append(catp)
                if p['brandproblem_id'] != None:
                    catp = BarndsProblems.objects.filter(id=p['brandproblem_id']).values()
                    cpall.append(catp)
                if p['modelProblem_id'] != None:
                    catp = Problems.objects.filter(id=p['modelProblem_id']).values()
                    cpall.append(catp)

            tp=TechnicianProblems.objects.filter(order_id=order['id']).values()
            cpPic=CustomerProblemPic.objects.filter(order_id=order['id']).values()
            tpPic=TechnicianProblemPic.objects.filter(order_id=order['id']).values()
            order['customerProblem']=cp
            order['customerProblemPic'] = cpPic
            order['technicianProblem']=tp
            order['technicianProblemPic']=tpPic
            all.append(order)
        return Response(all)

class GetTechOpenOrders(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request, *args, **kwargs):
        tid=self.request.data.get('techID')
        order=Order.objects.filter(technician_id=tid).exclude(Q(orderStatus_id=4) | Q(orderStatus_id=5))
        orders=OrderSerializer(order,many=True)
        encoder = DjangoJSONEncoder()
        allOrder = encoder.encode(orders.data)
        json_orders = json.loads(allOrder)
        all=[]
        for order in json_orders:
            cp = CustomerProblems.objects.filter(order_id=order['id']).values()
            for p in cp:
                print(p)
            tp=TechnicianProblems.objects.filter(order_id=order['id']).values()
            cpPic=CustomerProblemPic.objects.filter(order_id=order['id']).values()
            tpPic=TechnicianProblemPic.objects.filter(order_id=order['id']).values()
            order['customerProblem']=cp
            order['customerProblemPic'] = cpPic
            order['technicianProblem']=tp
            order['technicianProblemPic']=tpPic
            all.append(order)
        return Response(all)


# class SendOrderToTechnician(APIView):
#     permission_classes = (AllowAny,)
#
#     def post(self, request, *args, **kwargs):
#         techid=self.request.data.get('techID')
#         orderid=self.request.data.get('orderID')
#         order=Order.objects.filter(id=orderid).values()
#         data={}
#         data['users']=techid
#         data['title']='سفارش جدید'
#         data['content'] = 'اطلاعات کلی'
#         data['push'] = True
#         data['data']=order
#         r = requests.post('http://localhost:8000/baseinfo/sendFCM/', data=data)
#         return Response(r)

class SendOrderToTechnician(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        techid=self.request.data.get('techID')
        orderid=self.request.data.get('orderID')
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
        print(fcmToken)
        data={"subtitle":"Elementary School",
              # "to":"e03zZk0kTXSUfgR1dhrmBE:APA91bEVwh3m1gucEphY-KYfiq7wyyXpkWJ4cd4S8KLhGGBLAGwHh-0j2u8ZIanKjhZtu1F6ilL3hba14EAg5k4ZhW1-L_wKuCO8W5gtg737bBtY_ILBH8lYRplF9E_svd2jNL-2i4nd",
              # "to":"dhKDbw2NXkEWtQnU90clep:APA91bFHPx31u4RS4zicr_ktT1rQGdcjIEyDNko9rLsKhwrrq7sMRPQAnzWJCS8X3swV59H7TSKyPvZ2apJvvjsYCruQheYag2NRNzpsbHpxWl_9Kb67cYX4TpWqj0beFvlcgqBIeb_U",
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
                  "amount" : "از 250,000 تا 500,000 تومان",
                  "appliance":str(order[0]['applianceBrand__a_barndCategory__a_categoryName']),
                  "appliancePic":str(order[0]['applianceBrand__a_barndCategory__a_categoryImage']),
                  "brand":str(order[0]['applianceBrand__a_brandName']),
                  "brandPic":str(order[0]['applianceBrand__a_brandImage']),
                  "model":str(order[0]['applianceModel__applianceModel']),
                  "date":str(orderDate),
                  "timerange":str(order[0]['orderTimeRange__timeRange']),
                  "address":str(order[0]['orderAddress__city__cityName'])+", "+str(order[0]['orderAddress__region__regionName'])+", ...",
                  "problems":["مشکل 1","مشکل2"],
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