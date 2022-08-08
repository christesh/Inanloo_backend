# Generated by Django 3.2.14 on 2022-08-08 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personal', '0001_initial'),
        ('baseinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('individualDeviceBarcode', models.CharField(max_length=40)),
                ('individualDeviceStatus', models.CharField(choices=[('Available', 'موجود در انبار'), ('Sold', 'فروخته شده'), ('Loaned', 'امانی'), ('Returned', 'مرجوعی')], max_length=30)),
                ('individualDeviceDescription', models.TextField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseinfo.devices')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.supplier')),
            ],
            options={
                'verbose_name_plural': 'IndividualDevice',
            },
        ),
        migrations.CreateModel(
            name='SoldIndividualDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.BigIntegerField()),
                ('salesKind', models.CharField(choices=[('Sold', 'فروخته شده'), ('Loaned', 'امانی'), ('Garranty', 'گارانتی')], max_length=30)),
                ('description', models.TextField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.individualdevice')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.companymembers')),
                ('technician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.technician')),
            ],
            options={
                'verbose_name_plural': 'SoldIndividualDevice',
            },
        ),
    ]
