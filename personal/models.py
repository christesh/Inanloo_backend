from django.db import models
from django.contrib.auth.models import User, Group
from baseinfo.models import Provinces, Regions
from django.utils.safestring import mark_safe

# Create your models here.

class Person(models.Model):
    firstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=100)
    nationalId = models.CharField(max_length=10,primary_key=True, null=False, blank=False )
    birthDate = models.DateField(null=True, blank=True)
    genderChoice = (
        ('0', 'زن'),
        ('1', 'مرد'))
    gender = models.CharField(max_length=10, choices=genderChoice, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    createdAt = models.DateTimeField(null=False, blank=False)
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE ,related_name='Creator')
    auth = models.ForeignKey(User, on_delete=models.CASCADE,related_name='User')
    picture = models.ImageField(upload_to='./UserPersonalImages', null=True, blank=True)
    ageRang = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.f_name) + '-' + str(self.l_name)

    class Meta:
        verbose_name_plural = 'Person'


class Mobiles(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    mobileNumebr=models.CharField(max_length=11, null=False, blank=False)
    isMain=models.BooleanField(null=False, blank=False)

    def __str__(self):
        return str(self.person) + '-' + str(self.mobileNumebr) +'-'+str(self.isMain)

    class Meta:
        verbose_name_plural = 'Mobiles'


class Phones(models.Model):
    person=models.ForeignKey(Person, on_delete=models.CASCADE)
    phoneNumebr=models.CharField(max_length=11, null=False, blank=False)
    isMain=models.BooleanField(null=False, blank=False)

    def __str__(self):
        return str(self.person) + '-' + str(self.phoneNumebr) +'-'+str(self.isMain)

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    catrgory = models.ForeignKey(Group, on_delete=models.CASCADE)
    active = models.BooleanField(null=True, blank=True)
    fillprofile = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return str(self.person) + '-' + str(self.user) + '-' + str(self.catrgory)

    class Meta:
        verbose_name_plural = 'PersonAuth'


class sms(models.Model):
    userid = models.CharField(max_length=11)
    vercode = models.CharField(max_length=10)

    def __str__(self):
        return str(self.userid)

    class Meta:
        verbose_name_plural = 'sms'

