# Generated by Django 3.2.14 on 2022-08-08 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accountant', '0002_initial'),
        ('configrules', '0001_initial'),
        ('baseinfo', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commissionrules',
            name='orderKind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.kindoforder'),
        ),
        migrations.AddField(
            model_name='commissionrules',
            name='paymentKind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accountant.paymentkind'),
        ),
        migrations.AddField(
            model_name='commissionrules',
            name='technicianCategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseinfo.techniciancategory'),
        ),
    ]