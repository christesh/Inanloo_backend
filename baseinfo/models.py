from django.db import models

# Create your models here.


class MembersGroup(models.Model):
    group=models.CharField(max_length=40)
    description=models.TextField()

    def __str__ (self):
        return str(self.group)

    class Meta:
        verbose_name_plural = 'MembersGroup'


class CustomerCategory(models.Model):
    customerCategory=models.CharField(max_length=50)
    categoryDescription=models.TextField()

    def __str__(self):
        return str(self.customerCategory)

    class Meta:
        verbose_name_plural = 'CustomerCategory'


class TechnicianCategory(models.Model):
    technicianCategory=models.CharField(max_length=50)
    technicianDescription=models.TextField()

    def __str__(self):
        return str(self.technicianCategory)

    class Meta:
        verbose_name_plural = 'TechnicianCategory'


class TechnicianSkills(models.Model):
    skill=models.CharField(max_length=50)
    skillDescription=models.TextField()

    def __str__(self):
        return str(self.skill)

    class Meta:
        verbose_name_plural = 'TechnicianSkills'


class ApplianceCategories(models.Model):
    a_categoryName=models.CharField(max_length=50)
    a_categoryDescription=models.TextField()

    def __str__(self):
        return str(self.a_categoryName)

    class Meta:
        verbose_name_plural = 'DeviceCategories'


class ApplianceBrands(models.Model):
    a_barndCategory=models.ForeignKey(ApplianceCategories,on_delete=models.CASCADE)
    a_brandName=models.CharField(max_length=50)
    a_brandDescription=models.TextField()

    def __str__(self):
        return str(self.a_brandName)

    class Meta:
        verbose_name_plural = 'DeviceBrands'


class Appliances(models.Model):
    applianceBrand=models.ForeignKey(ApplianceBrands,on_delete=models.CASCADE)
    applianceModel=models.CharField(max_length=20)
    applianceDescription=models.TextField()
    applianceRate=models.FloatField()

    def __str__(self):
        return str(self.applianceBrand) + '-' + str(self.applianceModel)

    class Meta:
        verbose_name_plural = 'Devices'


class DeviceCategories(models.Model):
    d_categoryName=models.CharField(max_length=50)
    d_categoryDescription=models.TextField()

    def __str__(self):
        return str(self.d_categoryName)

    class Meta:
        verbose_name_plural = 'DeviceCategories'


class DeviceBrands(models.Model):
    d_barndCategory=models.ForeignKey(DeviceCategories,on_delete=models.CASCADE)
    d_brandName=models.CharField(max_length=50)
    d_brandDescription=models.TextField()

    def __str__(self):
        return str(self.d_brandName)

    class Meta:
        verbose_name_plural = 'DeviceBrands'


class Devices(models.Model):
    appliance=models.ForeignKey(Appliances,on_delete=models.CASCADE)
    deviceBrand=models.ForeignKey(DeviceBrands,on_delete=models.CASCADE)
    deviceModel=models.CharField(max_length=20)
    deviceDescription = models.TextField()

    def __str__(self):
        return str(self.deviceBrand) + '-' + str(self.deviceBrand) + '-' + str(self.deviceModel)

    class Meta:
        verbose_name_plural = 'Devices'


class DevicesPrice(models.Model):
    device=models.ForeignKey(Devices,on_delete=models.CASCADE)
    devicePrice = models.BigIntegerField()
    createdDate=models.DateTimeField()
    def __str__(self):
        return str(self.device) + '-' + str(self.devicePrice) + '-' + str(self.createdDate)

    class Meta:
        verbose_name_plural = 'DevicesPrice'


class Provinces(models.Model):
    provinceName = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return str(self.provinceName)

    class Meta:
        verbose_name_plural = 'Provinces'


class ProvinceGeofence(models.Model):
    province = models.ForeignKey(Provinces,on_delete=models.CASCADE, null=False, blank=False)
    provinceLat = models.FloatField()
    provinceLong = models.FloatField()

    def __str__(self):
        return str(self.province) + '-' + str(self.provinceLat) + '-' + str(self.provinceLong)

    class Meta:
        verbose_name_plural = 'ProvinceGeofence'


class Regions(models.Model):
    regionName = models.CharField(max_length=50, null=False, blank=False)
    regionDescription= models.TextField()

    def __str__(self):
        return str(self.regionName)

    class Meta:
        verbose_name_plural = 'Regions'

class RegionsGeofence(models.Model):
    region = models.ForeignKey(Provinces,on_delete=models.CASCADE, null=False, blank=False)
    regionLat = models.FloatField()
    regionLong = models.FloatField()

    def __str__(self):
        return str(self.region) + '-' + str(self.regionLat) + '-' + str(self.regionLong)

    class Meta:
        verbose_name_plural = 'RegionsGeofence'


class DesignModels(models.Model):
    modelName=models.CharField(max_length=20)
    modelTitle=models.CharField(max_length=20)

    def __str__(self):
        return str(self.modelName)

    class Meta:
        verbose_name_plural = 'DesignModels'


class DesignJson(models.Model):
    modelName=models.ForeignKey(DesignModels, on_delete=models.CASCADE)
    fieldsJson=models.TextField()

    def __str__(self):
        return str(self.modelName)

    class Meta:
        verbose_name_plural = 'DesignJson'


class sms(models.Model):
    userId = models.CharField(max_length=11)
    verifyCode = models.CharField(max_length=10)

    def __str__(self):
        return str(self.userId)

    class Meta:
        verbose_name_plural = 'sms'