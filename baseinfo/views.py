from django.shortcuts import render
from .models import HireJson,Cities,Regions,Provinces,Neighbourhoods,Appliances,ApplianceCategories,\
    ApllianceCategoryProblems,BarndsProblems,Problems,Counties,ApplianceBrands
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .Serializers import RegionsSerializer,ProvincesSerializer,NabourHoodsSerializer,AppliancesSerializer,ApplianceCategoriesSerializer
import json
# Create your views here.
class CreateDesignJson (APIView):
    permission_classes = (AllowAny,)
    def post(self, request, *args, **kwargs):
        modelname=self.request.data.get('modelName')
        modeltitle=self.request.data.get('modelTitle')
        fieldsjson = self.request.data.get('fieldsJson')
        print(modelname)
        obj = HireJson(modelName=modelname, modelTitle=modeltitle, fieldsJson=fieldsjson)
        obj.save()
        return Response({'message':'ok'})

class GetAllDesignJson (APIView):
    permission_classes = (AllowAny,)
    def get(self,request):
        obj = HireJson.objects.all().values()
        return Response(obj)

class GetRegins(APIView):
    permission_classes = (IsAuthenticated,)
    def get (self,request):
        province=Provinces.objects.all()
        res=ProvincesSerializer(province,many=True)
        return Response(res.data)

