from rest_framework import serializers
from .models import Supplier,Customers, CompanyMembers, \
    Addresses, Technician, Person,Mobiles,Phones,PersonAuth
from baseinfo.Serializers import MembersGroupSerializer, CustomerCategory,TechnicianCategory,ProvincesSerializerV2,\
    CountiesSerializerV2,CitiesSerializerV2,RegionsSerializerV2,NabourHoodsSerializer,ProvincesSerializer

class UserUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customers
        fields = ['id', 'picture']

class CustomerCategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = CustomerCategory
        fields = '__all__'


class CustomersSerializer (serializers.ModelSerializer):
    customerCategory = CustomerCategorySerializer()

    class Meta:
        model= Customers
        fields= '__all__'


class TechnicianCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicianCategory
        fields = '__all__'



class CompanyMembersSerializer (serializers.ModelSerializer):

    class Meta:
        model= CompanyMembers
        fields= '__all__'

class SupplierSerializer (serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class PhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = ['id','phoneNumber']


class MobilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobiles
        fields = '__all__'


class AddressesSerializer(serializers.ModelSerializer):
    province=ProvincesSerializer()
    class Meta:
        model = Addresses
        fields = ['id','province','addressStreet','addressLane','addressNo','addressUnit','addressFloor','isMain','addressLat','addressLong']

class AddressesSerializerV2(serializers.ModelSerializer):
    province = ProvincesSerializerV2()
    county=CountiesSerializerV2()
    city = CitiesSerializerV2()
    region = RegionsSerializerV2()
    neighbourhood = NabourHoodsSerializer()
    class Meta:
        model = Addresses
        fields = '__all__'
        # fields = ['id','province_id','province2']

class PersonSerializer(serializers.ModelSerializer):
    address=AddressesSerializerV2(many=True)
    mobile=MobilesSerializer(many=True)
    phones=PhonesSerializer(many=True)
    class Meta:
        model = Person
        fields = ['id', 'firstName', 'lastName', 'nationalId','phones','mobile','address']


class CustomerSerializer(serializers.ModelSerializer):
    # person=PersonSerializer(many=True)
    address = AddressesSerializerV2(many=True)
    mobile = MobilesSerializer(many=True)
    phones = PhonesSerializer(many=True)
    class Meta:
        model = Customers
        fields = ['id', 'firstName', 'lastName', 'nationalId','birthDate','picture','phones','mobile','address','picture','customerCategory',
                  'customerDevices']

class CompanyMemberSerializer(serializers.ModelSerializer):
    # person=PersonSerializer(many=True)
    address = AddressesSerializerV2(many=True)
    mobile = MobilesSerializer(many=True)
    phones = PhonesSerializer(many=True)
    membersGroup=MembersGroupSerializer()

    class Meta:
        model = CompanyMembers
        fields = ['id', 'firstName', 'lastName', 'nationalId','birthDate','phones','mobile','address','picture','membersGroup',
                  'hireDate','quitDate']

class TechnicianSerializer (serializers.ModelSerializer):
    address = AddressesSerializerV2(many=True)
    mobile = MobilesSerializer(many=True)
    phones = PhonesSerializer(many=True)

    class Meta:
        model = Technician
        fields = ['id', 'firstName', 'lastName', 'nationalId','picture', 'phones', 'mobile','technicianFavourite', 'address','birthDate', 'technicianCategory',
                  'technicianFavourite', 'technicianRank', 'activate','status', 'hireForm']


class PersonAuthSerializer(serializers.ModelSerializer):
    person = PersonSerializer()

    class Meta:
        model = PersonAuth
        fields = '__all__'