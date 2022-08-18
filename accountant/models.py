from django.db import models
from django.contrib.auth.models import User, Group
from order.models import Order
# from configrules.models import CommissionRules
# Create your models here.


class PaymentStatus(models.Model):
    """
    در این جدول انواع وضعیت پرداخت توسط مدیر سیستم تعریف خواهد شد.
    به عنوان مثال: موفق، نا موفق، اقساطی و ...
    """
    status=models.CharField(max_length=20,help_text='عنوان وضغیت پرداخت')
    description=models.TextField(null=True,blank=True,help_text='توضیحات مربوط به وضعیت پرداخت')

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
    description=models.TextField(null=True,blank=True,help_text='توضیحات مربوط به نوع فاکتور')

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
    description=models.TextField(null=True,blank=True,help_text='توضیحات مربوط به وضعیت فاکتور')

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
    description=models.TextField(null=True,blank=True,help_text='توضیحات مربوط به نوع روش پرداخت')

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
    """
    در این جدول اطلاعات انواع تراکنش ها تعریف می شوند
    """
    transactionKind=models.CharField(max_length=20,help_text='عنوان نوع تراکنش در این فیلد ذخیره می شود')
    descriptions=models.TextField(help_text='توضیحات مربوط به نوع تراکنش در این فیلد ذخیره می شود')

    def __str__(self):
        return str(self.transactionKind)

    class Meta:
        verbose_name_plural = 'TransactionKind'


class BankAccountInfo(models.Model):
    """
    اطلاعات مربوط به حساب بانکی افراد در این جدول ذخیره می شود
    """
    userID=models.ForeignKey(User,on_delete=models.CASCADE,help_text='در این فسلد مشخص میشود این حساب بانکی مربوط به کدام کاربر هست')
    bankName=models.CharField(max_length=20,help_text='نام بانک در این فیلد ذخیره میشود')
    bankAccountNO=models.CharField(max_length=20,help_text='شماره حساب در این فیلد ذخیره میشود')
    bankAccountSHABA=models.CharField(max_length=20,help_text='شماره شبا مربوط به حساب بانکی ذخیره می شود')
    createDate=models.DateTimeField(help_text='در این فیلد مشخص میشود این حساب در تاریخی در سیستم ثبت شده است')

    def __str__(self):
        return str(self.userID) + "-" +str(self.bankName)

    class Meta:
        verbose_name_plural = 'BankAccountInfo'


class Wallet (models.Model):
    """
    اطلاعات مربوط به کیف پول در این جدول ذخیره می شود
    """
    userID=models.ForeignKey(User,on_delete=models.CASCADE,help_text='این فیلد مشخص میکند که این کیف پول مربوط به کدام کاربر می باشد')
    walletName=models.CharField(max_length=20,help_text='شماره یکتا کیف پول در این فیلد ذخیره می شود')
    bankAccount=models.ForeignKey(BankAccountInfo, on_delete=models.CASCADE,help_text='در این فیلد مشخص می شود که کیف پول به چه حساب بانکی متصل است')
    credit=models.BigIntegerField(default=0, help_text='اعتبار کیف پول در این فیلد ذخیره می شود')

    def __str__(self):
        return str(self.userID) + "-" +str(self.walletName)

    class Meta:
        verbose_name_plural = 'Wallet'


