# Generated by Django 3.2.14 on 2022-11-03 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('warehouse', '0001_initial'),
        ('personal', '0001_initial'),
        ('order', '0001_initial'),
        ('baseinfo', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='soldIndividualDevice',
            field=models.ManyToManyField(help_text='در این فیلد اطلاعات قطعه خریداری شده از جدول SoldIndividualDevice ذخیره می شود', to='warehouse.SoldIndividualDevice'),
        ),
        migrations.AddField(
            model_name='order',
            name='applianceBrand',
            field=models.ForeignKey(help_text='در این فیلد نوع لوازم خانگی مربط به سفارش ذخیره می شود', on_delete=django.db.models.deletion.CASCADE, to='baseinfo.appliancebrands'),
        ),
        migrations.AddField(
            model_name='order',
            name='applianceModel',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='در این فیلد نوع لوازم خانگی مربط به سفارش ذخیره می شود', null=True, on_delete=django.db.models.deletion.CASCADE, to='baseinfo.appliances'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(help_text='در این فیلد مشخص می شود سفارش مربوط به کدام مشتری است', on_delete=django.db.models.deletion.CASCADE, to='personal.customers'),
        ),
        migrations.AddField(
            model_name='order',
            name='orderAddress',
            field=models.ForeignKey(help_text='در این فیلد آدرس انجام سفارش ذخیره می شود', on_delete=django.db.models.deletion.CASCADE, to='personal.addresses'),
        ),
        migrations.AddField(
            model_name='order',
            name='orderKind',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='در این فیلد نوع سفارش از جدول KindOfOrder ذخیره می شود', null=True, on_delete=django.db.models.deletion.CASCADE, to='order.kindoforder'),
        ),
        migrations.AddField(
            model_name='order',
            name='orderStatus',
            field=models.ForeignKey(help_text='در این فیلد وضعیت سفارش ذخیره می شود', on_delete=django.db.models.deletion.CASCADE, to='order.orderstatus'),
        ),
        migrations.AddField(
            model_name='order',
            name='orderTimeRange',
            field=models.ForeignKey(help_text='در این فیلد بازه زمانی انجام سفارش ذخیره می شود', on_delete=django.db.models.deletion.CASCADE, to='order.ordertimerange'),
        ),
        migrations.AddField(
            model_name='order',
            name='registerBy',
            field=models.ForeignKey(help_text='در این فیلد ثبت کننده سفارش ذخیره می شود', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='technician',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='در این فیلد تکنسین انجام دهنده سفارش ذخیره می شود', null=True, on_delete=django.db.models.deletion.CASCADE, to='personal.technician'),
        ),
        migrations.AddField(
            model_name='customerproblems',
            name='brandproblem',
            field=models.ForeignKey(blank=True, help_text='در این فلد مشکل از جدول Problems انتخاب میشود', null=True, on_delete=django.db.models.deletion.CASCADE, to='baseinfo.barndsproblems'),
        ),
        migrations.AddField(
            model_name='customerproblems',
            name='categoryProblem',
            field=models.ForeignKey(blank=True, help_text='در این فلد مشکل از جدول Problems انتخاب میشود', null=True, on_delete=django.db.models.deletion.CASCADE, to='baseinfo.aplliancecategoryproblems'),
        ),
        migrations.AddField(
            model_name='customerproblems',
            name='modelProblem',
            field=models.ForeignKey(blank=True, help_text='در این فلد مشکل از جدول Problems انتخاب میشود', null=True, on_delete=django.db.models.deletion.CASCADE, to='baseinfo.problems'),
        ),
        migrations.AddField(
            model_name='customerproblems',
            name='order',
            field=models.ForeignKey(blank=True, help_text='در این فیلد مشخص میشود قطعه خریداری شده مربوط به کدام سفارش است', null=True, on_delete=django.db.models.deletion.CASCADE, to='order.order'),
        ),
        migrations.AddField(
            model_name='customerproblempic',
            name='order',
            field=models.ForeignKey(help_text='در این فیلد مشخص میشود تصویر اپدیت شده مربوط به کدام سفارش است', on_delete=django.db.models.deletion.CASCADE, to='order.order'),
        ),
        migrations.AddField(
            model_name='customerapplianceinvoice',
            name='customerAppliance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.customerappliance'),
        ),
        migrations.AddField(
            model_name='customerapplianceguarantee',
            name='customerAppliance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.customerappliance'),
        ),
        migrations.AddField(
            model_name='customerappliance',
            name='applianceModel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='baseinfo.appliances'),
        ),
        migrations.AddField(
            model_name='customerappliance',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.customers'),
        ),
    ]
