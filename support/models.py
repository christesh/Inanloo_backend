from django.db import models
from django.contrib.auth.models import User, Group
from order.models import *


# Create your models here.
class TechnicianNegativePoints(models.Model):
    """
    در این جدول نکات منفی مربوط به بازخورد تکنسین ها توسط مدیر سیستم تغریف میشوند
    """
    pointTitle = models.CharField(max_length=20, help_text='در این فیلد عنوان نکات منفی ذخیره میشود')
    pointValue = models.FloatField( help_text='در این فیلد ارزش نکات منفی ذخیره میشود')
    description = models.TextField(null=True,blank=True, help_text='در این فیلد توضیحات مربوط نکات منفی ذخیره میشود')

    def __str__(self):
        return str(self.pointTitle)

    class Meta:
        verbose_name_plural = 'TechnicianNegativePoints'


class TechnicianPositivePoints (models.Model):
    """
        در این جدول نکات مثبت مربوط به بازخورد تکنسین ها توسط مدیر سیستم تغریف میشوند
        """
    pointTitle=models.CharField(max_length=20, help_text='در این فیلد عنوان نکات مثبت ذخیره میشود')
    pointValue=models.FloatField( help_text='در این فیلد ارزش نکات مثبت ذخیره میشود')
    description=models.TextField(null=True,blank=True,help_text='در این فیلد توضیحات مربوط نکات مثبت ذخیره میشود')

    def __str__(self):
        return str(self.pointTitle)

    class Meta:
        verbose_name_plural = 'TechnicianPositivePoints'


class TechnicianSurvey (models.Model):
    """
    در این جدول اطلاعات مربوط به بازخورد تکنسین ها ذخیره میشود
    """
    userID=models.ForeignKey(User,on_delete=models.CASCADE, help_text='در این فیلد فرد ثبت کننده بازخورد ذخیره میشود')
    orderId=models.ForeignKey(Order,on_delete=models.CASCADE, help_text='در این فیلد مشخص میشود این بازخورد مربوط به کدام سفارش است')
    orderRating=models.FloatField( help_text='در این فیلد امتیاز سفارش ذخیره میشود')
    survayDate=models.DateTimeField( help_text='در این فیلد عنوان زمان ثبت یازخورد ذخیره میشود')
    technicianPositivePoints=models.ForeignKey(TechnicianPositivePoints , on_delete=models.CASCADE, help_text='در این فیلد  نکات مثبت تکنسین ذخیره میشود')
    technicianNegativePoints = models.ForeignKey(TechnicianNegativePoints, on_delete=models.CASCADE, help_text='در این فیلد  نکات منفی تکنسین ذخیره میشود')

    def __str__(self):
        return str(self.orderId)

    class Meta:
        verbose_name_plural = 'TechnicianSurvey'


class CustomerNegativePoints(models.Model):
    """
        در این جدول نکات منفی مربوط به بازخورد مشتریان توسط مدیر سیستم تغریف میشوند
        """
    pointTitle = models.CharField(max_length=20, help_text='در این فیلد عنوان نکات منفی ذخیره میشود')
    pointValue = models.FloatField(help_text='در این فیلد ارزش نکات منفی ذخیره میشود')
    description = models.TextField(null=True,blank=True,help_text='در این فیلد توصیحات نکات منفی ذخیره میشود')

    def __str__(self):
        return str(self.pointTitle)

    class Meta:
        verbose_name_plural = 'TechnicianNegativePoints'


class CustomerPositivePoints (models.Model):
    """
            در این جدول نکات مثبت مربوط به بازخورد تکنسین ها توسط مدیر سیستم تغریف میشوند
            """
    pointTitle=models.CharField(max_length=20, help_text='در این فیلد عنوان نکات مثبت ذخیره میشود')
    pointValue=models.FloatField(help_text='در این فیلد ارزش نکات مثبت ذخیره میشود')
    description=models.TextField(null=True,blank=True,help_text='در این فیلد توصیحات نکات مثبت ذخیره میشود')

    def __str__(self):
        return str(self.pointTitle)

    class Meta:
        verbose_name_plural = 'TechnicianPositivePoints'


