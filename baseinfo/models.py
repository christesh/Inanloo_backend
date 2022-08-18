from django.db import models
# from personal.models import Supplier
from django.contrib.auth.models import User, Group

# Create your models here.


class MembersGroup(models.Model):
    """
    در این جدول گروه های کاربری تعریف می شود
    """
    group=models.CharField(max_length=40,help_text='در این فیلد عنوان گروه ها ذخیره می شود')
    description=models.TextField(null=True,blank=True,help_text='در این فیلد توضیحات مربوط به گروه ها ذخیره می شود')

    def __str__ (self):
        return str(self.group)

    class Meta:
        verbose_name_plural = 'MembersGroup'


class CustomerCategory(models.Model):
    """
    در این جدول طبقه بندی مشتریان تعریف میشود
    """
    customerCategory=models.CharField(max_length=50,help_text='در این فیلد عنوان طبقه ها ذخیره می شود')
    categoryDescription=models.TextField(null=True,blank=True,help_text='در این فیلد توضیحات مربوط به طبقه ها ذخیره می شود')

    def __str__(self):
        return str(self.customerCategory)

    class Meta:
        verbose_name_plural = 'CustomerCategory'


class TechnicianCategory(models.Model):
    """
        در این جدول طبقه بندی تکنسین ها تعریف میشود
    """
    technicianCategory=models.CharField(max_length=50,help_text='در این فیلد عنوان طبقه ها ذخیره می شود')
    technicianDescription=models.TextField(null=True,blank=True,help_text='در این فیلد توضیحات مربوط به طبقه ها ذخیره می شود')

    def __str__(self):
        return str(self.technicianCategory)

    class Meta:
        verbose_name_plural = 'TechnicianCategory'


class TechnicianSkills(models.Model):
    """
          در این جدول مهارتهای مربوط به تکنسین ها تعریف میشود
    """
    skill=models.CharField(max_length=50,help_text='در این فیلد عنوان  مهارتها ذخیره می شود')
    skillDescription=models.TextField(null=True,blank=True,help_text='در این فیلد توضیحات مربوط به مهارتها ذخیره می شود')

    def __str__(self):
        return str(self.skill)

    class Meta:
        verbose_name_plural = 'TechnicianSkills'


class ApplianceCategories(models.Model):
    """
             در این جدول طبقه بندی مربوط به لوازم خانگی تعریف میشود
    """
    a_categoryName=models.CharField(max_length=50,help_text='در این فیلد عنوان انواع لوازم خانگی ذخیره می شود')
    a_categoryDescription=models.TextField(null=True,blank=True,help_text='در این فیلد توضیحات مربوط به لوازم خانگی ذخیره می شود')
    a_categoryImage=models.ImageField(upload_to='images/ApplianceCategories/')
    def __str__(self):
        return str(self.a_categoryName)

    class Meta:
        verbose_name_plural = 'ApplianceCategories'


class ApplianceBrands(models.Model):
    """
       در این جدول برندهای مربوط به لوازم خانگی تعریف میشود
    """
    a_barndCategory=models.ForeignKey(ApplianceCategories,on_delete=models.CASCADE,help_text='در این فیلد مشخص میشود که هریک از برند های به کدام نوع از لوازم خانگی مربوط است')
    a_brandName=models.CharField(max_length=50,help_text='در این فیلد نام برند ذخیره می شود')
    a_brandDescription=models.TextField(null=True,blank=True,help_text='در این فیلد توضیحات مربوط به هر برند ذخیره می شود')
    a_brandImage = models.ImageField(upload_to='images/ApplianceBrands/')
    def __str__(self):
        return str(self.a_brandName)

    class Meta:
        verbose_name_plural = 'ApplianceBrands'


class Appliances(models.Model):
    """
    در این جدول مدل هریک از لوازم خانگی ذخیره میشود
    """
    applianceBrand=models.ForeignKey(ApplianceBrands,on_delete=models.CASCADE,help_text='در این فیلد مشخص میشود که هریک از مدلهای به کدام برند مربوط است')
    applianceModel=models.CharField(max_length=20,null=True, blank=True,help_text='در این فیلد عنوان مدل ذخیره می شود')
    applianceSerial = models.CharField(max_length=20, null=True, blank=True,help_text='در این فیلد سریال دستگاه ذخیره میشود')
    applianceDescription=models.TextField(null=True,blank=True,help_text='در این فیلد توصیخات موربوط به مدل دستگاه ذخیره می شود')
    applianceRate=models.FloatField(null=True,blank=True,help_text='در این فیلد برای مدل ها رنج ارزشی مالی ذخیره می شود')
    applianceImage = models.ImageField(upload_to='images/Appliances/')
    def __str__(self):
        return str(self.applianceBrand) + '-' + str(self.applianceModel)

    class Meta:
        verbose_name_plural = 'Appliances'


