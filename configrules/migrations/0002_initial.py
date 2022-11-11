# Generated by Django 3.2.14 on 2022-11-03 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('baseinfo', '0001_initial'),
        ('order', '0001_initial'),
        ('accountant', '0002_initial'),
        ('configrules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commissionrules',
            name='orderKind',
            field=models.ForeignKey(help_text='در این فیلد نوع خدمت ذخیره می شود', on_delete=django.db.models.deletion.CASCADE, to='order.kindoforder'),
        ),
        migrations.AddField(
            model_name='commissionrules',
            name='paymentKind',
            field=models.ForeignKey(help_text='در این فیلد نوع پرداخت ذخیره می شود', on_delete=django.db.models.deletion.CASCADE, to='accountant.paymentkind'),
        ),
        migrations.AddField(
            model_name='commissionrules',
            name='technicianCategory',
            field=models.ForeignKey(help_text='در این فیلد نوع تکنسین ذخیره می شود', on_delete=django.db.models.deletion.CASCADE, to='baseinfo.techniciancategory'),
        ),
    ]
