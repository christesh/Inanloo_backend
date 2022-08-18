from django.shortcuts import render
from django.db.models import Sum,Count,Avg,Q,Max,Min,F,Case,Case,  Value, When
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User, Group
from django.utils import timezone
import http.client
import requests
import json
import random
from baseinfo.models import OTPsms
from .models import Person,PersonAuth

# Create your views here.
class JustSms(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        mob = self.request.data.get('mobile')
        pin = ''.join(random.choice('0123456789') for _ in range(4))
        sm = OTPsms.objects.filter(userId=mob).values()
        if (sm.exists()):
            d = OTPsms.objects.filter(userId=mob).delete()
        r = OTPsms.objects.create(userId=mob, verifyCode=pin)
        conn = http.client.HTTPConnection("api.ghasedaksms.com")
        payload = "type=1&param1=" + "کاربر" + "&param2=" + pin + "&receptor=" + mob + "&template=verifysms2"
        headers = {'apikey': "rPyTiM/H76cybtptI7DDsOp4rMCWgk2KL57WRCZeR3s",
                   'content-type': "application/x-www-form-urlencoded"
                   }
        conn.request("POST", "/v2/send/verify", payload.encode('utf-8'), headers)
        res = conn.getresponse()
        data = res.read()
        c1 = json.loads(data)
        return Response(c1)


class SendSms(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        mob = self.request.data.get('mobile')
        per = User.objects.filter(Q(username=mob)).values()
        # return Response(per)
        if (per.exists()):
            pin = ''.join(random.choice('0123456789') for _ in range(4))
            sm = OTPsms.objects.filter(userId=mob).values()
            if (sm.exists()):
                d = OTPsms.objects.filter(userId=mob).delete()
            r = OTPsms.objects.create(userId=mob, verifyCode=pin)
            conn = http.client.HTTPConnection("api.ghasedaksms.com")
            payload = "type=1&param1=" + "کاربر" + "&param2=" + pin + "&receptor=" + mob + "&template=verifysms2"
            headers = {'apikey': "rPyTiM/H76cybtptI7DDsOp4rMCWgk2KL57WRCZeR3s",
                       'content-type': "application/x-www-form-urlencoded"
                       }
            conn.request("POST", "/v2/send/verify", payload.encode('utf-8'), headers)
            res = conn.getresponse()
            data = res.read()
            c1 = json.loads(data)
            return Response(c1)
        else:
            return Response({"result": "mobile number not match"})


class CheckSms(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        smscode = self.request.data.get('code')
        mob = self.request.data.get('mobile')
        sm = OTPsms.objects.filter(Q(userId=mob), Q(verifyCode=smscode)).values()
        if (sm.exists()):
            return Response({"result": "success"})
        else:
            return Response({"result": "code does not match"})


class GetPersonCategories(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        p = Group.objects.all().values('id','name')
        return Response(p)


class Register(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        user = self.request.data.get('username')
        pass1 = user
        ln = self.request.data.get('lname')
        fn = self.request.data.get('fname')
        usercategory=self.request.data.get('usercategory')
        nid=self.request.data.get('nationalid')
        p = User.objects.filter(username=user).values()
        if (p.exists()):
            return Response({"key": "username exists"})
        else:
            data1 = {'username': user, 'password1': pass1, 'password2': pass1}
            r = requests.post('http://localhost:8000/api/v1/rest-auth/registration/', data=data1)
            rt = r.text.strip()
            d = json.loads(rt)
            if (r.status_code == 201):
                authid = User.objects.filter(username=user).values('id')
                userupdate = User.objects.filter(username=user).update(last_name=ln, first_name=fn)
                personcreate = Person(nationalId=nid, firstName=fn, lastName=ln,authuser_id=authid, createdBy_id=authid, createdAt= timezone.now())
                personcreate.save()
                personauthcreate = PersonAuth.objects.create(person=personcreate, category_id=usercategory, active=True, fillProfile=False)
                d={'key':'one user was created'}

            return Response(d)


class GetPerson(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        p = User.objects.filter(id=self.request.user.id).values('username')
        per = Person.objects.filter(mobile__in=p).values()
        return Response(per)

