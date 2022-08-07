from django.db import models
from personal.models import CustomerCategory,TechnicianCategory
from accountant.models import PaymentKind
from order.models import KindOfOrder
from baseinfo.models import Appliances


# Create your models here.
#
class CommissionRules(models.Model):
    commissionRuleName=models.CharField(max_length=20)
    customerCategory=models.ForeignKey(CustomerCategory, on_delete=models.CASCADE)
    technicianCategory=models.ForeignKey(TechnicianCategory, on_delete=models.CASCADE)
    orderKind=models.ForeignKey(KindOfOrder, on_delete=models.CASCADE)
    appliances=models.ForeignKey(Appliances, on_delete=models.CASCADE)
    paymentKind=models.ForeignKey(PaymentKind,on_delete=models.CASCADE )
    technicianCommission=models.FloatField()
    companyCommission=models.FloatField()

    def __str__(self):
        return str(self.commissionRuleName)

    class Meta:
        verbose_name_plural = 'CommissionRules'