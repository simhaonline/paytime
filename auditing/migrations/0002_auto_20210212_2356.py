# Generated by Django 3.1.5 on 2021-02-12 23:56

from __future__ import absolute_import

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auditing", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="modelchange",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="modelchange",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]