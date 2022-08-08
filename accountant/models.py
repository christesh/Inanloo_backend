from django.db import models
from django.contrib.auth.models import User, Group
from order.models import Order
# from configrules.models import CommissionRules
# Create your models here.


class PaymentStatus(models.Model):
    """
    در این جدول انواع وضعیت پرداخت توسظ مدیر سیستم تعریف خواهد شد.
    به عنوان مثال: موفق، نا موفق، اقساطی و ...
    """
    status=models.CharField(max_length=20,help_text='عنوان وضغیت پرداخت')
    description=models.TextField(help_text='توضیحات مربوط به وضعیت پرداخت')

    def __str__(self):
        return str(self.status)

    class Meta:
        verbose_name_plural = 'PaymentStatus'


class InvoiceKinds(models.Model):
    """
    منظور از invoice، فاکتور است. در این جدول انواع فاکتور توسط مدیر سیستم تعریف می شود
    به عنوان مثال: فاکتور تکنسین، فاکتور مشتری و ...
    """
    invoiceKinds=models.CharField(max_length=20,help_text='عنوان نوع فاکتور')
    description=models.TextField(help_text='توضیحات مربوط به نوع فاکتور')

    def __str__(self):
        return str(self.invoiceKinds)

    class Meta:
        verbose_name_plural = 'InvoiceKinds'

class InvoiceStatus(models.Model):
    """
    منظور از invoice، فاکتور است. در این جدول انواع وضعیت فاکتور توسط مدیر سیستم تعریف می شود
    به عنوان مثال: پرداخت شده، پرداخت نشده، صادر شده و ...
    """
    invoiceKinds=models.CharField(max_length=20,help_text='عنوان وضعیت فاکتور')
    description=models.TextField(help_text='توضیحات مربوط به وضعیت فاکتور')

    def __str__(self):
        return str(self.invoiceKinds)

    class Meta:
        verbose_name_plural = 'InvoiceKinds'


class PaymentKind(models.Model):
    """
        در این جدول انواع روش پرداخت توسظ مدیر سیستم تعریف خواهد شد.
        به عنوان مثال: نقدی، پرداخت اینترنتی، کیف پول و ...
    """
    paymentKind=models.CharField(max_length=10,help_text='عنوان نوع روش پرداخت')
    description=models.TextField(help_text='توضیحات مربوط به نوع روش پرداخت')

    def __str__(self):
        return str(self.paymentKind)

    class Meta:
        verbose_name_plural = 'PaymentKind'


class Invoices(models.Model):
    """
    در این جدول اطلاعات مربوط به فاکتورهای صادر شده ذخیره میشود
    """
    orderNo= models.ForeignKey(Order, on_delete=models.CASCADE,help_text='این فیلد مشخص میکند که این فاکتور به کدام سفارش ارتباظ داره')
    invoiceNo=models.CharField(max_length=20,help_text='شماره فاکتور')
    invoiceKind=models.ForeignKey(InvoiceKinds,on_delete=models.CASCADE,help_text='توسط این فیلد نوع فاکتور از جدول InvoiceKinds انتخاب می شود')
    paymentKind=models.ForeignKey(PaymentKind, on_delete=models.CASCADE,help_text='توسط این فیلد نوع روش پرداحت از جدول PaymentKind انتخاب می شود')
    accepted=models.BooleanField(help_text='مشخص میکند آیا فاکتور توسط مشتری تایید شده یا خیر')
    acceptedBy=models.ForeignKey(User,on_delete=models.CASCADE,help_text='اطلاعات مربوط به کاربر تایید کننده فاکتور در این فیلد ذخیره می شود')
    acceptedDateTime=models.DateTimeField(help_text='تاریخ و ساعت تایید فاکتور در این قیلد ذخیره می شود')
    invoiceStatus=models.ForeignKey(InvoiceStatus,on_delete=models.CASCADE,help_text='توسط این فیلد وضعیت فاکتور از جدول InvoiceStatus انتخاب می شود')
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


