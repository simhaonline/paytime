# Generated by Django 3.1.5 on 2021-01-22 06:07

from __future__ import absolute_import

from django.db import migrations, models

import finance.validators


class Migration(migrations.Migration):

    dependencies = [
        ("finance", "0018_auto_20210121_1229"),
    ]

    operations = [
        migrations.AlterField(
            model_name="package",
            name="days",
            field=models.PositiveIntegerField(
                validators=[finance.validators.validate_number]
            ),
        ),
        migrations.AlterField(
            model_name="package",
            name="name",
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name="package",
            name="return_on_investmentent",
            field=models.PositiveIntegerField(),
        ),
    ]