class Payment(models.Model):
    """
    اطلاعات مربوط به پرداخت ها در این جدول ذخیره میشود
    """
    invoice = models.ForeignKey(Invoices, on_delete=models.CASCADE,help_text='در این فیلد مشخص میشود که پرداخت به کدام فاکتور مربوط می شود')
    paymentNo=models.CharField(max_length=10,help_text='شماره یکتای پرادخت در این فیلد ذخیره می شود')
    createBy=models.ForeignKey(User, on_delete=models.CASCADE,help_text='در این فیلد مشخص میشود که پرداخت توسط کدام کاربر انجام شده است')
    status=models.ForeignKey(PaymentStatus, on_delete=models.CASCADE,help_text='در این فیلد مشخص میشود که چرداخت ار چه نوعی هست و یکی از اطلاعات جدول PaymentStatus را برمیگرداند')
    invoiceAmount=models.BigIntegerField(help_text='مبلغ پرادخت در این فیلد ذخیره می شود')
    transactionDate=models.DateTimeField(help_text='تاریخ پرادخت در این فیلد ذخیره می شود')
    transactionKind=models.ForeignKey(TransactionKind,on_delete=models.CASCADE,help_text='در این فیلد توع ترکنش از جدول TransactionKind دخیره میشود')
    TRANSACTION_STATUS=[
        ('SUCCESSFUL','موفق'),
        ('FAILED','ناموفق')
    ]
    transactionStatus=models.CharField(max_length=10, choices=TRANSACTION_STATUS,help_text='وضعیت تراکنش در این فیلد ذخیره می شود')
    trackingCode=models.CharField(max_length=30,help_text='در این فیلد گد رهگیری پرداخت ذخیره می شود')
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE, null=True,blank=True,help_text='در این فیلد مشخص میشود که این پرداخت مربوط به کدام کیف پول است')

    def __str__(self):
        return str(self.paymentNo)

    class Meta:
        verbose_name_plural = 'Payment'


class Commissions(models.Model):
    """
    در این جدول پورسانت (کمیسیون) مبربوط به خدمات ذخیره می شوند
    """
    orderNo=models.ForeignKey(Order,on_delete=models.CASCADE,help_text='در این فیلد مشخص می شود پروسانت مربوط به کدام سفارش است')
    # commissionRule=models.ForeignKey(CommissionRules,on_delete=models.CASCADE)
    cost=models.BooleanField(help_text='در این فیلد هزینه انجام شده ذخیره می شود')
    revenue=models.BooleanField(help_text='در این فیلد میزان سود ذخیره می شود')
    technicianCommission=models.BooleanField(help_text='در این فیلد میزان پورسانت تکنسین ذخیره می شود')
    companyCommission=models.BooleanField(help_text='در این فیلد میزان سهم شرکت ذخیره می شود')

    def __str__(self):
        return str(self.orderNo)

    class Meta:
        verbose_name_plural = 'Commissions'


class WalletTransactions(models.Model):
    """
    در این جدول تراکنش های کیف پول ها ثبت می شوند
    """
    originWallet=models.ForeignKey(Wallet,on_delete=models.CASCADE ,related_name='Orgin' ,help_text='در این فیلد میشود تراکنش مربوط به کدام کیف پول مرتبظ است')
    transactionDateTime=models.DateTimeField(help_text='در این فیلد تاریخ و ساعت تراکنش ذخیره می شود')
    transactionAmount=models.BigIntegerField(help_text='در این فیلد میزان مبلغ تراکنش ذخیره می شود')
    TRANSACTION_KIND=[
        ('PAY', 'واریز'),
        ('WITHDRAW', 'برداشت'),
        ('INCOME_TRANSFER','انتقال از'),
        ('OUTCOME_TRANSFER', 'انتقال به')
    ]
    transactionKind= models.CharField(max_length=20,choices=TRANSACTION_KIND,help_text='در این فیلد نوع تراکنش ذخیره می شود')
    payer=models.ForeignKey(User,on_delete=models.CASCADE, null=True , blank= True,help_text='در این فیلد کاربر پرداخت  کننده ذخیره می شود')
    DESTINATION_KIND = [
        ('ORDER', 'مربوط به سفارش'),
        ('WALLET', 'انتقال به کیف پول'),
    ]
    destinationKind=models.CharField(max_length=20,choices=DESTINATION_KIND,help_text='در این فیلد مشخص میشود این تراکنش مربوط به پرداخت سفارش است یا خارج از سفارش پرداخت شده است')
    destinationWallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='Destination',help_text='در این فیلد مشخص میشود این تراکنش مربوط به انتقال مبلغ به کدام کیف پول است')
    destinationInvoice=models.ForeignKey(Invoices,on_delete=models.CASCADE,help_text='در این فیلد مشخص میشود این تراکنش مربوط به کدام فاکتور صادر شده است')

    def __str__(self):
        return str(self.originWallet)

    class Meta:
        verbose_name_plural = 'WalletTransactions'


