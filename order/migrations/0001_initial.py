# Generated by Django 3.2.14 on 2022-11-03 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('baseinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAppliance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applianceSerial', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'verbose_name_plural': 'CustomerAppliance',
            },
        ),
        migrations.CreateModel(
            name='CustomerApplianceGuarantee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guaranteePic', models.ImageField(upload_to='images/CustomerApplianceGuarantee/')),
                ('guaranteeStartDate', models.CharField(blank=True, max_length=30, null=True)),
                ('guaranteeEndDate', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'verbose_name_plural': 'CustomerApplianceGuarantee',
            },
        ),
        migrations.CreateModel(
            name='CustomerApplianceInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoicePic', models.ImageField(upload_to='images/CustomerApplianceInvoice/')),
            ],
            options={
                'verbose_name_plural': 'CustomerApplianceInvoice',
            },
        ),
        migrations.CreateModel(
            name='CustomerProblemPic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problemImage', models.ImageField(upload_to='images/CustomerProblems/')),
            ],
            options={
                'verbose_name_plural': 'CustomerProblemPic',
            },
        ),
        migrations.CreateModel(
            name='CustomerProblems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerDescription', models.TextField(blank=True, help_text='?????????? ???????? ?????????????? ?????????? ???? ???????????? ???????????? ?????????? ?????????? ??????????', null=True)),
            ],
            options={
                'verbose_name_plural': 'CustomerProblems',
            },
        ),
        migrations.CreateModel(
            name='KindOfOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderKind', models.CharField(help_text='???? ?????? ???????? ???? ?????????? ???????? ?????? ?????????? ?????????? ???? ??????', max_length=20)),
                ('description', models.TextField(blank=True, help_text='???? ?????? ???????? ?????????????? ?????????? ???? ?????? ?????????? ?????????? ???? ??????', null=True)),
            ],
            options={
                'verbose_name_plural': 'KindOfOrder',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registerDateTime', models.DateTimeField(help_text='???? ?????? ???????? ???????? ?????? ?????????? ?????????? ???? ??????')),
                ('applianceSerial', models.CharField(blank=True, help_text='???? ?????? ???????? ?????? ?????????? ?????????? ???????? ???? ?????????? ?????????? ???? ??????', max_length=30, null=True)),
                ('orderDate', models.DateField(help_text='???? ?????? ???????? ?????????? ?????????? ?????????? ?????????? ???? ??????')),
                ('description', models.TextField(blank=True, help_text='???? ?????? ???????? ?????????????? ?????????? ?????????? ???? ?????????? ?????????? ?????????? ???? ??????', null=True)),
            ],
            options={
                'verbose_name_plural': 'Order',
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(help_text='???? ?????? ???????? ?????????? ?????????? ?????????? ???? ??????', max_length=20)),
                ('description', models.TextField(blank=True, help_text='???? ?????? ???????? ?????????????? ?????????? ???? ?????????? ?????????? ???? ??????', null=True)),
            ],
            options={
                'verbose_name_plural': 'OrderStatus',
            },
        ),
        migrations.CreateModel(
            name='OrderTimeRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeRange', models.CharField(help_text='???? ?????? ???????? ???? ?????? ???????? ???????? ?????????? ?????????? ???? ??????', max_length=20)),
                ('startTime', models.TimeField(help_text='???? ?????? ???????? ???????? ???????? ???????? ?????????? ?????????? ???? ??????')),
                ('endTime', models.TimeField(help_text='???? ?????? ???????? ???????? ?????????? ???????? ?????????? ?????????? ???? ??????')),
                ('description', models.TextField(blank=True, help_text='???? ?????? ???????? ?????????????? ???????? ???????? ???????? ?????????? ?????????? ???? ??????', null=True)),
            ],
            options={
                'verbose_name_plural': 'OrderTimeRange',
            },
        ),
        migrations.CreateModel(
            name='TechnicianProblems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technicianDescription', models.TextField(blank=True, help_text='?????????? ???????? ?????????????? ?????????? ???? ???????????? ???????????? ???????????? ?????????? ??????????', null=True)),
                ('order', models.ForeignKey(help_text='???? ?????? ???????? ???????? ?????????? ???????? ?????????????? ?????? ?????????? ???? ???????? ?????????? ??????', on_delete=django.db.models.deletion.CASCADE, to='order.order')),
                ('problem', models.ForeignKey(help_text='???? ?????? ?????? ???????? ???? ???????? Problems ???????????? ??????????', on_delete=django.db.models.deletion.CASCADE, to='baseinfo.problems')),
            ],
            options={
                'verbose_name_plural': 'TechnicianProblems',
            },
        ),
        migrations.CreateModel(
            name='TechnicianProblemPic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problemImage', models.ImageField(upload_to='images/CustomerProblems/')),
                ('order', models.ForeignKey(help_text='???? ?????? ???????? ???????? ?????????? ?????????? ?????????? ?????? ?????????? ???? ???????? ?????????? ??????', on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
            options={
                'verbose_name_plural': 'CustomerProblemPic',
            },
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(help_text='???? ?????? ???????? ???????? ?????????? ???????? ?????????????? ?????? ?????????? ???? ???????? ?????????? ??????', on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
            options={
                'verbose_name_plural': 'OrderDetails',
            },
        ),
    ]
