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
        return str(self.id)+"=>"+str(self.pointTitle)

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
        return str(self.id)+"=>"+str(self.pointTitle)

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
    technicianPositivePoints=models.ManyToManyField(TechnicianPositivePoints , help_text='در این فیلد  نکات مثبت تکنسین ذخیره میشود')
    technicianNegativePoints = models.ManyToManyField(TechnicianNegativePoints, help_text='در این فیلد  نکات منفی تکنسین ذخیره میشود')
    commnet = models.TextField(null=True,blank=True)
    def __str__(self):
        return str(self.id)+"=>"+str(self.orderId)

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
        return str(self.id)+"=>"+str(self.pointTitle)

    class Meta:
        verbose_name_plural = 'CustomerNegativePoints'


class CustomerPositivePoints (models.Model):
    """
            در این جدول نکات مثبت مربوط به بازخورد تکنسین ها توسط مدیر سیستم تغریف میشوند
            """
    pointTitle=models.CharField(max_length=20, help_text='در این فیلد عنوان نکات مثبت ذخیره میشود')
    pointValue=models.FloatField(help_text='در این فیلد ارزش نکات مثبت ذخیره میشود')
    description=models.TextField(null=True,blank=True,help_text='در این فیلد توصیحات نکات مثبت ذخیره میشود')

    def __str__(self):
        return str(self.id)+"=>"+str(self.pointTitle)

    class Meta:
        verbose_name_plural = 'CustomerPositivePoints'


class CustomerSurvey(models.Model):
    """
        در این جدول اطلاعات مربوط به بازخورد تکنسین ها ذخیره میشود
        """
    userID = models.ForeignKey(User, on_delete=models.CASCADE, help_text='در این فیلد فرد ثبت کننده بازخورد ذخیره میشود')
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE, help_text='در این فیلد مشخص میشود این بازخورد مربوط به کدام سفارش است')
    orderRating = models.FloatField(help_text='در این فیلد امتیاز سفارش ذخیره میشود')
    surveyDate = models.DateTimeField( help_text='در این فیلد عنوان زمان ثبت یازخورد ذخیره میشود')
    customerPositivePoints = models.ManyToManyField(CustomerPositivePoints,  help_text='در این فیلد  نکات مثبت مشتری ذخیره میشود')
    customerNegativePoints = models.ManyToManyField(CustomerNegativePoints,  help_text='در این فیلد  نکات منفی مشتری ذخیره میشود')
    comment=models.TextField(null=True,blank=True,)
    def __str__(self):
        return str(self.id)+"=>"+str(self.orderId)

    class Meta:
        verbose_name_plural = 'CustomerSurvey'


class TicketStatus(models.Model):
    """
    در این جدول انواع وضعبت تیکت ها تعریف می شود
    """

    statusTitle=models.CharField(max_length=30, help_text='در این فیلد نامی عنوان وضعیت تیکیت ذخیره میشود')
    description=models.TextField(null=True,blank=True, help_text='در این فیلد توصیحات برای وضعیت تیکیت ذخیره میشود')

    def __str__(self):
        return str(self.statusTitle)

    class Meta:
        verbose_name_plural = 'TicketStatus'


class TicketPriority(models.Model):
    """
    در این جدول اولویت تیکت ها تعریف می شود
    """

    priorityTitle = models.CharField(max_length=30, help_text='در این فیلد عنوان برای اولویت تیکیت ذخیره میشود')
    description = models.TextField(null=True,blank=True, help_text='در این فیلد توضیحات برای اولویت تیکیت ذخیره میشود')

    def __str__(self):
        return str(self.priorityTitle)

    class Meta:
        verbose_name_plural = 'TicketPriority'


class  TicketSubjects(models.Model):
    title=models.CharField(max_length=50, help_text='در این فیلد شماره تیکیت ذخیره میشود')
    description=models.TextField(null=True,blank=True)
    def __str__(self):
        return str(self.id) +"=>"+str(self.title)

    class Meta:
        verbose_name_plural = 'TicketSubjects'


class Tickets(models.Model):
    """
    در این جدول اطلاعات مربوط به کلیه تیکت ها ذخیره می شود
    """
    ticketNo=models.CharField(max_length=10, help_text='در این فیلد شماره تیکیت ذخیره میشود')
    createBy=models.ForeignKey(User,on_delete=models.CASCADE , related_name='CreateBY', help_text='در این فیلد ثبت کننده تیکیت ذخیره میشود')
    createDateTime=models.DateTimeField( help_text='در این فیلد زمان ثبت تیکیت ذخیره میشود')
    closedDateTime=models.DateTimeField(null=True,blank=True,help_text='در این فیلد زمان بستن تیکیت ذخیره میشود')
    ticketStatus=models.ForeignKey(TicketStatus, on_delete=models.CASCADE,help_text='در این فیلد وضعیت تیکیت از جدول TicketStatus ذخیره میشود')
    ticketPriority = models.ForeignKey(TicketPriority, on_delete=models.CASCADE,help_text='در این فیلد اولویت تیکیت از جدول TicketPriority ذخیره میشود')
    subject=models.ForeignKey(TicketSubjects,on_delete=models.CASCADE,null=True,blank=True)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE,
                              help_text='در این فیلد مشخص میشود قطعه خریداری شده مربوط به کدام سفارش است')
    def __str__(self):
        return str(self.id) +"=>"+str(self.ticketNo)

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
        return str(self.id) +"=>"+str(self.ticketNo) +'-'+str(self.sender) +'-'+str(self.answerTo)

    class Meta:
        verbose_name_plural = 'TicketChats'

class TicketFiles(models.Model):

    ticketNo = models.ForeignKey(Tickets, on_delete=models.CASCADE,
                                 help_text='در این فیلد شماره تیکیت از جدول Tickets ذخیره میشود')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, help_text='در این فیلد ارسال کننده تیکیت ذخیره میشود')
    file=models.FileField(upload_to='teckets/files')

    def __str__(self):
        return str(self.id) +"=>" +str(self.ticketNo) +'-'+str(self.sender)

    class Meta:
        verbose_name_plural = 'TicketChats'

class ChatMessages(models.Model):

    sender = models.ForeignKey(User, on_delete=models.CASCADE, help_text='در این فیلد ارسال کننده پیام ذخیره میشود')
    receiver = models.CharField(max_length=5, help_text='در این فیلد دریافت کننده پیام ذخیره میشود')
    messageText = models.TextField(help_text='در این فیلد متن پیام ذخیره میشود')
    messageDateTime = models.DateTimeField(help_text='در این فیلد زمان ثبت پیام ذخیره میشود')
    read=models.BooleanField( null=True, blank=True)

    def __str__(self):
        return str(self.messageDateTime) + '-' + str(self.sender) + '-' + str(self.receiver)

    class Meta:
        verbose_name_plural = 'ChatMessages'

class UserChatStatus( models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, help_text='در این فیلد وضعیت کاربر برا چت ذخیره میشود')
    active=models.BooleanField()

    def __str__(self):
        return str(self.user) + '-' + str(self.active)

    class Meta:
        verbose_name_plural = 'UserChatStatus'