from django.db import models
from django.contrib.auth.models import User, Group
from order.models import Order
# from configrules.models import CommissionRules
# Create your models here.


class PaymentStatus(models.Model):
    status=models.CharField(max_length=20)
    description=models.TextField()

    def __str__(self):
        return str(self.status)

    class Meta:
        verbose_name_plural = 'PaymentStatus'


class InvoiceKinds(models.Model):
    invoiceKinds=models.CharField(max_length=20)
    description=models.TextField()

    def __str__(self):
        return str(self.invoiceKinds)

    class Meta:
        verbose_name_plural = 'InvoiceKinds'


class PaymentKind(models.Model):
    paymentKind=models.CharField(max_length=10)
    description=models.TextField()

    def __str__(self):
        return str(self.paymentKind)

    class Meta:
        verbose_name_plural = 'PaymentKind'


class Invoices(models.Model):
    orderNo= models.ForeignKey(Order, on_delete=models.CASCADE)
    invoiceNo=models.CharField(max_length=20)
    invoiceKind=models.ForeignKey(InvoiceKinds,on_delete=models.CASCADE)
    paymentKind=models.ForeignKey(PaymentKind, on_delete=models.CASCADE)
    accepted=models.BooleanField()
    acceptedBy=models.ForeignKey(User,on_delete=models.CASCADE)
    acceptedDateTime=models.DateTimeField()

    def __str__(self):
        return str(self.invoiceNo)

    class Meta:
        verbose_name_plural = 'Invoices'


class TransactionKind(models.Model):
    transactionKind=models.CharField(max_length=20)
    descriptions=models.TextField()

    def __str__(self):
        return str(self.transactionKind)

    class Meta:
        verbose_name_plural = 'TransactionKind'


class BankAccountInfo(models.Model):
    userID=models.ForeignKey(User,on_delete=models.CASCADE)
    bankName=models.CharField(max_length=20)
    bankAccountNO=models.CharField(max_length=20)
    bankAccountSHABA=models.CharField(max_length=20)
    createDate=models.DateTimeField()

    def __str__(self):
        return str(self.userID) + "-" +str(self.bankName)

    class Meta:
        verbose_name_plural = 'BankAccountInfo'


class Wallet (models.Model):
    userID=models.ForeignKey(User,on_delete=models.CASCADE)
    walletName=models.CharField(max_length=20)
    bankAccount=models.ForeignKey(BankAccountInfo, on_delete=models.CASCADE)
    credit=models.BigIntegerField()

    def __str__(self):
        return str(self.userID) + "-" +str(self.walletName)

    class Meta:
        verbose_name_plural = 'Wallet'


class Payment(models.Model):
    invoice = models.ForeignKey(Invoices, on_delete=models.CASCADE)
    paymentNo=models.CharField(max_length=10)
    createBy=models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.ForeignKey(PaymentStatus, on_delete=models.CASCADE)
    invoiceAmount=models.BigIntegerField()
    transactionDate=models.DateTimeField()
    transactionKind=models.ForeignKey(TransactionKind,on_delete=models.CASCADE)
    TRANSACTION_STATUS=[
        ('SUCCESSFUL','موفق'),
        ('FAILED','ناموفق')
    ]
    transactionStatus=models.CharField(max_length=10, choices=TRANSACTION_STATUS)
    trackingCode=models.CharField(max_length=30)
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return str(self.paymentNo)

    class Meta:
        verbose_name_plural = 'Payment'


class Commissions(models.Model):
    orderNo=models.ForeignKey(Order,on_delete=models.CASCADE)
    # commissionRule=models.ForeignKey(CommissionRules,on_delete=models.CASCADE)
    cost=models.BooleanField()
    revenue=models.BooleanField()
    technicianCommission=models.BooleanField()
    companyCommission=models.BooleanField()

    def __str__(self):
        return str(self.orderNo)

    class Meta:
        verbose_name_plural = 'Commissions'


class WalletTransactions(models.Model):
    originWallet=models.ForeignKey(Wallet,on_delete=models.CASCADE ,related_name='Orgin' )
    transactionDateTime=models.DateTimeField()
    transactionAmount=models.BigIntegerField()
    TRANSACTION_KIND=[
        ('PAY', 'واریز'),
        ('WITHDRAW', 'برداشت'),
        ('INCOME_TRANSFER','انتقال از'),
        ('OUTCOME_TRANSFER', 'انتقال به')
    ]
    transactionKind= models.CharField(max_length=20,choices=TRANSACTION_KIND)
    payer=models.ForeignKey(User,on_delete=models.CASCADE, null=True , blank= True)
    DESTINATION_KIND = [
        ('ORDER', 'مربوط به سفارش'),
        ('WALLET', 'انتقال به کیف پول'),
    ]
    destinationKind=models.CharField(max_length=20,choices=DESTINATION_KIND)
    destinationWallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='Destination')
    destinationInvoice=models.ForeignKey(Invoices,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.originWallet)

    class Meta:
        verbose_name_plural = 'WalletTransactions'


