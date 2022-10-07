from django.shortcuts import render
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class GetAllOrders (APIView):
    permission_classes = (AllowAny,)
    def get(self,request):
        snippets = Order.objects.all()
        serializer = OrderSerializer(snippets, many=True)
        return Response(serializer.data)