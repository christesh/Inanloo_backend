from django.contrib import admin
from .models import (
    PaymentStatus,
    InvoiceKinds,
    InvoiceStatus,
    PaymentKind,
    Invoices,
    TransactionKind,
    BankAccountInfo,
    Wallet,
    Payment,
    Commissions,
    WalletTransactions
)
# Register your models here.

admin.site.register(PaymentStatus),
admin.site.register(InvoiceKinds),
admin.site.register(InvoiceStatus),
admin.site.register(PaymentKind),
admin.site.register(Invoices),
admin.site.register(TransactionKind),
admin.site.register(BankAccountInfo),
admin.site.register(Wallet),
admin.site.register(Payment),
admin.site.register(Commissions),
admin.site.register(WalletTransactions)