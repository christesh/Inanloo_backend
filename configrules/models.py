from django.db import models
from personal.models import CustomerCategory,TechnicianCategory
from accountant.models import PaymentKind
from order.models import KindOfOrder
from baseinfo.models import Appliances


# Create your models here.
#
class CommissionRules(models.Model):
    """
    در این جدول انواع نحوه محاسبه پورسانت تعریف میشود
    """
    commissionRuleName=models.CharField(max_length=20, help_text='در این فیلد یک نام برای فرمول محاسبه پورسانت ذخیره می شود')
    customerCategory=models.ForeignKey(CustomerCategory, on_delete=models.CASCADE, help_text='در این فیلد نوع مشتری ذخیره می شود')
    technicianCategory=models.ForeignKey(TechnicianCategory, on_delete=models.CASCADE, help_text='در این فیلد نوع تکنسین ذخیره می شود')
    orderKind=models.ForeignKey(KindOfOrder, on_delete=models.CASCADE, help_text='در این فیلد نوع خدمت ذخیره می شود')
    appliances=models.ForeignKey(Appliances, on_delete=models.CASCADE, help_text='در این فیلد نوع لوازم خانگی ذخیره می شود')
    paymentKind=models.ForeignKey(PaymentKind,on_delete=models.CASCADE , help_text='در این فیلد نوع پرداخت ذخیره می شود')
    technicianCommission=models.FloatField(help_text='در این فیلد سهم تکنسین ذخیره می شود')
    companyCommission=models.FloatField( help_text='در این فیلد شهم شرکت ذخیره می شود')

    def __str__(self):
        return str(self.commissionRuleName)

    class Meta:
        verbose_name_plural = 'CommissionRules'