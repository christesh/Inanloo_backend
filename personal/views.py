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
from baseinfo.models import OTPsms,MembersPermission
from .models import *
from .serializres import *
from baseinfo.Serializers import MembersGroupSerializer,MembersPermissionSSerializer
from django.db.models import Q
from rest_framework.authtoken.models import Token

# Create your views here.
class JustSms(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        mob = self.request.data.get('mobile')
        pin = ''.join(random.choice('0123456789') for _ in range(4))
        print(pin)
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
            print(pin)
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

class changepass(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request,*args, **kwargs):
        uid = self.request.data.get('uid')
        passw = self.request.data.get('pass')
        u = User.objects.get(username=uid)
        u.set_password(passw)
        u.save()
        return Response({"result":"password change"})

class ForgetSendSms(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        mob = self.request.data.get('mobile')
        user=self.request.data.get('uid')
        per = User.objects.filter(Q(username=user),Q()).values()
        # return Response(per)
        if (per.exists()):
            pin = ''.join(random.choice('0123456789') for _ in range(4))
            print(pin)
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
        us=User.objects.filter(username=mob).values()
        sm = OTPsms.objects.filter(Q(userId=mob), Q(verifyCode=smscode)).values()
        if (sm.exists()):
            if (us.exists()):
                user = User.objects.get(username=mob)
                token,create = Token.objects.get_or_create(user=user)
                print(token)
                return Response({"result": str(token)})
            else:
                return Response({"result": "success"})
        else:
            return Response({"result": "code does not match"})


class GetPersonCategories(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        p = Group.objects.all().values('id','name')
        return Response(p)


class RegisterPerson(APIView):
    permission_classes = (AllowAny,)
    print('r1')
    def post(self, request, *args, **kwargs):
        user = self.request.data.get('username')
        pass1 = user
        ln = self.request.data.get('lname')
        fn = self.request.data.get('fname')
        usercategory=self.request.data.get('usercategory')
        catName=Group.objects.filter(id=usercategory).values('name')
        nid=self.request.data.get('nationalid')
        p = User.objects.filter(username=user)
        print('r2')
        print(p)
        if (p.exists()):
            print('pexist')
            return Response({"key": "username exists"})
        else:
            data1 = {'username': user, 'password1': pass1, 'password2': pass1}
            print(data1)
            r = requests.post('http://localhost:8000/api/v1/rest-auth/registration/', data=data1)
            rt = r.text.strip()
            d = json.loads(rt)
            print("salam1")
            if (r.status_code == 201):
                authid = User.objects.filter(username=user).values('id')
                userupdate = User.objects.filter(username=user).update(last_name=ln, first_name=fn, mobile=user)
                if(catName[0]['name']=='مشتری'):
                    personcreate = Customers(nationalId=nid, firstName=fn, lastName=ln,authuser_id=authid,
                                         createdBy_id=authid, createdAt= timezone.now())
                    personcreate.save()
                else:
                    personcreate = Technician(nationalId=nid, firstName=fn, lastName=ln, authuser_id=authid,
                                              createdBy_id=authid, createdAt=timezone.now())
                    personcreate.save()
                personauthcreate = PersonAuth.objects.create(person=personcreate,user_id=authid, category_id=usercategory, active=True, fillProfile=False)
                mobilecreate= Mobiles.objects.create(person=personcreate,mobileNumber=user,isMain=True)
                d={'key':'one user was created'}
            return Response(d)

# class FillTechnicianProfile(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def post(self, request, *args, **kwargs):
#         technicianProfile=self.request.data.get('profilejson')


class RegisterCompanyMembers(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = self.request.data.get('username')
        pass1 = self.request.data.get('password')
        ln = self.request.data.get('lname')
        fn = self.request.data.get('fname')
        usercategory = self.request.data.get('usercategory')
        nid = self.request.data.get('nationalid')
        mobile = self.request.data.get('mobile')
        group=self.request.data.get('group')
        p = User.objects.filter(username=user)
        print(group)
        print(usercategory)
        creator=self.request.user.id
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
                personcreate = CompanyMembers(nationalId=nid, firstName=fn, lastName=ln, authuser_id=authid,
                                         createdBy_id=creator, createdAt=timezone.now(),membersGroup_id=group)
                personcreate.save()
                personauthcreate = PersonAuth.objects.create(person_id=personcreate.id, user_id=authid,
                                                             category_id=usercategory, active=True, fillProfile=False)
                mobilecreate = Mobiles.objects.create(person_id=personcreate.id, mobileNumber=mobile, isMain=True)
                d = {'key': 'one user was created'}
            return Response(d)


class EditCompanyMembers(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        userid=self.request.data.get('userid')
        ln = self.request.data.get('lname')
        fn = self.request.data.get('fname')
        nid = self.request.data.get('nationalid')
        mobile = self.request.data.get('mobile')
        group=self.request.data.get('group')
        personcreate = CompanyMembers.objects.filter(id=userid).update(nationalId=nid, firstName=fn, lastName=ln, membersGroup_id=group)

        mobilecreate = Mobiles.objects.filter(person_id=userid).update(mobileNumber=mobile)
        return Response({'update':'successfully'})

class GetAllMemberGroup(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        p =MembersGroup.objects.all()
        s=MembersGroupSerializer(p,many=True)
        return Response(s.data)


class GetAllPermissions(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        p =MembersPermission.objects.all().values()
        s=MembersPermissionSSerializer(p)
        return Response(p)

class GetAllPersonDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        p = Person.objects.all()
        serializer = PersonSerializer(p, many=True)
        return Response(serializer.data)


class GetAllCustomersDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        p = Customers.objects.all()
        serializer = CustomerSerializer(p, many=True)
        return Response(serializer.data)


class GetAllTechniciansDetails(APIView):
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)
    def get(self, request):
        p = Technician.objects.all()
        serializer = TechnicianSerializer(p, many=True)
        return Response(serializer.data)


class GetCustomersDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        id = self.request.data.get('userID')
        p = Customers.objects.filter(id=id)
        serializer = CustomerSerializer(p, many=True)
        return Response(serializer.data)

class GetTechniciansDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        id = self.request.data.get('userID')
        p = Technician.objects.filter(id=id)
        serializer = TechnicianSerializer(p, many=True)
        return Response(serializer.data)


class GetPersonAuth(APIView):
    # serializer_class = PersonSerializer
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        person_auth = PersonAuth.objects.filter(user__id=self.request.user.id).values('person','category','category__name','active','fillProfile')
        return Response(person_auth)

class GetAllCompanyMembers(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        companymember = CompanyMembers.objects.all()
        serializer = CompanyMemberSerializer(companymember, many=True)
        return Response(serializer.data)

class GetPersonDetails(APIView):
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)
    def get(self, request):
        # id = self.request.data.get('userID')
        # cid=PersonAuth.objects.filter(user_id=self.request.user.id).values('person_id')
        p = CompanyMembers.objects.filter(authuser_id=self.request.user.id)
        serializer = CompanyMemberSerializer(p, many=True)
        return Response(serializer.data)

class DeleteCompanyMember(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        id = self.request.data.get('userID')
        p = CompanyMembers.objects.filter(id=id).delete()
        # return Response({'delete': 'successful'})
        return Response({'delete':'successful'})


class EditMemberGroup(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        groupName = self.request.data.get('groupname')
        geroupid=self.request.data.get('groupid')
        pers = self.request.data.get('permissions')
        p=MembersGroup.objects.filter(id=geroupid)
        print (p[0])
        p[0].permissions.clear()
        for per in pers:
            pp=MembersPermission.objects.filter(id=per)
            p[0].permissions.add(pp[0])
        s=MembersGroup.objects.filter(id=geroupid).update(group=groupName)
        return Response({'update': 'successful'})


class CreateMemberGroup(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        groupName = self.request.data.get('groupname')
        permissions=self.request.data.get('permissions')
        p=MembersGroup(group=groupName)

        p.save()
        for per in permissions:
            p.permissions.add(per)
        return Response({'create': 'successful'})


class DeleteMembersGroup(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        id = self.request.data.get('userID')
        p = MembersGroup.objects.filter(id=id).delete()
        # return Response({'delete': 'successful'})
        return Response({'delete': 'successful'})


class GetUserAddress(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request, *args, **kwargs):
        userid=self.request.data.get('id')
        userAddress=Addresses.object.filter(person_id=userid).values('province_id','province__provinceName',
                                                                     'county_id' ,'county__countyName',
                                                                     'city_id', 'city__cityName',
                                                                     'region_id','region_regionName',
                                                                     'neighbourhood_id','neighbourhood_neighbourhoodName',
                                                                     'addressLat','addressLong',
                                                                     'addressStreet','addressLane','addressNo',
                                                                     'addressUnit','addressFloor','isMain')
        return Response(userAddress)


class CreateCustomerAddress(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        uid = self.request.data.get('uid')
        pid = self.request.data.get('pid')
        coid = self.request.data.get('coid')
        cid = self.request.data.get('cid')
        rid = self.request.data.get('rid')
        nid = self.request.data.get('nid')
        mainstreet = self.request.data.get('mainstreet')
        substreet = self.request.data.get('substreet')
        lane = self.request.data.get('lane')
        building = self.request.data.get('building')
        no = self.request.data.get('no')
        unit = self.request.data.get('unit')
        floor = self.request.data.get('floor')
        lat = self.request.data.get('lat')
        long = self.request.data.get('long')
        isMain =self.request.data.get('isMain')
        address=Addresses(person_id=uid,province_id=pid,county_id=coid,
                          city_id=cid,region_id=rid,neighbourhood_id=nid,
                          addressLat=lat,addressLong=long,addressStreet=mainstreet,
                          addressSubStreet=substreet,addressLane=lane,
                          addressBuilding=building,addressNo=no,addressUnit=unit,
                          addressFloor=floor,isMain=isMain)
        address.save()
        if(isMain):
            a=Addresses.objects.filter(~Q(id=address.id)).update(isMain=False)
        return  Response({'New Address created for userid':uid,'Address ID': address.id})


class EditCustomerAddress(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        addid = self.request.data.get('addid')
        uid = self.request.data.get('uid')
        pid = self.request.data.get('pid')
        coid = self.request.data.get('coid')
        cid = self.request.data.get('cid')
        rid = self.request.data.get('rid')
        nid = self.request.data.get('nid')
        mainstreet = self.request.data.get('mainstreet')
        substreet = self.request.data.get('substreet')
        lane = self.request.data.get('lane')
        building = self.request.data.get('building')
        no = self.request.data.get('no')
        unit = self.request.data.get('unit')
        floor = self.request.data.get('floor')
        lat = self.request.data.get('lat')
        long = self.request.data.get('long')
        isMain =self.request.data.get('isMain')
        print(addid)
        address=Addresses.objects.filter(id=addid).update(province_id=pid,county_id=coid,
                          city_id=cid,region_id=rid,neighbourhood_id=nid,
                          addressLat=lat,addressLong=long,addressStreet=mainstreet,
                          addressSubStreet=substreet,addressLane=lane,
                          addressBuilding=building,addressNo=no,addressUnit=unit,
                          addressFloor=floor,isMain=isMain)

        return  Response({'New Address created for userid':uid,'Address ID': addid})

class DeleteCustomerAddress(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request, *args, **kwargs):
        id = self.request.data.get('addid')
        print(id)
        da=Addresses.objects.filter(id=id).delete()
        return Response({'Address deleted ID': id})


class TechnicianUploadPic(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            user = Technician.objects.get(id=self.request.data.get('id'))
            profilePic = request.FILES["profilePic"]
            print(profilePic)
            user.picture = profilePic
            user.save()
            return Response({'response':'upload pics success'})
        except:
            return Response({'response': 'upload pics failed'})

class CustomerUploadPic(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            user = Customers.objects.get(id=self.request.data.get('id'))
            profilePic = request.FILES["profilePic"]
            print(profilePic)
            user.picture = profilePic
            user.save()
            return Response({'response':'upload pics success'})
        except:
            return Response({'response': 'upload pics failed'})