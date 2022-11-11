# Generated by Django 3.2.14 on 2022-11-03 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApllianceCategoryProblems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problemTitle', models.CharField(help_text='در این فیلد عنوان مشکل ذخیره میشود', max_length=20)),
                ('problemDescription', models.TextField(blank=True, help_text='در این فیلد توضیحات مربوط به مشکل ذخیره می شود', null=True)),
                ('lowPrice', models.CharField(blank=True, help_text='در این فیلد حداقل هزینه مشکل ذخیره می شود', max_length=20, null=True)),
                ('highPrice', models.CharField(blank=True, help_text='در این فیلد حداکثر هزینه مشکل ذخیره می شود', max_length=20, null=True)),
            ],
            options={
                'verbose_name_plural': 'ApllianceCategoryProblems',
            },
        ),
        migrations.CreateModel(
            name='ApplianceBrands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_brandName', models.CharField(help_text='در این فیلد نام برند ذخیره می شود', max_length=50)),
                ('a_brandDescription', models.TextField(blank=True, help_text='در این فیلد توضیحات مربوط به هر برند ذخیره می شود', null=True)),
                ('a_brandImage', models.ImageField(blank=True, null=True, upload_to='images/ApplianceBrands/')),
            ],
            options={
                'verbose_name_plural': 'ApplianceBrands',
            },
        ),
        migrations.CreateModel(
            name='ApplianceCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_categoryName', models.CharField(help_text='در این فیلد عنوان انواع لوازم خانگی ذخیره می شود', max_length=50)),
                ('a_categoryDescription', models.TextField(blank=True, help_text='در این فیلد توضیحات مربوط به لوازم خانگی ذخیره می شود', null=True)),
                ('a_categoryImage', models.ImageField(blank=True, null=True, upload_to='images/ApplianceCategories/')),
            ],
            options={
                'verbose_name_plural': 'ApplianceCategories',
            },
        ),
        migrations.CreateModel(
            name='Appliances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applianceModel', models.CharField(blank=True, help_text='در این فیلد عنوان مدل ذخیره می شود', max_length=20, null=True)),
                ('applianceDescription', models.TextField(blank=True, help_text='در این فیلد توصیخات موربوط به مدل دستگاه ذخیره می شود', null=True)),
                ('applianceRate', models.FloatField(blank=True, help_text='در این فیلد برای مدل ها رنج ارزشی مالی ذخیره می شود', null=True)),
                ('applianceImage', models.ImageField(blank=True, null=True, upload_to='images/Appliances/')),
            ],
            options={
                'verbose_name_plural': 'Appliances',
            },
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityName', models.CharField(help_text='در این فیلد نام شهرستان ذحیره می شود', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='CustomerCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerCategory', models.CharField(help_text='در این فیلد عنوان طبقه ها ذخیره می شود', max_length=50)),
                ('categoryDescription', models.TextField(blank=True, help_text='در این فیلد توضیحات مربوط به طبقه ها ذخیره می شود', null=True)),
            ],
            options={
                'verbose_name_plural': 'CustomerCategory',
            },
        ),
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applianceSerial', models.CharField(blank=True, help_text='در این فیلد سریال دستگاه ذخیره میشود', max_length=20, null=True)),
                ('deviceDescription', models.TextField(blank=True, help_text='در این فیلد توصیخات مدل قطعه ذحیره می شود', null=True)),
                ('deviceImage', models.ImageField(upload_to='images/Devices/')),
                ('appliance', models.ForeignKey(help_text='در این فیلد می شود این قطعه به کدام یک از لوازم خانگی مربیط است', on_delete=django.db.models.deletion.CASCADE, to='baseinfo.appliances')),
            ],
            options={
                'verbose_name_plural': 'Devices',
            },
        ),
        migrations.CreateModel(
            name='DevicesGuarantee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guaranteeStart', models.DateField(blank=True, help_text='تاریخ تولد فرد در این فیلد ذخیره میشود', null=True)),
                ('guaranteePeriod', models.IntegerField(blank=True, help_text='تاریخ تولد فرد در این فیلد ذخیره میشود', null=True)),
                ('isValid', models.BooleanField(blank=True, null=True)),
                ('device', models.ForeignKey(help_text='در این فیلد مشحص میشود قیمت مربوط به کدام قطعه است', on_delete=django.db.models.deletion.CASCADE, to='baseinfo.devices')),
            ],
            options={
                'verbose_name_plural': 'DevicesGuarantee',
            },
        ),
        migrations.CreateModel(
            name='HireForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formName', models.CharField(help_text='در این فیلد نام فرم ذحیره می شود', max_length=20)),
                ('formTitle', models.CharField(help_text='در این فیلد عنوان قابل نمایش فرم ذحیره می شود', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'HireForm',
            },
        ),
        migrations.CreateModel(
            name='MembersPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('active', models.BooleanField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'MembersPermission',
            },
        ),
        migrations.CreateModel(
            name='OTPsms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(help_text='در این فیلد مشخص می شود پبامک برای کدام کاربر ارسال شده است', max_length=11)),
                ('verifyCode', models.CharField(help_text='در این فیلد کد تایید برای ورود یا ثبت نام دخیره می شود', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'OTPsms',
            },
        ),
        migrations.CreateModel(
            name='ProblemsKind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'ProblemsKind',
            },
        ),
        migrations.CreateModel(
            name='Provinces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provinceName', models.CharField(help_text='در این فیلد نام استان ذحیره می شود', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Provinces',
            },
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regionName', models.CharField(help_text='در این فیلد نام منطقه ذحیره می شود', max_length=50)),
                ('regionDescription', models.TextField(blank=True, help_text='در این فیلد توضیحات مربوط به مناطق ذحیره می شود', null=True)),
                ('city', models.ForeignKey(help_text='در این فیلد مشخص میشود منطقه مربوط به کدام شهرستان است', on_delete=django.db.models.deletion.CASCADE, related_name='regions', to='baseinfo.cities')),
            ],
            options={
                'verbose_name_plural': 'Regions',
            },
        ),
        migrations.CreateModel(
            name='SmsTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smsName', models.CharField(help_text='در این فیلد عنوان پیامک ذخیره میشود', max_length=11)),
                ('smsKind', models.CharField(choices=[('info', 'اطلاع رسانی'), ('feadback', 'بازخورد')], help_text='در این فیلد مشخص می شود پیامک ارسالی از نوع اطلاع رسانی بوده یا بازخورد', max_length=10)),
                ('smsCaption', models.TextField(help_text='در این فیلد متن پیامک ارسالی ذخیره می شود')),
            ],
            options={
                'verbose_name_plural': 'SmsTypes',
            },
        ),
        migrations.CreateModel(
            name='TechnicianCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technicianCategory', models.CharField(help_text='در این فیلد عنوان طبقه ها ذخیره می شود', max_length=50)),
                ('technicianDescription', models.TextField(blank=True, help_text='در این فیلد توضیحات مربوط به طبقه ها ذخیره می شود', null=True)),
            ],
            options={
                'verbose_name_plural': 'TechnicianCategory',
            },
        ),
        migrations.CreateModel(
            name='Sms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smsCaption', models.TextField(help_text='در این فیلد متن پیامک ارسالی ذخیره می شود')),
                ('smsSendDateTime', models.DateTimeField(help_text='در این فیلد زمان ارسال پیامک ارسالی ذخیره می شود')),
                ('smsAnswer', models.TextField(help_text='در این فیلد پاسخ دریافتی از مخاطب ذخیره می شود')),
                ('smsReceiveDateTime', models.DateTimeField(help_text='در این فیلد زمان دریافت پیامک جواب ذخیره می شود')),
                ('receiver', models.ForeignKey(help_text='در این فیلد گیرنده پیامک ذخیره می شود', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('smsType', models.ForeignKey(help_text='در این فیلد مشخص میشو پیامک مربوط به کدام نوع از پیامک های تعریف شده در جدول SmsTypes میشود', on_delete=django.db.models.deletion.CASCADE, to='baseinfo.smstypes')),
            ],
            options={
                'verbose_name_plural': 'SmsTypes',
            },
        ),
        migrations.CreateModel(
            name='RegionsGeofence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regionLat', models.FloatField(help_text='در این فیلد عرض جعرافیایی ذحیره می شود')),
                ('regionLong', models.FloatField(help_text='در این فیلد طول جعرافیایی ذحیره می شود')),
                ('region', models.ForeignKey(help_text='در این فیلد مشحص می شود هر نقطه مربوط به کدام منظقه می شود', on_delete=django.db.models.deletion.CASCADE, to='baseinfo.regions')),
            ],
            options={
                'verbose_name_plural': 'RegionsGeofence',
            },
        ),
        migrations.CreateModel(
            name='ProvinceGeofence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provinceLat', models.FloatField(help_text='در این فیلد عرض جعرافیایی ذحیره می شود')),
                ('provinceLong', models.FloatField(help_text='در این فیلد طول جغرافیایی ذحیره می شود')),
                ('province', models.ForeignKey(help_text='در این فیلد می شود  نقطه محدوده مربوط به کدام استان است', on_delete=django.db.models.deletion.CASCADE, to='baseinfo.provinces')),
            ],
            options={
                'verbose_name_plural': 'ProvinceGeofence',
            },
        ),
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problemTitle', models.CharField(help_text='در این فیلد عنوان مشکل ذخیره میشود', max_length=20)),
                ('problemDescription', models.TextField(blank=True, help_text='در این فیلد توضیحات مربوط به مشکل ذخیره می شود', null=True)),
                ('lowPrice', models.CharField(blank=True, help_text='در این فیلد حداقل هزینه مشکل ذخیره می شود', max_length=20, null=True)),
                ('highPrice', models.CharField(blank=True, help_text='در این فیلد حداکثر هزینه مشکل ذخیره می شود', max_length=20, null=True)),
                ('appliances', models.ForeignKey(help_text='در این فیلد مشحص میشود مشکل مربوط به کدام یک از لوازم خانگی است', on_delete=django.db.models.deletion.CASCADE, related_name='modelProblem', to='baseinfo.appliances')),
                ('problemKind', models.ForeignKey(blank=True, help_text='در این فیلد نوع مشکل ذخیره می شود', null=True, on_delete=django.db.models.deletion.CASCADE, to='baseinfo.problemskind')),
            ],
            options={
                'verbose_name_plural': 'Problems',
            },
        ),
        migrations.CreateModel(
            name='Neighbourhoods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighbourhoodName', models.CharField(help_text='در این فیلد نام محله ذحیره می شود', max_length=50)),
                ('neighbourhoodDescription', models.TextField(blank=True, help_text='در این فیلد توضیحات مربوط به محله ذحیره می شود', null=True)),
                ('region', models.ForeignKey(help_text='در این فیلد مشخص میشود منطقه مربوط به کدام شهرستان است', on_delete=django.db.models.deletion.CASCADE, related_name='neighbourhoods', to='baseinfo.regions')),
            ],
            options={
                'verbose_name_plural': 'Neighbourhoods',
            },
        ),
        migrations.CreateModel(
            name='NeighbourhoodGeofence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighbourhoodLat', models.FloatField(help_text='در این فیلد عرض جعرافیایی ذحیره می شود')),
                ('neighbourhoodLong', models.FloatField(help_text='در این فیلد طول جعرافیایی ذحیره می شود')),
                ('neighbourhood', models.ForeignKey(help_text='در این فیلد مشحص می شود هر نقطه مربوط به کدام محله می شود', on_delete=django.db.models.deletion.CASCADE, to='baseinfo.neighbourhoods')),
            ],
            options={
                'verbose_name_plural': 'NeighbourhoodGeofence',
            },
        ),
        migrations.CreateModel(
            name='MembersGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(help_text='در این فیلد عنوان گروه ها ذخیره می شود', max_length=40)),
                ('description', models.TextField(blank=True, help_text='در این فیلد توضیحات مربوط به گروه ها ذخیره می شود', null=True)),
                ('permissions', models.ManyToManyField(blank=True, null=True, to='baseinfo.MembersPermission')),
            ],
            options={
                'verbose_name_plural': 'MembersGroup',
            },
        ),
        migrations.CreateModel(
            name='HireJson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formJson', models.TextField(help_text='در این فیلد طراحی فرم  به صورت Json ذحیره می شود')),
                ('form', models.ForeignKey(help_text='در این فیلد مشحص می شود هریک از طراحی های انجام شده مربوط به کدام فرم است', on_delete=django.db.models.deletion.CASCADE, to='baseinfo.hireform')),
            ],
            options={
                'verbose_name_plural': 'HireJson',
            },
        ),
        migrations.CreateModel(
            name='DevicesPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devicePrice', models.BigIntegerField(help_text='در این فیلد قیمت قطعه ذحیره می شود')),
                ('createdDate', models.DateTimeField(help_text='در این فیلد تاریخ ثبت قیمت قطعه ذحیره می شود')),
                ('device', models.ForeignKey(help_text='در این فیلد مشحص میشود قیمت مربوط به کدام قطعه است', on_delete=django.db.models.deletion.CASCADE, to='baseinfo.devices')),
            ],
            options={
                'verbose_name_plural': 'DevicesPrice',
            },
        ),
        migrations.CreateModel(
            name='DevicesGuaranteeImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/Devices/Guarantee')),
                ('guarantee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseinfo.devicesguarantee')),
            ],
            options={
                'verbose_name_plural': 'DevicesGuaranteeImages',
            },
        ),
        migrations.CreateModel(
            name='Counties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countyName', models.CharField(help_text='در این فیلد نام شهرستان ذحیره می شود', max_length=50)),
                ('province', models.ForeignKey(help_text='در این فیلد مشخص میشود شهرستان مربوط به کدام استان است', on_delete=django.db.models.deletion.CASCADE, related_name='counties', to='baseinfo.provinces')),
            ],
        ),
        migrations.CreateModel(
            name='CityGeofence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityLat', models.FloatField(help_text='در این فیلد عرض جعرافیایی ذحیره می شود')),
                ('cityLong', models.FloatField(help_text='در این فیلد طول جغرافیایی ذحیره می شود')),
                ('city', models.ForeignKey(help_text='در این فیلد می شود نقطه محدوده مربوط به کدام شهرستان است', on_delete=django.db.models.deletion.CASCADE, to='baseinfo.cities')),
            ],
            options={
                'verbose_name_plural': 'CityGeofence',
            },
        ),
        migrations.AddField(
            model_name='cities',
            name='county',
            field=models.ForeignKey(help_text='در این فیلد مشخص میشود شهرستان مربوط به کدام استان است', on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='baseinfo.counties'),
        ),
        migrations.CreateModel(
            name='BarndsProblems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problemTitle', models.CharField(help_text='در این فیلد عنوان مشکل ذخیره میشود', max_length=20)),
                ('problemDescription', models.TextField(blank=True, help_text='در این فیلد توضیحات مربوط به مشکل ذخیره می شود', null=True)),
                ('lowPrice', models.CharField(blank=True, help_text='در این فیلد حداقل هزینه مشکل ذخیره می شود', max_length=20, null=True)),
                ('highPrice', models.CharField(blank=True, help_text='در این فیلد حداکثر هزینه مشکل ذخیره می شود', max_length=20, null=True)),
                ('appliancesBrands', models.ForeignKey(help_text='در این فیلد مشحص میشود مشکل مربوط به کدام یک از لوازم خانگی است', on_delete=django.db.models.deletion.CASCADE, related_name='brandProblem', to='baseinfo.appliancebrands')),
                ('problemKind', models.ForeignKey(blank=True, help_text='در این فیلد نوع مشکل ذخیره می شود', null=True, on_delete=django.db.models.deletion.CASCADE, to='baseinfo.problemskind')),
            ],
            options={
                'verbose_name_plural': 'BarndsProblems',
            },
        ),
        migrations.CreateModel(
            name='AppliancesSupplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appliance', models.ForeignKey(help_text='در این فیلد نام دستگاه ذخیره میشود', on_delete=django.db.models.deletion.CASCADE, to='baseinfo.appliances')),
            ],
            options={
                'verbose_name_plural': 'AppliancesSupplier',
            },
        ),
    ]
