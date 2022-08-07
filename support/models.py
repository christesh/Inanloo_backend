from django.db import models
from django.contrib.auth.models import User, Group
from order.models import *


# Create your models here.
class TechnicianNegativePoints(models.Model):
    pointTitle = models.CharField(max_length=20)
    pointValue = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return str(self.pointTitle)

    class Meta:
        verbose_name_plural = 'TechnicianNegativePoints'


class TechnicianPositivePoints (models.Model):
    pointTitle=models.CharField(max_length=20)
    pointValue=models.FloatField()
    description=models.TextField()

    def __str__(self):
        return str(self.pointTitle)

    class Meta:
        verbose_name_plural = 'TechnicianPositivePoints'


class TechnicianSurvey (models.Model):
    userID=models.ForeignKey(User,on_delete=models.CASCADE)
    orderId=models.ForeignKey(Order,on_delete=models.CASCADE)
    orderRating=models.FloatField()
    survayDate=models.DateTimeField()
    technicianPositivePoints=models.ForeignKey(TechnicianPositivePoints , on_delete=models.CASCADE)
    technicianNegativePoints = models.ForeignKey(TechnicianNegativePoints, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.orderId)

    class Meta:
        verbose_name_plural = 'TechnicianSurvey'


class CustomerNegativePoints(models.Model):
    pointTitle = models.CharField(max_length=20)
    pointValue = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return str(self.pointTitle)

    class Meta:
        verbose_name_plural = 'TechnicianNegativePoints'


class CustomerPositivePoints (models.Model):
    pointTitle=models.CharField(max_length=20)
    pointValue=models.FloatField()
    description=models.TextField()

    def __str__(self):
        return str(self.pointTitle)

    class Meta:
        verbose_name_plural = 'TechnicianPositivePoints'


class CustomerSurvey(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    orderRating = models.FloatField()
    survayDate = models.DateTimeField()
    customerPositivePoints = models.ForeignKey(CustomerPositivePoints, on_delete=models.CASCADE)
    customerNegativePoints = models.ForeignKey(CustomerNegativePoints, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.orderId)

    class Meta:
        verbose_name_plural = 'CustomerSurvey'


class TicketStatus(models.Model):
    statusName=models.CharField(max_length=10)
    statusTitle=models.CharField(max_length=10)
    description=models.TextField()

    def __str__(self):
        return str(self.statusTitle)

    class Meta:
        verbose_name_plural = 'TicketStatus'


class TicketPriority(models.Model):
    priorityName = models.CharField(max_length=10)
    priorityTitle = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return str(self.priorityTitle)

    class Meta:
        verbose_name_plural = 'TicketStatus'


class Tickets(models.Model):
    ticketNo=models.CharField(max_length=10)
    createBy=models.ForeignKey(User,on_delete=models.CASCADE , related_name='CreateBY')
    answerBy=models.ForeignKey(User,on_delete=models.CASCADE , related_name='answerBy')
    createDateTime=models.DateTimeField()
    closedDateTime=models.DateTimeField(null=True,blank=True)
    ticketStatus=models.ForeignKey(TicketStatus, on_delete=models.CASCADE)
    ticketPriority = models.ForeignKey(TicketPriority, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ticketNo)

    class Meta:
        verbose_name_plural = 'Tickets'


class TicketChats(models.Model):
    ticketno=models.ForeignKey(Tickets, on_delete=models.CASCADE)
    sender=models.ForeignKey(User, on_delete=models.CASCADE)
    answerTo=models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    comment=models.TextField()
    chatDateTime=models.DateTimeField()

    def __str__(self):
        return str(self.ticketno) +'-'+str(self.sender) +'-'+str(self.answerTo)

    class Meta:
        verbose_name_plural = 'TicketChats'

