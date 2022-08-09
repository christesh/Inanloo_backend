from django.db import models
from django.contrib.auth.models import User, Group
from baseinfo.models import MembersGroup, Provinces, Regions, Devices, CustomerCategory, TechnicianCategory, TechnicianSkills
from django.utils.safestring import mark_safe

# Create your models here.


class Person(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=100)
    nationalId = models.CharField(max_length=10,primary_key=True, null=False, blank=False )
    birthDate = models.DateField(null=True, blank=True)
    genderChoice = (
        ('0', 'زن'),
        ('1', 'مرد'))
    gender = models.CharField(max_length=10, choices=genderChoice, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    createdAt = models.DateTimeField(null=False, blank=False)
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE, related_name='creator')
    picture = models.ImageField(upload_to='./UserPersonalImages', null=True, blank=True)
    ageRang = models.IntegerField(null=True, blank=True)
    authuser = models.ForeignKey(User, on_delete=models.CASCADE,related_name='User')

class Customers(Person):
    customerCategory=models.ForeignKey(CustomerCategory, on_delete=models.CASCADE)
    customerDevices=models.ManyToManyField(Devices)

    def __str__(self):
        return 'Customer' +str(self.firstName) + '-' + str(self.lastName) +'-'+str(self.nationalId)

    class Meta:
        verbose_name_plural = 'Customers'


class Technician(Person):
    technicianCategory = models.ForeignKey(TechnicianCategory, on_delete=models.CASCADE)
    technicianSkills= models.ManyToManyField(TechnicianSkills)
    technicianDevices=models.ManyToManyField(Devices)
    technicianRank=models.FloatField()
    activate=models.BooleanField()

    def __str__(self):
        return 'Technician' + str(self.firstName) + '-' + str(self.lastName) +'-'+str(self.nationalId) +'-'+str(self.activate)

    class Meta:
        verbose_name_plural = 'Technician'


class CompanyMembers(Person):
    membersGroup= models.ForeignKey(MembersGroup, on_delete=models.CASCADE)
    hireDate=models.DateField()
    quitDate=models.DateField()

    def __str__(self):
        return 'CompanyMember' + str(self.firstName) + '-' + str(self.lastName) +'-'+str(self.nationalId)

    class Meta:
        verbose_name_plural = 'CompanyMembers'


class Mobiles(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    mobileNumber=models.CharField(max_length=11, null=False, blank=False)
    isMain=models.BooleanField(null=False, blank=False)

    def __str__(self):
        return str(self.person) + '-' + str(self.mobileNumber) +'-'+str(self.isMain)

    class Meta:
        verbose_name_plural = 'Mobiles'


class Phones(models.Model):
    person=models.ForeignKey(Person, on_delete=models.CASCADE)
    phoneNumber=models.CharField(max_length=11, null=False, blank=False)
    isMain=models.BooleanField(null=False, blank=False)

    def __str__(self):
        return str(self.person) + '-' + str(self.phoneNumber) +'-'+str(self.isMain)

    class Meta:
        verbose_name_plural = 'Phones'


class Addresses(models.Model):
    person=models.ForeignKey(Person, on_delete=models.CASCADE)
    province=models.ForeignKey(Provinces, on_delete=models.CASCADE, null=True, blank=True)
    region=models.ForeignKey(Regions, on_delete=models.CASCADE, null=False, blank=False)
    addresslat=models.FloatField()
    addresslong=models.FloatField()
    addressStreet=models.TextField(null=False, blank=False)
    addressLane = models.TextField(null=False, blank=False)
    addressNo=models.SmallIntegerField(null=False, blank=False)
    addressUnit=models.SmallIntegerField(null=True, blank=True)
    addressFloor=models.SmallIntegerField(null=False, blank=False)
    isMain=models.BooleanField(null=False, blank=False)

    def __str__(self):
        return str(self.person) + '-' + str(self.province) +'-'+str(self.region)+'-'+str(self.addressStreet)+'-'+str(self.addressLane)+'-'+str(self.addressNo)+'-'+str(self.isMain)

    class Meta:
        verbose_name_plural = 'Addresses'


class PersonAuth(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    category = models.ForeignKey(Group, on_delete=models.CASCADE)
    active = models.BooleanField(null=True, blank=True)
    fillProfile = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return str(self.person) + '-' + str(self.user) + '-' + str(self.category)

    class Meta:
        verbose_name_plural = 'PersonAuth'


class Supplier (models.Model):
    supplierName=models.CharField(max_length=100)
    supplierTel=models.CharField(max_length=100)
    supplierFax = models.CharField(max_length=100)
    supplierEmail = models.CharField(max_length=100)
    supplierAddress=models.CharField(max_length=500)
    supplierAgentFirstName=models.CharField(max_length=10)
    supplierAgentLastName = models.CharField(max_length=50)
    supplierAgentMobile = models.CharField(max_length=50)

    def __str__(self):
        return str(self.supplierName)

    class Meta:
        verbose_name_plural = 'Supplier'

