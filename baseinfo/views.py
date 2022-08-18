from django.shortcuts import render
from .models import HireJson
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
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
