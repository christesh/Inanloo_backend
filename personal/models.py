from django.db import models
from django.contrib.auth.models import User, Group
from baseinfo.models import MembersGroup, Cities, Neighbourhoods, Provinces, Regions, Devices, CustomerCategory, TechnicianCategory, TechnicianSkills
from django.utils.safestring import mark_safe

# Create your models here.


class Person(models.Model):
    """
    این جدول اطلاعات کلی و پایه هر فردی که در سیستم ثبت میشود را نگهداری میکند
    """
    firstName = models.CharField(max_length=50,help_text='نام فرد در این فیلد ذخیره میشود')
    lastName = models.CharField(max_length=100,help_text='نام خانوادگی فرد در این فیلد ذخیره میشود')
    nationalId = models.CharField(max_length=10, null=True, blank=True ,help_text='کد ملی فرد در این فیلد ذخیره میشود')
    birthDate = models.DateField(null=True, blank=True,help_text='تاریخ تولد فرد در این فیلد ذخیره میشود')
    genderChoice = (
        ('0', 'زن'),
        ('1', 'مرد'))
    gender = models.CharField(max_length=10, choices=genderChoice, null=True, blank=True,help_text='جنسیت فرد در این فیلد ذخیره میشود')
    email = models.EmailField(null=True, blank=True,help_text='ادرس ایمیل فرد در این فیلد ذخیره میشود')
    createdAt = models.DateTimeField(null=False, blank=False,help_text='تاریخ ثبت نام فرد در این فیلد ذخیره میشود')
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE, related_name='creator',help_text='سخض ثبت نام کننده فرد در این فیلد ذخیره میشود')
    picture = models.ImageField(upload_to='userimage/UserPersonalImages', null=True, blank=True,help_text='تصویر پروفایل فرد در این فیلد ذخیره میشود')
    ageRang = models.IntegerField(null=True, blank=True,help_text='بازه سنی فرد در این فیلد ذخیره میشود')
    authuser = models.ForeignKey(User, on_delete=models.CASCADE,related_name='User',help_text=' در این فیلد مشخص میشود این فرد به چه نام کاربری در سیستم ثبت شده است')


class Customers(Person):
    """
    در این جدول اطلاعات مشتریان ذخیره میشود
    این جدول از جدول Person ارث بری میکند و علاوه بر اطلاعات آن اطلاعات دیگری صرفا هم برای مشتریان ذخیره میکند
    """
    customerCategory=models.ForeignKey(CustomerCategory, on_delete=models.CASCADE,help_text=' در این فیلد نوع مشتری از جدول CustomerCategory ذخیره میشود')
    customerDevices=models.ManyToManyField(Devices,help_text=' در این فیلد لوازم خانگی مشتری از جدول Devices ذخیره میشود')

    def __str__(self):
        return 'Customer' +str(self.firstName) + '-' + str(self.lastName) +'-'+str(self.nationalId)

    class Meta:
        verbose_name_plural = 'Customers'


class Technician(Person):
    """
       در این جدول اطلاعات تکنسین ها ذخیره میشود
       این جدول از جدول Person ارث بری میکند و علاوه بر اطلاعات آن اطلاعات دیگری صرفا هم برای تکنسین ها ذخیره میکند
       """
    technicianCategory = models.ForeignKey(TechnicianCategory, on_delete=models.CASCADE,help_text=' در این فیلد نوع تکنسین از جدول TechnicianCategory ذخیره میشود')
    technicianSkills= models.ManyToManyField(TechnicianSkills,help_text=' در این فیلد مهارت های تکنسین از جدول TechnicianSkills ذخیره میشود')
    technicianDevices=models.ManyToManyField(Devices,help_text=' در این فیلد لوازم خانگی تخصصی تکنسین از جدول Devices ذخیره میشود')
    technicianRank=models.FloatField(help_text=' در این فیلد گرید تکنسین ذخیره میشود')
    activate=models.BooleanField(help_text=' در این فیلد فعال بودن یا نبود تکنسین ذخیره میشود')
    hireForm=models.TextField(help_text=' در این فیلد اطلاعات فرم استخدامی تکنسین به صورت Json ذخیره میشود')
    def __str__(self):
        return 'Technician' + str(self.firstName) + '-' + str(self.lastName) +'-'+str(self.nationalId) +'-'+str(self.activate)

    class Meta:
        verbose_name_plural = 'Technician'


class CompanyMembers(Person):
    """
           در این جدول اطلاعات پرسنل شرکت ذخیره میشود
           این جدول از جدول Person ارث بری میکند و علاوه بر اطلاعات آن اطلاعات دیگری صرفا هم برای پرسنل شرکت ذخیره میکند
           """
    membersGroup= models.ForeignKey(MembersGroup, on_delete=models.CASCADE,help_text=' در این فیلد سطح دسترسی (نوع کاربری)  برای کارمند شرکت  از جدول MembersGroup ذخیره میشود')
    hireDate=models.DateField(help_text=' در این فیلد تاریخ استخدام ذخیره میشود')
    quitDate=models.DateField(help_text=' در این فیلد تاریخ اتمام همکاری ذخیره میشود')

    def __str__(self):
        return 'CompanyMember' + str(self.firstName) + '-' + str(self.lastName) +'-'+str(self.nationalId)

    class Meta:
        verbose_name_plural = 'CompanyMembers'


