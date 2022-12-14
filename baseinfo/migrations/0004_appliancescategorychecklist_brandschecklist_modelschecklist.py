# Generated by Django 3.2.14 on 2022-11-25 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseinfo', '0003_logs'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelsChecklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checklistTitle', models.CharField(help_text='در این فیلد عنوان مشکل ذخیره میشود', max_length=20)),
                ('Description', models.TextField(blank=True, help_text='در این فیلد توضیحات مربوط به مشکل ذخیره می شود', null=True)),
                ('appliances', models.ForeignKey(help_text='در این فیلد مشحص میشود مشکل مربوط به کدام یک از لوازم خانگی است', on_delete=django.db.models.deletion.CASCADE, related_name='modelChecklist', to='baseinfo.appliances')),
            ],
            options={
                'verbose_name_plural': 'ModelsChecklist',
            },
        ),
        migrations.CreateModel(
            name='BrandsChecklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checklistTitle', models.CharField(help_text='در این فیلد عنوان مشکل ذخیره میشود', max_length=20)),
                ('Description', models.TextField(blank=True, help_text='در این فیلد توضیحات مربوط به مشکل ذخیره می شود', null=True)),
                ('appliancesBrands', models.ForeignKey(help_text='در این فیلد مشحص میشود مشکل مربوط به کدام یک از لوازم خانگی است', on_delete=django.db.models.deletion.CASCADE, related_name='brandChecklist', to='baseinfo.appliancebrands')),
            ],
            options={
                'verbose_name_plural': 'BrandsChecklist',
            },
        ),
        migrations.CreateModel(
            name='AppliancesCategoryCheckList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checklistTitle', models.CharField(help_text='در این فیلد عنوان مشکل ذخیره میشود', max_length=20)),
                ('Description', models.TextField(blank=True, help_text='در این فیلد توضیحات مربوط به مشکل ذخیره می شود', null=True)),
                ('appliancescategory', models.ForeignKey(help_text='در این فیلد مشحص میشود مشکل مربوط به کدام یک از لوازم خانگی است', on_delete=django.db.models.deletion.CASCADE, related_name='appCatChecklist', to='baseinfo.appliancecategories')),
            ],
            options={
                'verbose_name_plural': 'ApplianceCategoryCheckList',
            },
        ),
    ]
