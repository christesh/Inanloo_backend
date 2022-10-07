# Generated by Django 3.2.14 on 2022-09-28 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('baseinfo', '0001_initial'),
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('individualDeviceBarcode', models.CharField(help_text='در این فیلد بارکد قطعه ذخیره میشود', max_length=40)),
                ('individualDeviceStatus', models.CharField(choices=[('Available', 'موجود در انبار'), ('Sold', 'فروخته شده'), ('Loaned', 'امانی'), ('Returned', 'مرجوعی')], help_text='در این فیلد وضعیت قطعه ذخیره میشود', max_length=30)),
                ('individualDeviceDescription', models.TextField(blank=True, help_text='در این فیلد توضیحات قطعه ذخیره میشود', null=True)),
                ('device', models.ForeignKey(help_text='در این فیلد قطعه از جدول Devices ذخیره میشود', on_delete=django.db.models.deletion.CASCADE, to='baseinfo.devices')),
                ('supplier', models.ForeignKey(help_text='در این فیلد تامین کننده قطعه از جدول Supplier ذخیره میشود', on_delete=django.db.models.deletion.CASCADE, to='personal.supplier')),
            ],
            options={
                'verbose_name_plural': 'IndividualDevice',
            },
        ),
        migrations.CreateModel(
            name='SoldIndividualDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.BigIntegerField(help_text='در این فیلد قیمت قطعه مشخص میشود')),
                ('salesKind', models.CharField(choices=[('Sold', 'فروخته شده'), ('Loaned', 'امانی'), ('Garranty', 'گارانتی')], help_text='در این فیلد توع قروش قطعه مشخص میشود', max_length=30)),
                ('description', models.TextField(blank=True, help_text='در این فیلد توضیحات مربوط به فروش قطعه ذخیره میشود', null=True)),
                ('device', models.ForeignKey(help_text='در این فیلد مشخص میشود قطعه مربوط به کدام قطعه از جدول IndividualDevice است', on_delete=django.db.models.deletion.CASCADE, to='warehouse.individualdevice')),
                ('seller', models.ForeignKey(help_text='در این فیلد مشخص میشود  پرسنل شرکت (انباردار) فروشنده قطعه کیست', on_delete=django.db.models.deletion.CASCADE, to='personal.companymembers')),
                ('technician', models.ForeignKey(help_text='در این فیلد مشخص میشود تکنسین تحویل گرینده قطعه کیست', on_delete=django.db.models.deletion.CASCADE, to='personal.technician')),
            ],
            options={
                'verbose_name_plural': 'SoldIndividualDevice',
            },
        ),
    ]
