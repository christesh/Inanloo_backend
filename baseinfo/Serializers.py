from rest_framework import serializers

from .models import *

# from personal.serializres import SupplierSerializer
class ProblemsSerialzer (serializers.ModelSerializer):
    class Meta:
        model=Problems
        fields='__all__'

class ModelsChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model=ModelsChecklist
        fields='__all__'

class AppliancesSerializer(serializers.ModelSerializer):
    ID = serializers.CharField(source='id')
    model = serializers.CharField(source='applianceModel')
    description = serializers.CharField(source='applianceDescription')
    modelProblem=ProblemsSerialzer(many=True)
    modelChecklist = ModelsChecklistSerializer(many=True)
    class Meta:
        model = Appliances
        fields = ['ID','model','description','modelProblem','modelChecklist']

class BarndsProblemsSerializer(serializers.ModelSerializer):
    class Meta:
        model= BarndsProblems
        fields ='__all__'

class BrandsChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model=BrandsChecklist
        fields= '__all__'

class ApplianceBrandsSerializer(serializers.ModelSerializer):
    ID = serializers.CharField(source='id')
    brand = serializers.CharField(source='a_brandName')
    brandpic = serializers.CharField(source='a_brandImage')
    description = serializers.CharField(source='a_brandDescription')
    models = AppliancesSerializer(many=True)
    brandProblem=BarndsProblemsSerializer(many=True)
    brandChecklist=BrandsChecklistSerializer(many=True)
    class Meta:
        model = ApplianceBrands
        fields = ['ID','brand','brandpic','description','brandProblem','brandChecklist','models','a_barndCategory']

class ApllianceCategoryProblemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApllianceCategoryProblems
        fields = '__all__'

class ApplianceCategoryChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model=AppliancesCategoryCheckList
        fields='__all__'

class ApplianceCategoriesSerializer(serializers.ModelSerializer):
    ID = serializers.CharField(source='id')
    title = serializers.CharField(source='a_categoryName')
    pic = serializers.CharField(source='a_categoryImage')
    description = serializers.CharField(source='a_categoryDescription')
    brands = ApplianceBrandsSerializer(many=True)
    appCatProblem=ApllianceCategoryProblemsSerializer(many=True)
    appCatChecklist = ApplianceCategoryChecklistSerializer(many=True)
    class Meta:
        model = ApplianceCategories
        fields = ['ID','title','pic','description','appCatProblem','appCatChecklist','brands']

class AppliancesSupplierSerializer(serializers.ModelSerializer):
    # supplier=SupplierSerializer()
    appliance=AppliancesSerializer(many=True)
    class Meta:
        model = AppliancesSupplier
        fields = '__all__'


class MembersPermissionSSerializer(serializers.ModelSerializer):

    class Meta:
             model = MembersPermission
             fields = '__all__'


class MembersGroupSerializer(serializers.ModelSerializer):
    permissions=MembersPermissionSSerializer(many=True)
    class Meta:
        model = MembersGroup
        fields = '__all__'


class CustomerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCategory
        fields = '__all__'


class TechnicianCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicianCategory
        fields = '__all__'


class ProblemsSerializer (serializers.ModelSerializer):
    appliances=AppliancesSerializer()
    class Meta:
        model = Problems
        fields = '__all__'

class NabourHoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Neighbourhoods
        fields = ['id','neighbourhoodName','neighbourhoodDescription']

class RegionsSerializer (serializers.ModelSerializer):
    neighbourhoods = NabourHoodsSerializer(many=True)
    class Meta:
        model = Regions
        fields = ['id','regionName','neighbourhoods']


class CitiesSerializer (serializers.ModelSerializer):
    regions = RegionsSerializer(many=True)
    class Meta:
        model = Cities
        fields = ['id','cityName','regions']

class CountiesSerializer (serializers.ModelSerializer):
    cities=CitiesSerializer(many=True)
    class Meta:
        model = Counties
        fields =['id','countyName','cities']

class ProvincesSerializer (serializers.ModelSerializer):
    counties=CountiesSerializer(many=True)

    class Meta:
        model = Provinces
        fields = ['id','provinceName','counties']


class RegionsSerializerV2 (serializers.ModelSerializer):
    # neighbourhoods = NabourHoodsSerializer(many=True)
    class Meta:
        model = Regions
        fields = ['id','regionName']


class CitiesSerializerV2 (serializers.ModelSerializer):
    # regions = RegionsSerializer(many=True)
    class Meta:
        model = Cities
        fields = ['id','cityName']


class CountiesSerializerV2 (serializers.ModelSerializer):
    # cities=CitiesSerializer(many=True)
    class Meta:
        model = Counties
        fields =['id','countyName']


class ProvincesSerializerV2 (serializers.ModelSerializer):
    # counties=CountiesSerializer(many=True)
    class Meta:
        model = Provinces
        fields = ['id','provinceName']


class SmsTypesSerializer (serializers.ModelSerializer):
    class Meta:
        model = SmsTypes
        fields = '__all__'


class OTPsmsSerializer (serializers.ModelSerializer):
    class Meta:
        model = OTPsms
        fields = '__all__'


class SmsSerializer (serializers.ModelSerializer):
    smsType=SmsTypesSerializer()
    class Meta:
        model = Sms
        fields = '__all__'

class testSerializer(serializers.ModelSerializer):
    class Meta:
        model=testModel
        fields= "__all__"