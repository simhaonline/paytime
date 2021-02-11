# Generated by Django 3.1.5 on 2021-02-07 01:38

from __future__ import absolute_import

import dirtyfields.dirtyfields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finance", "0020_auto_20210207_0043"),
    ]

    operations = [
        migrations.CreateModel(
            name="Banks",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                ("name", models.CharField(max_length=30)),
                ("slug", models.SlugField(max_length=15)),
                ("code", models.IntegerField(unique=True)),
                ("country", models.CharField(max_length=30)),
            ],
            options={
                "abstract": False,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.AlterField(
            model_name="bank",
            name="bank",
            field=models.CharField(
                choices=[
                    ("access-bank", "Access Bank"),
                    ("access-bank-diamond", "Access Bank (Diamond)"),
                    ("alat-by-wema", "ALAT by WEMA"),
                    ("asosavings", "ASO Savings and Loans"),
                    ("citibank", "Citibank"),
                    ("dynamic_standard_bank", "Dynamic Standard Bank"),
                    ("ecobank_ngr", "Ecobank Nigeria"),
                    ("fidelity_bank_ngr", "Fidelity Bank Nigeria"),
                    ("fbn", "First Bank of Nigeria"),
                    ("fcmb", "First City Monument Bank"),
                    ("gtb", "Guaranty Trust Bank"),
                    ("hb", "Heritage Bank"),
                    ("jz", "Jaiz Bank"),
                    ("keystone", "Keystone Bank"),
                    ("providus", "Providus Bank"),
                    ("polaris", "Polaris Bank"),
                    ("stanbic", "Stanbic IBTC Bank Nigeria"),
                    ("standard_chartered", "Standard Chartered Bank"),
                    ("sterling", "Sterling Bank"),
                    ("suntrust", "Suntrust Bank Nigeria"),
                    ("union_bank", "Union Bank of Nigeria"),
                    ("uba", "United Bank for Africa"),
                    ("unity_bank", "Unity Bank"),
                    ("wema_bank", "Wema Bank"),
                    ("zenith_bank", "Zenith Bank"),
                ],
                default="access_bank",
                max_length=30,
            ),
        ),
        migrations.AddField(
            model_name="bank",
            name="bank_detail",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="finance.banks",
            ),
        ),
    ]