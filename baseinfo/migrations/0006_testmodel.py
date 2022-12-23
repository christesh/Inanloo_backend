# Generated by Django 3.2.14 on 2022-12-22 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseinfo', '0005_alter_counties_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='testModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testpic', models.ImageField(upload_to='testimages/')),
            ],
            options={
                'verbose_name_plural': 'test',
            },
        ),
    ]
