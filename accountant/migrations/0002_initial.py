# Generated by Django 3.2.14 on 2022-11-03 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accountant', '0001_initial'),
        ('order', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='invoices',
            name='orderNo',
            field=models.ForeignKey(help_text='این فیلد مشخص میکند که این فاکتور به کدام سفارش ارتباظ داره', on_delete=django.db.models.deletion.CASCADE, to='order.order'),
        ),
        migrations.AddField(
            model_name='invoices',
            name='paymentKind',
            field=models.ForeignKey(help_text='توسط این فیلد نوع روش پرداحت از جدول PaymentKind انتخاب می شود', on_delete=django.db.models.deletion.CASCADE, to='accountant.paymentkind'),
        ),
        migrations.AddField(
            model_name='commissions',
            name='orderNo',
            field=models.ForeignKey(help_text='در این فیلد مشخص می شود پروسانت مربوط به کدام سفارش است', on_delete=django.db.models.deletion.CASCADE, to='order.order'),
        ),
        migrations.AddField(
            model_name='bankaccountinfo',
            name='userID',
            field=models.ForeignKey(help_text='در این فسلد مشخص میشود این حساب بانکی مربوط به کدام کاربر هست', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
