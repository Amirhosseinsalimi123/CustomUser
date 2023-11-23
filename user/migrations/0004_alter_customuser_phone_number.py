# Generated by Django 4.2.6 on 2023-11-23 06:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_customuser_phone_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.BigIntegerField(unique=True, validators=[django.core.validators.RegexValidator(message='phone number must be Iranian', regex='9(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}')], verbose_name='phone number'),
        ),
    ]