class AppliancesSupplier(models.Model):
    """
    در این جدول ارتباط بین دستگاه و تامین کننده مشخص میشود
    """
    supplier=models.ForeignKey('personal.Supplier',on_delete=models.CASCADE, null=True, blank=True,help_text='در این فیلد نام تامین کننده دستگاه مشخص میشود')
    appliance = models.ForeignKey(Appliances, on_delete=models.CASCADE,help_text='در این فیلد نام دستگاه ذخیره میشود')

    def __str__(self):
        return str(self.appliance) + '-' + str(self.supplier)

    class Meta:
        verbose_name_plural = 'AppliancesSupplier'


class DeviceCategories(models.Model):
    """
    در این جدول ظبقه بندی قطعات ذخیره می شود
    """
    d_categoryName=models.CharField(max_length=50,help_text='در این فیلد عنوان طبقه بندی قطعات ذخیره می شود')
    d_categoryDescription=models.TextField(null=True, blank=True,help_text='در این فیلد توضیحات طبقه بندی قطعات ذخیره می شود')
    d_categoryImage = models.ImageField(upload_to='images/DeviceCategories/')
    def __str__(self):
        return str(self.d_categoryName)

    class Meta:
        verbose_name_plural = 'DeviceCategories'


class DeviceBrands(models.Model):
    """
        در این جدول برند ثطعات ذخیره میشود
    """
    d_barndCategory=models.ForeignKey(DeviceCategories,on_delete=models.CASCADE,help_text='در این فیلد نوع قطغه از اطلاعات ذخیره شده در جدول DeviceCategories ذخیره می شود')
    d_brandName=models.CharField(max_length=50,help_text='در این فیلد عنوان برند قطعات ذخیره می شود')
    d_brandDescription=models.TextField(null=True, blank=True,help_text='در این فیلد توصیحات برند قطعات ذخیره می شود')
    d_brandImage = models.ImageField(upload_to='images/DeviceBrands/')
    def __str__(self):
        return str(self.d_brandName)

    class Meta:
        verbose_name_plural = 'DeviceBrands'


class Devices(models.Model):
    """
            در این جدول اطلاعات ثطعات ذخیره میشود
    """
    appliance=models.ForeignKey(Appliances,on_delete=models.CASCADE,help_text='در این فیلد می شود این قطعه به کدام یک از لوازم خانگی مربیط است')
    deviceBrand=models.ForeignKey(DeviceBrands,on_delete=models.CASCADE,help_text='در این فیلد می شود این قطعه به کدام یک از برندها مربیط است')
    deviceModel=models.CharField(max_length=20,null=True,blank=True,help_text='در این فیلد مدل قطعه ذحیره می شود')
    deviceDescription = models.TextField(null=True,blank=True,help_text='در این فیلد توصیخات مدل قطعه ذحیره می شود')
    deviceImage = models.ImageField(upload_to='images/Devices/')

    def __str__(self):
        return str(self.deviceBrand) + '-' + str(self.deviceBrand) + '-' + str(self.deviceModel)

    class Meta:
        verbose_name_plural = 'Devices'


class DevicesPrice(models.Model):
    """
    دز این جدول قیمت قطعات ذهیره میشود
    """
    device=models.ForeignKey(Devices,on_delete=models.CASCADE,help_text='در این فیلد مشحص میشود قیمت مربوط به کدام قطعه است')
    devicePrice = models.BigIntegerField(help_text='در این فیلد قیمت قطعه ذحیره می شود')
    createdDate=models.DateTimeField(help_text='در این فیلد تاریخ ثبت قیمت قطعه ذحیره می شود')
    def __str__(self):
        return str(self.device) + '-' + str(self.devicePrice) + '-' + str(self.createdDate)

    class Meta:
        verbose_name_plural = 'DevicesPrice'


class Problems(models.Model):
    """
    در این جدول انواع مشکلات مربوط به هر دستگاه تعریف می شود
    """
    appliances = models.ForeignKey(Appliances, on_delete=models.CASCADE,
                           help_text='در این فیلد مشحص میشود مشکل مربوط به کدام یک از لوازم خانگی است')
    problemTitle = models.CharField(max_length=20, help_text='در این فیلد عنوان مشکل ذخیره میشود')
    problemDescription = models.TextField(null=True,blank=True,help_text='در این فیلد توضیحات مربوط به مشکل ذخیره می شود')
    problemKind=models.CharField(max_length=20,help_text='در این فیلد نوع مشکل ذخیره می شود')

    def __str__(self):
        return str(self.problemTitle)

    class Meta:
        verbose_name_plural = 'Problems'


