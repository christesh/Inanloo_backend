from django.db import models
from baseinfo.models import Devices
from personal.models import Technician,CompanyMembers,Supplier

# Create your models here.


class IndividualDevice(models.Model):
    supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE)
    device=models.ForeignKey(Devices, on_delete=models.CASCADE)
    individualDeviceBarcode = models.CharField(max_length=40)
    DEVICE_STATUS_CHOICES = [
        ('Available', 'موجود در انبار'),
        ('Sold', 'فروخته شده'),
        ('Loaned', 'امانی'),
        ('Returned', 'مرجوعی')
    ]
    individualDeviceStatus = models.CharField(max_length=30, choices=DEVICE_STATUS_CHOICES)
    individualDeviceDescription = models.TextField()

    def __str__(self):
        return str(self.individualDeviceBarcode) + '-' + str(self.individualDeviceStatus)

    class Meta:
        verbose_name_plural = 'IndividualDevice'


class SoldIndividualDevice(models.Model):
    device=models.ForeignKey(IndividualDevice,on_delete=models.CASCADE)
    technician=models.ForeignKey(Technician, on_delete=models.CASCADE)
    seller=models.ForeignKey(CompanyMembers, on_delete=models.CASCADE)
    price=models.BigIntegerField()
    SALES_KIND_CHOICES = [
        ('Sold', 'فروخته شده'),
        ('Loaned', 'امانی'),
        ('Garranty', 'گارانتی')
    ]
    salesKind=models.CharField(max_length=30, choices=SALES_KIND_CHOICES)
    description=models.TextField()

    def __str__(self):
        return str(self.device) + '-' + str(self.technician) +'-'+str(self.salesKind) +'-'+str(self.seller)

    class Meta:
        verbose_name_plural = 'SoldIndividualDevice'