class CustomerSurvey(models.Model):
    """
        در این جدول اطلاعات مربوط به بازخورد تکنسین ها ذخیره میشود
        """
    userID = models.ForeignKey(User, on_delete=models.CASCADE, help_text='در این فیلد فرد ثبت کننده بازخورد ذخیره میشود')
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE, help_text='در این فیلد مشخص میشود این بازخورد مربوط به کدام سفارش است')
    orderRating = models.FloatField(help_text='در این فیلد امتیاز سفارش ذخیره میشود')
    surveyDate = models.DateTimeField( help_text='در این فیلد عنوان زمان ثبت یازخورد ذخیره میشود')
    customerPositivePoints = models.ForeignKey(CustomerPositivePoints, on_delete=models.CASCADE, help_text='در این فیلد  نکات مثبت مشتری ذخیره میشود')
    customerNegativePoints = models.ForeignKey(CustomerNegativePoints, on_delete=models.CASCADE, help_text='در این فیلد  نکات منفی مشتری ذخیره میشود')

    def __str__(self):
        return str(self.orderId)

    class Meta:
        verbose_name_plural = 'CustomerSurvey'


class TicketStatus(models.Model):
    """
    در این جدول انواع وضعبت تیکت ها تعریف می شود
    """
    statusName=models.CharField(max_length=10, help_text='در این فیلد نامی برای وضعیت تیکیت ذخیره میشود')
    statusTitle=models.CharField(max_length=10, help_text='در این فیلد نامی عنوان وضعیت تیکیت ذخیره میشود')
    description=models.TextField(null=True,blank=True, help_text='در این فیلد توصیحات برای وضعیت تیکیت ذخیره میشود')

    def __str__(self):
        return str(self.statusTitle)

    class Meta:
        verbose_name_plural = 'TicketStatus'


class TicketPriority(models.Model):
    """
    در این جدول اولویت تیکت ها تعریف می شود
    """
    priorityName = models.CharField(max_length=10, help_text='در این فیلد نامی برای اولویت تیکیت ذخیره میشود')
    priorityTitle = models.CharField(max_length=10, help_text='در این فیلد عنوان برای اولویت تیکیت ذخیره میشود')
    description = models.TextField(null=True,blank=True, help_text='در این فیلد توضیحات برای اولویت تیکیت ذخیره میشود')

    def __str__(self):
        return str(self.priorityTitle)

    class Meta:
        verbose_name_plural = 'TicketStatus'


class Tickets(models.Model):
    """
    در این جدول اطلاعات مربوط به کلیه تیکت ها ذخیره می شود
    """
    ticketNo=models.CharField(max_length=10, help_text='در این فیلد شماره تیکیت ذخیره میشود')
    createBy=models.ForeignKey(User,on_delete=models.CASCADE , related_name='CreateBY', help_text='در این فیلد ثبت کننده تیکیت ذخیره میشود')
    answerBy=models.ForeignKey(User,on_delete=models.CASCADE , related_name='answerBy', help_text='در این فیلد پاسخ دهنده تیکیت ذخیره میشود')
    createDateTime=models.DateTimeField( help_text='در این فیلد زمان ثبت تیکیت ذخیره میشود')
    closedDateTime=models.DateTimeField(null=True,blank=True,help_text='در این فیلد زمان بستن تیکیت ذخیره میشود')
    ticketStatus=models.ForeignKey(TicketStatus, on_delete=models.CASCADE,help_text='در این فیلد وضعیت تیکیت از جدول TicketStatus ذخیره میشود')
    ticketPriority = models.ForeignKey(TicketPriority, on_delete=models.CASCADE,help_text='در این فیلد اولویت تیکیت از جدول TicketPriority ذخیره میشود')

    def __str__(self):
        return str(self.ticketNo)

    class Meta:
        verbose_name_plural = 'Tickets'


class TicketChats(models.Model):
    """
    در این جدول متن چت های مربوط به کلیه تیکت ها ذخیره می شود
    """
    ticketNo=models.ForeignKey(Tickets, on_delete=models.CASCADE, help_text='در این فیلد شماره تیکیت از جدول Tickets ذخیره میشود')
    sender=models.ForeignKey(User, on_delete=models.CASCADE, help_text='در این فیلد ارسال کننده تیکیت ذخیره میشود')
    answerTo=models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, help_text='در این فیلد مشخص می شود به کدام تیکیت پاسخ داده شده است')
    comment=models.TextField( help_text='در این فیلد متن تیکیت ذخیره میشود')
    chatDateTime=models.DateTimeField(help_text='در این فیلد زمان ثبت تیکیت ذخیره میشود')

    def __str__(self):
        return str(self.ticketNo) +'-'+str(self.sender) +'-'+str(self.answerTo)

    class Meta:
        verbose_name_plural = 'TicketChats'