class getNabours(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        n = Neighbourhoods.objects.all()
        nn=NabourHoodsSerializer(n,many=True)
        return Response(nn.data)

class getApplience(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        n = ApplianceCategories.objects.all()
        nn = ApplianceCategoriesSerializer(n,many=True)
        return Response(nn.data)

class getProblems(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        categoryID=self.request.data.get('categoryID')
        barndID = self.request.data.get('brandID')
        modelID = self.request.data.get('modelID')
        if categoryID=="":
            categoryID="-1"
        if barndID == "":
            barndID="-1"
        if modelID == "":
            modelID="-1"
        catPromble = ApllianceCategoryProblems.objects.filter(appliancescategory_id=categoryID).values('id','problemTitle',
                                                                                                       'problemDescription',
                                                                                                       'problemKind',
                                                                                                       'lowPrice',
                                                                                                       'highPrice')
        brandPromble = BarndsProblems.objects.filter( appliancesBrands_id=barndID).values('id','problemTitle',
                                                                                                       'problemDescription',
                                                                                                       'problemKind',
                                                                                                       'lowPrice',
                                                                                                        'highPrice')
        ModelPromble = Problems.objects.filter(appliances_id=modelID).values('id','problemTitle',
                                                                                                       'problemDescription',
                                                                                                       'problemKind',
                                                                                                       'lowPrice',
                                                                                                       'highPrice')
        qs = catPromble.union(brandPromble, ModelPromble)
        return Response(qs)


class CreateApplianceCategoryProblem(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        appliancescategory = self.request.data.get('appliance')
        problemTitle = self.request.data.get('title')
        problemDescription =self.request.data.get('description')
        problemKind = self.request.data.get('kind')
        lowPrice = self.request.data.get('lowprice')
        highPrice =self.request.data.get('highprice')
        p = ApllianceCategoryProblems(appliancescategory_id=appliancescategory,problemTitle=problemTitle,
                                problemDescription=problemDescription,problemKind=problemKind,
                                lowPrice=lowPrice,highPrice=highPrice)
        p.save()
        return Response({'appliancecategoryproblem':'created','ID' : p.id})

class EditApplianceCategoryProblem(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        appId=self.request.data.get('id')
        problemTitle = self.request.data.get('title')
        problemDescription =self.request.data.get('description')
        problemKind = self.request.data.get('kind')
        lowPrice = self.request.data.get('lowprice')
        highPrice =self.request.data.get('highprice')
        co = ApllianceCategoryProblems.objects.filter(id=appId).update(problemTitle=problemTitle,
                                problemDescription=problemDescription,problemKind=problemKind,
                                lowPrice=lowPrice,highPrice=highPrice)
        return Response({'appliancecategoryproblem': 'edited'})


class DeleteApplianceCategoryProblem(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        pId=self.request.data.get('id')
        print(pId)
        co = ApllianceCategoryProblems.objects.filter(id=pId).delete()
        return Response({'appliancecategoryproblem': 'deleted'})


class CreateProvince(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request,*args, **kwargs):
        pname = self.request.data.get('provincename')
        p=Provinces(provinceName=pname)
        p.save()
        return Response({'province':'created'})

class CreateCounty(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request,*args, **kwargs):
        coname = self.request.data.get('countyname')
        pid=self.request.data.get('provinceid')
        co=Counties(countyName=coname,province_id=pid)
        co.save()
        return Response({'county':'created'})


class CreateCity(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request,*args, **kwargs):
        cname = self.request.data.get('cityname')
        coid=self.request.data.get('countyid')
        co=Cities(cityName=cname,county_id=coid)
        co.save()
        return Response({'city':'created'})

class CreateRegion(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request,*args, **kwargs):
        rname = self.request.data.get('regionname')
        cid=self.request.data.get('cityid')
        co=Regions(regionName=rname,city_id=cid)
        co.save()
        return Response({'region':'created'})

class CreateNeighbourhood(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request,*args, **kwargs):
        nname = self.request.data.get('neighbourhoodname')
        rid=self.request.data.get('regionid')
        co=Neighbourhoods(neighbourhoodName=nname,region_id=rid)
        co.save()
        return Response({'neighbourhood':'created'})


class EditProvince(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        pname = self.request.data.get('pname')
        pid = self.request.data.get('pid')
        co = Provinces.objects.filter(id=pid).update(provinceName=pname)

        return Response({'province': 'update'})


class EditCounty(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        coname = self.request.data.get('coname')
        coid = self.request.data.get('coid')
        co = Counties.objects.filter(id=coid).update(countyName=coname)

        return Response({'county': 'update'})

class EditCity(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        cname = self.request.data.get('cname')
        cid = self.request.data.get('cid')
        co = Cities.objects.filter(id=cid).update(cityName=cname)

        return Response({'city': 'update'})

class EditRegion(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        rname = self.request.data.get('rname')
        rid = self.request.data.get('rid')
        co = Regions.objects.filter(id=rid).update(regionName=rname)

        return Response({'region': 'update'})

class EditNeighbourhood(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        nname = self.request.data.get('nname')
        nid = self.request.data.get('nid')
        co = Neighbourhoods.objects.filter(id=nid).update(neighbourhoodName=nname)

        return Response({'neighbourhood': 'update'})


class DeleteProvince(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        pid = self.request.data.get('pid')
        co = Provinces.objects.filter(id=pid).delete()
        return Response({'province': 'delete'})


class DeleteCounty(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        coid = self.request.data.get('coid')
        co = Counties.objects.filter(id=coid).delete()

        return Response({'county': 'delete'})

class DeleteCity(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        cid = self.request.data.get('cid')
        co = Cities.objects.filter(id=cid).delete()

        return Response({'city': 'delete'})

class DeleteRegion(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        rid = self.request.data.get('rid')
        co = Regions.objects.filter(id=rid).delete()

        return Response({'region': 'delete'})

class DeleteNeighbourhood(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        nid = self.request.data.get('nid')
        co = Neighbourhoods.objects.filter(id=nid).delete()

        return Response({'neighbourhood': 'delete'})

class CreateAppliance(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request,*args, **kwargs):
        aname = self.request.data.get('appliancename')
        p=ApplianceCategories(a_categoryName=aname)
        p.save()
        return Response({'appliance':'created'})

class CreateBrand(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request,*args, **kwargs):
        bname = self.request.data.get('bname')
        bid=self.request.data.get('bid')
        co=ApplianceBrands(a_brandName=bname,a_barndCategory_id=bid)
        co.save()
        return Response({'brand':'created'})


class CreateModel(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request,*args, **kwargs):
        mname = self.request.data.get('mname')
        mid=self.request.data.get('mid')
        co=Appliances(applianceModel=mname,applianceBrand_id=mid)
        co.save()
        return Response({'model':'created'})


class EditAppliance(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        aname = self.request.data.get('aname')
        aid = self.request.data.get('aid')
        co = ApplianceCategories.objects.filter(id=aid).update(a_categoryName=aname)

        return Response({'appliance': 'update'})


class EditBrand(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        bname = self.request.data.get('bname')
        bid = self.request.data.get('bid')
        co = ApplianceBrands.objects.filter(id=bid).update(a_brandName=bname)

        return Response({'brand': 'update'})

class EditModel(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        mname = self.request.data.get('mname')
        mid = self.request.data.get('mid')
        co = Appliances.objects.filter(id=mid).update(applianceModel=mname)

        return Response({'model': 'update'})

class DeleteAppliance(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        aid = self.request.data.get('aid')
        co = ApplianceCategories.objects.filter(id=aid).delete()
        return Response({'appliance': 'delete'})


class DeleteBrand(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        bid = self.request.data.get('bid')
        co = ApplianceBrands.objects.filter(id=bid).delete()

        return Response({'brand': 'delete'})

class DeleteModel(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        mid = self.request.data.get('mid')
        co = Appliances.objects.filter(id=mid).delete()

        return Response({'model': 'delete'})
