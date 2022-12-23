from rest_framework import serializers
from .models import *
from baseinfo.Serializers import *
from personal.serializres import *
from warehouse.serialzres import *


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'


class OrderTimeRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTimeRange
        fields = '__all__'


class KindOfOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = KindOfOrder
        fields = '__all__'

class CustomerOrderProblemPic(serializers.ModelSerializer):
    class Meta:
        model=CustomerProblemPic
        fields='__all__'


class CustomerOrderApplianceGuarantee(serializers.ModelSerializer):
    class Meta:
        model=CustomerApplianceGuarantee
        fields='__all__'

class CustomerOrderApplianceInvoice(serializers.ModelSerializer):
    class Meta:
        model=CustomerApplianceInvoice
        fields='__all__'

class CustomerProblemPicSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomerProblemPic
        fields='__all__'

class CPSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomerProblems
        fields= '__all__'

class ApplianceCategorieSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model= ApplianceCategories
        fields= '__all__'


class OrderApplianceBrandSerializer(serializers.ModelSerializer):
    a_barndCategory=ApplianceCategorieSimpleSerializer(read_only=True)
    class Meta:
        model=ApplianceBrands
        fields="__all__"


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer( read_only=True)
    applianceBrand = OrderApplianceBrandSerializer(read_only=True)
    # device = DevicesSerializer(many=True,read_only=True)
    orderKind = KindOfOrderSerializer(read_only=True)
    orderTimeRange = OrderTimeRangeSerializer(read_only=True)
    # orderAddress = AddressesSerializer(read_only=True)
    orderStatus = OrderStatusSerializer(read_only=True)
    technician = TechnicianSerializer(read_only=True)
    orderAddress = AddressesSerializerV2( read_only=True)
    applianceModel=AppliancesSerializer(read_only=True)
    # customerProblems=CPSerializer(many=True)
    # registerBy=User(read_only=True)
    class Meta:
        model = Order
        # fields = ['customer','technician','orderStatus','applianceBrand','orderKind','orderTimeRange','orderAddress','orderAddress','customerProblems']
        fields= '__all__'




class OrderDetailsSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    soldIndividualDevice=SoldIndividualDeviceSerializer()

    class Meta:
        model = OrderDetails
        fields = '__all__'


class CustomerProblemsSerializer(serializers.ModelSerializer):
    order=OrderSerializer()
    problem = ProblemsSerializer()

    class Meta:
        model = CustomerProblems
        fields = '__all__'


class CustomerProblemPicSerializer(serializers.ModelSerializer):


    class Meta:
        model = CustomerProblemPic
        fields = '__all__'


class TechnicianProblemsSerializer(serializers.ModelSerializer):

    problem = ProblemsSerializer()

    class Meta:
        model = TechnicianProblems
        fields = '__all__'


class TechnicianProblemPicSerializer(serializers.ModelSerializer):


    class Meta:
        model = TechnicianProblemPic
        fields = '__all__'




