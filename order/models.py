
from django.db import models
from personal.models import Customers,Technician,CompanyMembers,Addresses
from baseinfo.models import Appliances,Devices
from django.contrib.auth.models import User, Group
from warehouse.models import SoldIndividualDevice
# Create your models here.


class KindOfOrder(models.Model):
    orderKind=models.CharField(max_length=20)
    description=models.TextField()

    def __str__(self):
        return str(self.orderKind)

    class Meta:
        verbose_name_plural = 'KindOfOrder'


class OrderTimeRange(models.Model):
    timeRange=models.CharField(max_length=20)
    startTime=models.TimeField()
    endTime=models.TimeField()
    description=models.TextField()

    def __str__(self):
        return str(self.timeRange)

    class Meta:
        verbose_name_plural = 'OrderTimeRange'


class OrderStatus (models.Model):
    status=models.CharField(max_length=20)
    description=models.TextField()

    def __str__(self):
        return str(self.status)

    class Meta:
        verbose_name_plural = 'OrderStatus'


class Order (models.Model):
    customer=models.ForeignKey(Customers,on_delete=models.CASCADE)
    registerBy = models.ForeignKey(User, on_delete=models.CASCADE)
    registerDateTime=models.DateTimeField()
    appliance=models.ForeignKey(Appliances,on_delete=models.CASCADE)
    device=models.ForeignKey(Devices, on_delete=models.CASCADE, null=True, blank=True)
    orderKind = models.ForeignKey(KindOfOrder, on_delete=models.CASCADE)
    orderDate=models.DateField();
    orderTimeRange=models.ForeignKey(OrderTimeRange , on_delete=models.CASCADE)
    orderAddress = models.ForeignKey(Addresses, on_delete=models.CASCADE)
    orderStatus=models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return str(self.customer) + '-' +str(self.registerDateTime)

    class Meta:
        verbose_name_plural = 'Order'


class OrderDetails(models.Model):
    order= models.ForeignKey(Order,on_delete=models.CASCADE)
    soldIndividualDevice=models.ManyToManyField(SoldIndividualDevice)

    def __str__(self):
        return str(self.order) + '-' + str(self.soldIndividualDevice)

    class Meta:
        verbose_name_plural = 'OrderDetails'









