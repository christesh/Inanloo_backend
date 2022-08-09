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
from baseinfo.models import sms
from .models import Person,PersonAuth

# Create your views here.

class justsms(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        mob = self.request.data.get('mobile')
        name = self.request.data.get('fname')
        print(mob, name)
        if name == "":
            p = Person.objects.filter(mobile=mob).values('f_name')
            name = p[0]['f_name']
        pin = ''.join(random.choice('0123456789') for _ in range(4))
        sm = sms.objects.filter(userid=mob).values()
        if (sm.exists()):
            d = sms.objects.filter(userid=mob).delete()
        r = sms.objects.create(userid=mob, vercode=pin)
        conn = http.client.HTTPConnection("api.ghasedaksms.com")
        payload = "type=1&param1=" + name + "&param2=" + pin + "&receptor=" + mob + "&template=verifysms2"
        headers = {'apikey': "rPyTiM/H76cybtptI7DDsOp4rMCWgk2KL57WRCZeR3s",
                   'content-type': "application/x-www-form-urlencoded"
                   }
        conn.request("POST", "/v2/send/verify", payload.encode('utf-8'), headers)
        res = conn.getresponse()
        data = res.read()
        c1 = json.loads(data)
        return Response(c1)

class sendsms(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        mob = self.request.data.get('mobile')
        per = User.objects.filter(Q(username=mob)).values()
        # return Response(per)
        if (per.exists()):
            pin = ''.join(random.choice('0123456789') for _ in range(4))
            sm = sms.objects.filter(userId=mob).values()
            if (sm.exists()):
                d = sms.objects.filter(userId=mob).delete()
            r = sms.objects.create(userId=mob, verifyCode=pin)
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

class checksms(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        smscode = self.request.data.get('code')
        mob = self.request.data.get('mobile')
        sm = sms.objects.filter(Q(userId=mob), Q(verifyCode=smscode)).values()
        if (sm.exists()):
            return Response({"result": "success"})
        else:
            return Response({"result": "code does not match"})

class GetPersonCategories(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        p = Group.objects.all().values('id','name')
        return Response(p)

class register(APIView):
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
                personcreate = Person.objects.create(nationalId=nid, firstName=fn, lastName=ln,authuser_id=authid,createdBy_id=authid, createdAt= timezone.now())
                personauthcreate = PersonAuth.objects.create(person_id=nid, category_id=usercategory, active=True,
                                                                 fillProfile=False)
                d={'key':'one user was created'}

            return Response(d)




class getperson(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        p = User.objects.filter(id=self.request.user.id).values('username')
        per = Person.objects.filter(mobile__in=p).values()
        return Response(per)

