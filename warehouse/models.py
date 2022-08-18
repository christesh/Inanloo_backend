from django.db import models
from baseinfo.models import Devices
from personal.models import Technician,CompanyMembers,Supplier

# Create your models here.


class IndividualDevice(models.Model):
    """
    در این جدول اطلاعات مربوط به هر قطعه ذخیره میشود
    """
    supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE, help_text='در این فیلد تامین کننده قطعه از جدول Supplier ذخیره میشود')
    device=models.ForeignKey(Devices, on_delete=models.CASCADE, help_text='در این فیلد قطعه از جدول Devices ذخیره میشود')
    individualDeviceBarcode = models.CharField(max_length=40, help_text='در این فیلد بارکد قطعه ذخیره میشود')
    DEVICE_STATUS_CHOICES = [
        ('Available', 'موجود در انبار'),
        ('Sold', 'فروخته شده'),
        ('Loaned', 'امانی'),
        ('Returned', 'مرجوعی')
    ]
    individualDeviceStatus = models.CharField(max_length=30, choices=DEVICE_STATUS_CHOICES, help_text='در این فیلد وضعیت قطعه ذخیره میشود')
    individualDeviceDescription = models.TextField(null=True, blank=True, help_text='در این فیلد توضیحات قطعه ذخیره میشود')

    def __str__(self):
        return str(self.individualDeviceBarcode) + '-' + str(self.individualDeviceStatus)

    class Meta:
        verbose_name_plural = 'IndividualDevice'


class SoldIndividualDevice(models.Model):
    """
    در این جدول اطلاعات مربوط به قطعات فروخته شده ذخیره می شود
    """
    device=models.ForeignKey(IndividualDevice,on_delete=models.CASCADE, help_text='در این فیلد مشخص میشود قطعه مربوط به کدام قطعه از جدول IndividualDevice است')
    technician=models.ForeignKey(Technician, on_delete=models.CASCADE, help_text='در این فیلد مشخص میشود تکنسین تحویل گرینده قطعه کیست')
    seller=models.ForeignKey(CompanyMembers, on_delete=models.CASCADE, help_text='در این فیلد مشخص میشود  پرسنل شرکت (انباردار) فروشنده قطعه کیست')
    price=models.BigIntegerField( help_text='در این فیلد قیمت قطعه مشخص میشود')
    SALES_KIND_CHOICES = [
        ('Sold', 'فروخته شده'),
        ('Loaned', 'امانی'),
        ('Garranty', 'گارانتی')
    ]
    salesKind=models.CharField(max_length=30, choices=SALES_KIND_CHOICES,help_text='در این فیلد توع قروش قطعه مشخص میشود')
    description=models.TextField(null=True, blank=True,help_text='در این فیلد توضیحات مربوط به فروش قطعه ذخیره میشود')

    def __str__(self):
        return str(self.device) + '-' + str(self.technician) +'-'+str(self.salesKind) +'-'+str(self.seller)

    class Meta:
        verbose_name_plural = 'SoldIndividualDevice'