class Provinces(models.Model):
    """
    در این جدول اسامی استان ها ذحیره میشود
    """
    provinceName = models.CharField(max_length=50, null=False, blank=False,help_text='در این فیلد نام استان ذحیره می شود')

    def __str__(self):
        return str(self.provinceName)

    class Meta:
        verbose_name_plural = 'Provinces'


class ProvinceGeofence(models.Model):
    """
    در این جدول نقاط مخدوده جغرافیایی استان ذحیره میشود
    """
    province = models.ForeignKey(Provinces,on_delete=models.CASCADE, null=False, blank=False,help_text='در این فیلد می شود  نقطه محدوده مربوط به کدام استان است')
    provinceLat = models.FloatField(help_text='در این فیلد عرض جعرافیایی ذحیره می شود')

    provinceLong = models.FloatField(help_text='در این فیلد طول جغرافیایی ذحیره می شود')

    def __str__(self):
        return str(self.province) + '-' + str(self.provinceLat) + '-' + str(self.provinceLong)

    class Meta:
        verbose_name_plural = 'ProvinceGeofence'


class Cities(models.Model):
    """
    در این جدول اسامی شهرستان ها ذحیره میشود
    """
    province = models.ForeignKey(Provinces, on_delete=models.CASCADE,help_text='در این فیلد مشخص میشود شهرستان مربوط به کدام استان است')
    cityName = models.CharField(max_length=50, null=False, blank=False,
                                    help_text='در این فیلد نام شهرستان ذحیره می شود')
    def __str__(self):
        return str(self.cityName)

    class Meta:
        verbose_name_plural = 'Cities'


class CityGeofence(models.Model):
    """
    در این جدول نقاط محدوده جغرافیایی شهرستان ذحیره میشود
    """
    city = models.ForeignKey(Cities,on_delete=models.CASCADE, null=False, blank=False,help_text='در این فیلد می شود نقطه محدوده مربوط به کدام شهرستان است')
    cityLat = models.FloatField(help_text='در این فیلد عرض جعرافیایی ذحیره می شود')
    cityLong = models.FloatField(help_text='در این فیلد طول جغرافیایی ذحیره می شود')


    def __str__(self):
        return str(self.city) + '-' + str(self.cityLat) + '-' + str(self.cityLong)

    class Meta:
        verbose_name_plural = 'CityGeofence'


class Regions(models.Model):
    """
        در این جدول اسامی مناطق ذحیره میشود
    """
    city=models.ForeignKey(Cities,on_delete=models.CASCADE,help_text='در این فیلد مشخص میشود منطقه مربوط به کدام شهرستان است')
    regionName = models.CharField(max_length=50, null=False, blank=False,help_text='در این فیلد نام منطقه ذحیره می شود')
    regionDescription= models.TextField(null=True,blank=True,help_text='در این فیلد توضیحات مربوط به مناطق ذحیره می شود')

    def __str__(self):
        return str(self.regionName)

    class Meta:
        verbose_name_plural = 'Regions'

class RegionsGeofence(models.Model):
    """
       در این جدول نقاط مخدوده جغرافیایی منظقه ذحیره میشود
    """
    region = models.ForeignKey(Regions,on_delete=models.CASCADE, null=False, blank=False,help_text='در این فیلد مشحص می شود هر نقطه مربوط به کدام منظقه می شود')
    regionLat = models.FloatField(help_text='در این فیلد عرض جعرافیایی ذحیره می شود')
    regionLong = models.FloatField(help_text='در این فیلد طول جعرافیایی ذحیره می شود')

    def __str__(self):
        return str(self.region) + '-' + str(self.regionLat) + '-' + str(self.regionLong)

    class Meta:
        verbose_name_plural = 'RegionsGeofence'


class Neighbourhoods(models.Model):
    """
        در این جدول اسامی محله ها ذخیره میشود
    """
    city = models.ForeignKey(Cities, on_delete=models.CASCADE,
                             help_text='در این فیلد مشخص میشود منطقه مربوط به کدام شهرستان است')
    neighbourhoodName = models.CharField(max_length=50, null=False, blank=False,help_text='در این فیلد نام محله ذحیره می شود')
    neighbourhoodDescription= models.TextField(null=True,blank=True,help_text='در این فیلد توضیحات مربوط به محله ذحیره می شود')

    def __str__(self):
        return str(self.neighbourhoodName)

    class Meta:
        verbose_name_plural = 'Neighbourhoods'


