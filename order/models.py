
from django.db import models
from personal.models import Customers,Technician,CompanyMembers,Addresses
from baseinfo.models import Appliances, Devices, Problems
from django.contrib.auth.models import User, Group
from warehouse.models import SoldIndividualDevice
# Create your models here.


class KindOfOrder(models.Model):
    """
    در این جدول انواع سفارشات تعریف می شود
    """
    orderKind=models.CharField(max_length=20, help_text='در این فیلد یک عنوان برای توع سفارش ذخیره می شود')
    description=models.TextField(null=True,blank=True, help_text='در این فیلد توصیحات مربوط به نوع سفارش ذخیره می شود')

    def __str__(self):
        return str(self.orderKind)

    class Meta:
        verbose_name_plural = 'KindOfOrder'


class OrderTimeRange(models.Model):
    """
    در این جدول بازه های زمانی امکان پذیر برای ثبت سفارش تعریف میشود
    """
    timeRange=models.CharField(max_length=20, help_text='در این فیلد یک نام برای بازه زمانی ذخیره می شود')
    startTime=models.TimeField( help_text='در این فیلد ساعت شروع بازه زمانی ذخیره می شود')
    endTime=models.TimeField( help_text='در این فیلد ساعت پایان بازه زمانی ذخیره می شود')
    description=models.TextField(null=True,blank=True, help_text='در این فیلد توضیحات لازم برای بازه زمانی ذخیره می شود')

    def __str__(self):
        return str(self.timeRange)

    class Meta:
        verbose_name_plural = 'OrderTimeRange'


class OrderStatus (models.Model):
    """
    در این جدول انواع وضعیت های مربوط به سفارش ها تعریف می شود
    """
    status=models.CharField(max_length=20,help_text='در این فیلد عنوان وضعیت ذخیره می شود')
    description=models.TextField(null=True,blank=True,help_text='در این فیلد توضیحات مربوط به وضعیت ذخیره می شود')

    def __str__(self):
        return str(self.status)

    class Meta:
        verbose_name_plural = 'OrderStatus'


class Order (models.Model):
    """
    در این جدول سفارشات مشتریان ثبت میشود
    """
    customer=models.ForeignKey(Customers,on_delete=models.CASCADE,help_text='در این فیلد مشخص می شود سفارش مربوط به کدام مشتری است')
    registerBy = models.ForeignKey(User, on_delete=models.CASCADE,help_text='در این فیلد ثبت کننده سفارش ذخیره می شود')
    registerDateTime=models.DateTimeField(help_text='در این فیلد زمان ثبت سفارش ذخیره می شود')
    appliance=models.ForeignKey(Appliances,on_delete=models.CASCADE,help_text='در این فیلد نوع لوازم خانگی مربط به سفارش ذخیره می شود')
    # device=models.ForeignKey(Devices, on_delete=models.CASCADE, null=True, blank=True,help_text='در این فیلد قطعه مربوط به سفارش ذخیره می شود')
    orderKind = models.ForeignKey(KindOfOrder, on_delete=models.CASCADE,help_text='در این فیلد نوع سفارش از جدول KindOfOrder ذخیره می شود')
    orderDate=models.DateField(help_text='در این فیلد تاریخ انجام سفارش ذخیره می شود')
    orderTimeRange=models.ForeignKey(OrderTimeRange , on_delete=models.CASCADE,help_text='در این فیلد بازه زمانی انجام سفارش ذخیره می شود')
    orderAddress = models.ForeignKey(Addresses, on_delete=models.CASCADE,help_text='در این فیلد آدرس انجام سفارش ذخیره می شود')
    orderStatus=models.ForeignKey(OrderStatus, on_delete=models.CASCADE,help_text='در این فیلد وضعیت سفارش ذخیره می شود')
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE, null=True, blank=True,help_text='در این فیلد تکنسین انجام دهنده سفارش ذخیره می شود')
    description = models.TextField(null=True,blank=True, help_text='در این فیلد توضیحات مازاد مربوط به انجام سفارش ذخیره می شود')

    def __str__(self):
        return str(self.customer) + '-' +str(self.registerDateTime)

    class Meta:
        verbose_name_plural = 'Order'


class OrderDetails(models.Model):
    """
    در این جدول اطلاعات مربوط به خرید قطعات استفاده شده در سفارش ذخیره می شود
    """
    order= models.ForeignKey(Order,on_delete=models.CASCADE,help_text='در این فیلد مشخص میشود قطعه خریداری شده مربوط به کدام سفارش است')
    soldIndividualDevice=models.ManyToManyField(SoldIndividualDevice,help_text='در این فیلد اطلاعات قطعه خریداری شده از جدول SoldIndividualDevice ذخیره می شود')

    def __str__(self):
        return str(self.order) + '-' + str(self.soldIndividualDevice)

    class Meta:
        verbose_name_plural = 'OrderDetails'


class CustomerProblems (models.Model):
    """
    در این جدول عیوب اظهاری مشتری ذخیره میشود
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              help_text='در این فیلد مشخص میشود قطعه خریداری شده مربوط به کدام سفارش است')
    problem=models.ForeignKey(Problems,on_delete=models.CASCADE,help_text='در این فلد مشکل از جدول Problems انتخاب میشود')
    customerDescription=models.TextField(null=True,blank=True, help_text='دراین فیلد توضیحات مربوط به مشکلات اظهاری مشتری ذخیره میشود')

    def __str__(self):
        return str(self.order) + '-' + str(self.problem)

    class Meta:
        verbose_name_plural = 'CustomerProblems'


class CustomerProblemPic (models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              help_text='در این فیلد مشخص میشود تصویر اپدیت شده مربوط به کدام سفارش است')
    problemImage = models.ImageField(upload_to='images/CustomerProblems/')

    def __str__(self):
        return str(self.order) + '-' + str(self.problemImage)

    class Meta:
        verbose_name_plural = 'CustomerProblemPic'


class TechnicianProblems (models.Model):
    """
    در این جدول عیوب اظهاری تکنسین ها ذخیره میشود
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              help_text='در این فیلد مشخص میشود قطعه خریداری شده مربوط به کدام سفارش است')
    problem=models.ForeignKey(Problems,on_delete=models.CASCADE,help_text='در این فلد مشکل از جدول Problems انتخاب میشود')
    technicianDescription=models.TextField(null=True,blank=True,help_text='دراین فیلد توضیحات مربوط به مشکلات اظهاری تکنسین ذخیره میشود')

    def __str__(self):
        return str(self.order) + '-' + str(self.problem)

    class Meta:
        verbose_name_plural = 'TechnicianProblems'


class TechnicianProblemPic (models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              help_text='در این فیلد مشخص میشود تصویر اپدیت شده مربوط به کدام سفارش است')
    problemImage = models.ImageField(upload_to='images/CustomerProblems/')

    def __str__(self):
        return str(self.order) + '-' + str(self.problemImage)

    class Meta:
        verbose_name_plural = 'CustomerProblemPic'