class Mobiles(models.Model):
    """
    در این جدول شماره تلفن های همراه افراد ذخیره میشود
    """
    person = models.ForeignKey(Person, on_delete=models.CASCADE,help_text=' در این فیلد مشخص میشود شماره موبایل مربوط به چه فردیست')
    mobileNumber=models.CharField(max_length=11, null=False, blank=False,help_text=' در این فیلد شماره موبایل ذخیره میشود')
    isMain=models.BooleanField(null=False, blank=False,help_text=' در این فیلد مشخص میشود آیا این شماره موبایل شماره موبایل اصلی قرد است یا نه')

    def __str__(self):
        return str(self.person) + '-' + str(self.mobileNumber) +'-'+str(self.isMain)

    class Meta:
        verbose_name_plural = 'Mobiles'


class Phones(models.Model):
    """
       در این جدول شماره تلفن های ثابت افراد ذخیره میشود
       """
    person=models.ForeignKey(Person, on_delete=models.CASCADE,help_text=' در این فیلد مشخص میشود شماره ثابت مربوط به چه فردیست')
    phoneNumber=models.CharField(max_length=11, null=False, blank=False,help_text=' در این فیلد شماره ثابت ذخیره میشود')
    isMain=models.BooleanField(null=False, blank=False,help_text=' در این فیلد مشخص میشود آیا این شماره ثابت شماره اصلی قرد است یا نه')

    def __str__(self):
        return str(self.person) + '-' + str(self.phoneNumber) +'-'+str(self.isMain)

    class Meta:
        verbose_name_plural = 'Phones'


class Addresses(models.Model):
    """
           در این جدول آدرس های افراد ذخیره میشود
           """
    person=models.ForeignKey(Person, on_delete=models.CASCADE,help_text=' در این فیلد مشخص میشود آدرس مربوط به چه فردیست')
    province=models.ForeignKey(Provinces, on_delete=models.CASCADE, null=True, blank=True,help_text=' در این فیلد مشخص آدرس مربوط به چه استانی است')
    city=models.ForeignKey(Cities, on_delete=models.CASCADE, null=True, blank=True,help_text=' در این فیلد مشخص آدرس مربوط به چه شهرستانی است')

    region=models.ForeignKey(Regions, on_delete=models.CASCADE, null=False, blank=False,help_text=' در این فیلد مشخص آدرس مربوط به چه منطقه ای است')
    neighbourhood=models.ForeignKey(Neighbourhoods, on_delete=models.CASCADE, null=True, blank=True,help_text=' در این فیلد مشخص آدرس مربوط به چه محله ای است')
    addressLat=models.FloatField(help_text='در این فیلد عرض جعرافیایی ذحیره می شود')
    addressLong=models.FloatField(help_text='در این فیلد طول جعرافیایی ذحیره می شود')
    addressStreet=models.TextField(null=False, blank=False,help_text='در این فیلد اسم خیابان ذحیره می شود')
    addressLane = models.TextField(null=False, blank=False,help_text='در این فیلد اسم کوچه ذحیره می شود')
    addressNo=models.SmallIntegerField(null=False, blank=False,help_text='در این فیلد پلاک ذحیره می شود')
    addressUnit=models.SmallIntegerField(null=True, blank=True,help_text='در این فیلد واحد ذحیره می شود')
    addressFloor=models.SmallIntegerField(null=False, blank=False,help_text='در این فیلد طبقه ذحیره می شود')
    isMain=models.BooleanField(null=False, blank=False,help_text=' در این فیلد مشخص میشود آیا این آدرس اصلی قرد است یا نه')

    def __str__(self):
        return str(self.person) + '-' + str(self.city) +'-'+str(self.region)+'-'+str(self.addressStreet)+'-'+str(self.addressLane)+'-'+str(self.addressNo)+'-'+str(self.isMain)

    class Meta:
        verbose_name_plural = 'Addresses'


class PersonAuth(models.Model):
    """
    در این جدول گروه کاربری فرد، فعال یا غیر فاعل بود و تکمیل بودن اطلاعات فرد ذخیره می شود
    """
    person = models.ForeignKey(Person, on_delete=models.CASCADE,help_text=' در این فیلد مشخص میشود اطلاعات مربوط به چه فردیست')
    category = models.ForeignKey(Group, on_delete=models.CASCADE,help_text=' در این فیلد مشخص میشود فرد مربوط به چه گروه کاربری است')
    active = models.BooleanField(null=True, blank=True,help_text=' در این فیلد مشخص میشود فرد فعال است یا نه')
    fillProfile = models.BooleanField(null=True, blank=True,help_text=' در این فیلد مشخص میشود آیا پروفایل فرد تکمیل شده است یا نه')

    def __str__(self):
        return str(self.person) + '-'  + str(self.category)

    class Meta:
        verbose_name_plural = 'PersonAuth'


class Supplier (models.Model):
    """
    در این جدول اطلاعات مربوط به تامین کنندگان ذخیره میشود
    """
    supplierName=models.CharField(max_length=100,help_text='در این فیلد نام تامین کننده ذحیره می شود')
    supplierTel=models.CharField(max_length=100,help_text='در این فیلد شماره تماس تامین کننده ذحیره می شود')
    supplierFax = models.CharField(max_length=100,help_text='در این فیلد فکس تامین کننده ذحیره می شود')
    supplierEmail = models.CharField(max_length=100,help_text='در این فیلد ایمیل تامین کننده ذحیره می شود')
    supplierAddress=models.CharField(max_length=500,help_text='در این فیلد آدرس تامین کننده ذحیره می شود')
    supplierAgentFirstName=models.CharField(max_length=10,help_text='در این فیلد نام رابط تامین کننده ذحیره می شود')
    supplierAgentLastName = models.CharField(max_length=50,help_text='در این فیلد نام خانوادگی رابط تامین کننده ذحیره می شود')
    supplierAgentMobile = models.CharField(max_length=50,help_text='در این فیلد موبایل رابط تامین کننده ذحیره می شود')

    def __str__(self):
        return str(self.supplierName)

    class Meta:
        verbose_name_plural = 'Supplier'

