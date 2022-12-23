from django.shortcuts import render
from django.db.models import Sum,Count,Avg,Q,Max,Min,F,Case,Case,  Value, When
from rest_framework.views import APIView
from .models import *
from .serializers import *
from personal.models import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from datetime import datetime
import json
from django.core.serializers.json import DjangoJSONEncoder
from fcm_django.models import FCMDevice
import requests
# Create your views here.
class GetUserChatStatus(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        uid = self.request.data.get('uid')
        users=PersonAuth.objects.filter(user_id__in=uid).values('user_id','person__id','person__firstName','person__lastName',
                                                                 'person__picture','category__name')
        res=[]
        for user in users:
            act=UserChatStatus.objects.filter(user_id=user['user_id']).values('active')
            print(act)
            if act.exists():
                if act[0]['active']:
                    status='online'
                else:
                    status = 'offline'
                res.append({'user_id':user['user_id'],
                        'person_id':user['user_id'],
                        'firstName':user['person__firstName'],
                        'lastName':user['person__lastName'],
                        'pic':user['person__picture'],
                        'category':user['category__name'],
                        'status':status})
            else:
                print("not excist")
                res.append({'user_id': user['user_id'],
                            'person_id': user['user_id'],
                            'firstName': user['person__firstName'],
                            'lastName': user['person__lastName'],
                            'pic': user['person__picture'],
                            'category': user['category__name'],
                            'status': 'offline'})

        return Response(res)

class GetUserMessages(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        uid = self.request.user
        rid = self.request.data.get('rid')
        r = ChatMessages.objects.filter(Q(receiver=uid.id)).update(read=True)
        messages=ChatMessages.objects.filter((Q(sender=uid) | Q(sender_id=rid)) & (Q(receiver=uid.id) |Q(receiver=rid))).order_by('messageDateTime').values()
        return Response(messages)

class SendMessages(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        sender=self.request.user
        receiverid = self.request.data.get('receiverid')
        messageText = self.request.data.get('messageText')
        msg=ChatMessages(
            sender=sender,
            receiver=receiverid,
            messageText=messageText,
            messageDateTime=datetime.now(),
            read=False
        )
        msg.save()
        return Response({'result':msg.id})

class SetActiveUser(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        uid = self.request.user
        try:
            act = UserChatStatus.objects.get(user_id=uid.id)
            act.active=True
            act.save()
        except:
            act=UserChatStatus(user=uid,active=True)
            act.save()
        return Response({'result':'activated'})

class SetDeactiveUser(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        uid = self.request.user
        try:
            act = UserChatStatus.objects.get(user_id=uid.id)
            act.active = False
            act.save()
        except:
            act = UserChatStatus(user=uid, active=False)
            act.save()
        return Response({'result':'deactivated'})

class ConnectedUsers(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        uid = self.request.user
        messages = ChatMessages.objects.filter((Q(sender=uid) | Q(receiver=uid.id)) ).values('sender_id','receiver','read').annotate(Max('sender_id'),Max('receiver'),Count('read'))
        return Response(messages)

class GetDateTimeNow(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(datetime.now())

class Createticket(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        createBy = self.request.user
        createDateTime=datetime.now()
        orderid=self.request.data.get('orderID')
        ticketStatus = TicketStatus.objects.get(id=self.request.data.get('statusID'))
        ticketPriority=TicketPriority.objects.get(id=self.request.data.get('priorityID'))
        ticketno=Tickets.objects.aggregate(Max('ticketNo'))
        subject=TicketSubjects.objects.get(id=self.request.data.get('subjectID'))
        if ticketno['ticketNo__max'] is None:
            ticketno=10000
        else:
            print (int(ticketno['ticketNo__max']))
            ticketno =int(ticketno['ticketNo__max']) + 1
        ticket=Tickets(
            ticketNo=ticketno,
            createBy = createBy,
            createDateTime =createDateTime,
            ticketStatus = ticketStatus,
            ticketPriority =ticketPriority,
            subject=subject,
            order_id=orderid
        )
        ticket.save()

        return Response({"result":ticket.id})

class CreateticketChat(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        ticketno = self.request.data.get('ticketno')
        sender = self.request.user
        answerTo = self.request.data.get('answerto')
        comment = self.request.data.get('comment')
        if answerTo is not "":
            ticketchat = TicketChats(
                ticketNo_id=ticketno,
                sender = sender,
                answerTo_id = answerTo,
                comment = comment,
                chatDateTime =datetime.now()
                )
        else:
            ticketchat = TicketChats(
                ticketNo_id=ticketno,
                sender=sender,
                comment=comment,
                chatDateTime=datetime.now()
            )
        ticketchat.save()
        return Response({"result": ticketchat.id})

class GetTicketAllStatusPrioritySubject(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        res=[]
        status=TicketStatus.objects.all().values()
        res.append({'status':status})
        priority = TicketPriority.objects.all().values()
        res.append({'priority':priority})
        subject = TicketSubjects.objects.all().values()
        res.append({'subject': subject})
        return Response(res)

class UploadTicketFile(APIView):
    permission_classes = (IsAuthenticated,)
    parser_class = (TicketFiles,)

    def post(self, request, *args, **kwargs):
        print(request.data)
        file_serializer = TicketFiles(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            print('salam')
            return Response({'response': 'upload file to ticket success'})
        else:
            print('bye')
            return Response({'response': 'upload file to ticket fialed'})

class GetAllTicketsChat(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        tc=TicketChats.objects.all().values("id",
                        ticket=F("ticketNo_id__ticketNo"),
                        sender_firstname=F("sender_id__first_name"),
                        sender_lastname=F("sender_id__last_name"),
                        answerToChat=F("answerTo_id"),
                        comment_text=F("comment"),
                        chatDate=F("chatDateTime"))

        return Response(tc)

class GetAllUserTicketsChat(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        tc=TicketChats.objects.filter(ticketNo_id__createBy=self.request.user.id).values("id",
                        ticket=F("ticketNo_id__ticketNo"),
                        sender_firstname=F("sender_id__first_name"),
                        sender_lastname=F("sender_id__last_name"),
                        answerToChat=F("answerTo_id"),
                        comment_text=F("comment"),
                        chatDate=F("chatDateTime"))

        return Response(tc)

class GetTicketDetails(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        ticketno=self.request.data.get('ticketNo')
        ticket=Tickets.objects.filter(ticketNo=ticketno)
        tickets=TicketsSerializer(ticket,many=True)
        tc = TicketChats.objects.filter(ticketNo_id__ticketNo=ticketno).values("id",
                                                                                           ticket=F(
                                                                                               "ticketNo_id__ticketNo"),
                                                                                           sender_firstname=F(
                                                                                               "sender_id__first_name"),
                                                                                           sender_lastname=F(
                                                                                               "sender_id__last_name"),
                                                                                           answerToChat=F(
                                                                                               "answerTo_id"),
                                                                                           comment_text=F("comment"),
                                                                                           chatDate=F("chatDateTime"))
        encoder = DjangoJSONEncoder()
        tcj = encoder.encode(tickets.data)
        ticketj = json.loads(tcj)
        ticketj[0]['chats']=tc
        return Response(ticketj)


class CreateTechnicianSurvey(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        uid=self.request.data.get('userID')
        orderid=self.request.data.get('orderID')
        orderRating =self.request.data.get('orderRank')
        survayDate = datetime.now()
        positivePoints = self.request.data.get('positive')
        NegativePoints =self.request.data.get('negative')
        comment = self.request.data.get('comment')
        ts=TechnicianSurvey(
            userID_id=uid,
            orderId =orderid,
            orderRating=orderRating,
            survayDate = survayDate,
            comment=comment
        )
        ts.save()
        for p in NegativePoints:
            cnp=TechnicianNegativePoints.objects.get(id=p)
            ts.technicianNegativePoints.add(cnp)
        for p in positivePoints:
            if p is not '':
                cpp = TechnicianPositivePoints.objects.get(id=p)
                ts.technicianPositivePoints.add(cpp)
        rankavg = TechnicianSurvey.objects.filter(userID_id=uid).aggregate(Avg('orderRating'))
        # print(rankavg)
        pid = PersonAuth.objects.filter(user_id=uid).values('person_id')
        # print(pid)
        tech = Technician.objects.get(id__in=pid)
        tech.technicianRank = rankavg['orderRating__avg']
        tech.save()

        return Response({'result':'Survey for Technician was Created'})


class CreateCustomerSurvey(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        uid=self.request.data.get('userID')
        orderid =self.request.data.get('orderID')
        orderRank = self.request.data.get('orderRank')
        surveyDate = datetime.now()
        positivePoints = self.request.data.getlist('positive')
        NegativePoints =self.request.data.getlist('negative')
        comment = self.request.data.get('comment')
        cs=CustomerSurvey(
            userID_id=uid,
            orderId_id =orderid,
            orderRating=orderRank,
            surveyDate = surveyDate,
            comment=comment
        )
        cs.save()
        for p in NegativePoints:
            cnp=CustomerNegativePoints.objects.get(id=p)
            cs.customerNegativePoints.add(cnp)
        for p in positivePoints:
            if p is not '':
                cpp = CustomerPositivePoints.objects.get(id=p)
                cs.customerPositivePoints.add(cpp)

        rankavg=CustomerSurvey.objects.filter(userID_id=uid).aggregate(Avg('orderRating'))
        # print(rankavg)
        pid=PersonAuth.objects.filter(user_id=uid).values('person_id')
        # print(pid)
        customer=Customers.objects.get(id__in=pid)
        customer.customerRank=rankavg['orderRating__avg']
        customer.save()
        return Response({'result':'Survey for Customer was Created'})

class GetCustomerSurveyPoints(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        res = []
        positive = CustomerPositivePoints.objects.all().values()
        res.append({'positive_points': positive})
        negative = CustomerNegativePoints.objects.all().values()
        res.append({'negative_points': negative})
        return Response(res)

class GetTechnicianSurveyPoints(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        res = []
        positive = TechnicianPositivePoints.objects.all().values()
        res.append({'positive_points': positive})
        negative = TechnicianNegativePoints.objects.all().values()
        res.append({'negative_points': negative})
        return Response(res)

class SendTicketNotification(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        senderID = self.request.data.get('senderID')
        reciverID = self.request.data.get('reciverID')
        message = self.request.data.get('message')
        ticketNo=self.request.data.get('ticketNo')
        r = SendTicketToUser(senderID, reciverID,ticketNo, message)
        return Response(r)

def SendTicketToUser(senderid,reciverid,ticketNo, message):
    uid=PersonAuth.objects.filter(user_id=senderid).values('person_id','person__firstName','person__lastName','person__picture')
    fcmToken = FCMDevice.objects.filter(user_id=reciverid).values('registration_id')
    data = {"subtitle": "Elementary School",
            "to": fcmToken[0]['registration_id'],
            "notification": {
                "body": "Message",
                "OrganizationId": "2",
                "content_available": "true",
                "subtitle": "تیکت",
                "title": "تیکت جدید",
                "priorty": "high",
                "click_action": "ir.mersaGroup.inanloService.expert.NewOrderActivity"},
            "data": {
                "ticket_No":ticketNo,
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
