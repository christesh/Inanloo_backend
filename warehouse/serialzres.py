from rest_framework import serializers
from .models import SoldIndividualDevice,IndividualDevice
# from baseinfo.Serializers import DevicesSerializer
from personal.serializres import SupplierSerializer, TechnicianSerializer,CompanyMembersSerializer


class SoldIndividualDeviceSerializer(serializers.ModelSerializer):
    # device = DevicesSerializer()
    technician = TechnicianSerializer()
    seller = CompanyMembersSerializer()

    class Meta:
        model = SoldIndividualDevice
        fields = '__all__'


class IndividualDeviceSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer()
    # device = DevicesSerializer()

    class Meta:
        model = IndividualDevice
        fields = '__all__'