class NeighbourhoodGeofence(models.Model):
    """
       در این جدول نقاط محدوده جغرافیایی محله ها ذحیره میشود
    """
    neighbourhood = models.ForeignKey(Neighbourhoods,on_delete=models.CASCADE, null=False, blank=False,help_text='در این فیلد مشحص می شود هر نقطه مربوط به کدام محله می شود')
    neighbourhoodLat = models.FloatField(help_text='در این فیلد عرض جعرافیایی ذحیره می شود')
    neighbourhoodLong = models.FloatField(help_text='در این فیلد طول جعرافیایی ذحیره می شود')

    def __str__(self):
        return str(self.neighbourhood) + '-' + str(self.neighbourhoodLat) + '-' + str(self.neighbourhoodLong)

    class Meta:
        verbose_name_plural = 'NeighbourhoodGeofence'


class HireForm(models.Model):
    """
    در این جدول انواع فرم های مورد نیاز ذخیره میشود
    """
    formName=models.CharField(max_length=20,help_text='در این فیلد نام فرم ذحیره می شود')
    formTitle=models.CharField(max_length=20,help_text='در این فیلد عنوان قابل نمایش فرم ذحیره می شود')

    def __str__(self):
        return str(self.formName)

    class Meta:
        verbose_name_plural = 'HireForm'


class HireJson(models.Model):
    """
    در این جدول طراحی فرم های مورد نیاز ذخیره می شود
    """
    form=models.ForeignKey(HireForm, on_delete=models.CASCADE,help_text='در این فیلد مشحص می شود هریک از طراحی های انجام شده مربوط به کدام فرم است')
    formJson=models.TextField(help_text='در این فیلد طراحی فرم  به صورت Json ذحیره می شود')

    def __str__(self):
        return str(self.form)

    class Meta:
        verbose_name_plural = 'HireJson'


class OTPsms(models.Model):
    """
    در این جدول اطلاعات مربوط به پیامک های OTP ذخیره می شود
    """
    userId = models.CharField(max_length=11,help_text='در این فیلد مشخص می شود پبامک برای کدام کاربر ارسال شده است')
    verifyCode = models.CharField(max_length=10,help_text='در این فیلد کد تایید برای ورود یا ثبت نام دخیره می شود')

    def __str__(self):
        return str(self.userId)

    class Meta:
        verbose_name_plural = 'OTPsms'


class SmsTypes(models.Model):
    """
    در این جدول اطلاعات مربوط به انواع پیامک ها ذخیره می شود
    """
    smsName = models.CharField(max_length=11,help_text='در این فیلد عنوان پیامک ذخیره میشود')
    smsKinds=(
        ('info','اطلاع رسانی'),
        ('feadback','بازخورد')
    )
    smsKind = models.CharField(max_length=10, choices=smsKinds, help_text='در این فیلد مشخص می شود پیامک ارسالی از نوع اطلاع رسانی بوده یا بازخورد')
    smsCaption = models.TextField(help_text='در این فیلد متن پیامک ارسالی ذخیره می شود')

    def __str__(self):
        return str(self.smsName) + '-' + str(self.smsKind)

    class Meta:
        verbose_name_plural = 'SmsTypes'


class Sms(models.Model):
    """
    در این جدول اطلاعات مربوط به پیامک های ارسالی و دریافتی ذخیره می شود
    """
    smsType = models.ForeignKey( SmsTypes, on_delete=models.CASCADE,help_text='در این فیلد مشخص میشو پیامک مربوط به کدام نوع از پیامک های تعریف شده در جدول SmsTypes میشود')
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,help_text='در این فیلد گیرنده پیامک ذخیره می شود')
    smsCaption = models.TextField(help_text='در این فیلد متن پیامک ارسالی ذخیره می شود')
    smsSendDateTime = models.DateTimeField(help_text='در این فیلد زمان ارسال پیامک ارسالی ذخیره می شود')
    smsAnswer = models.TextField(help_text='در این فیلد پاسخ دریافتی از مخاطب ذخیره می شود')
    smsReceiveDateTime = models.DateTimeField(help_text='در این فیلد زمان دریافت پیامک جواب ذخیره می شود')

    def __str__(self):
        return str(self.smsName) + '-' + str(self.smsKind)

    class Meta:
        verbose_name_plural = 'SmsTypes'