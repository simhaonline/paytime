# Generated by Django 3.1.3 on 2020-12-13 15:46

from __future__ import absolute_import

import dirtyfields.dirtyfields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import dashboard.models
import finance.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Wallet",
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
                (
                    "balance",
                    models.DecimalField(decimal_places=2, default=0, max_digits=12),
                ),
                (
                    "book_balance",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=12, null=True
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            bases=(
                dirtyfields.dirtyfields.DirtyFieldsMixin,
                models.Model,
                dashboard.models.TimeStampMixin,
            ),
        ),
        migrations.CreateModel(
            name="Transactions",
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
                (
                    "transaction_type",
                    models.CharField(
                        choices=[("deposit", "Deposit"), ("withdrawal", "Withdrawal")],
                        max_length=20,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("expired", "Expired"),
                            ("done", "Done"),
                            ("closed", "Closed"),
                            ("none", "None"),
                        ],
                        default="none",
                        max_length=20,
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=12)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transactions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            bases=(
                dirtyfields.dirtyfields.DirtyFieldsMixin,
                models.Model,
                dashboard.models.TimeStampMixin,
            ),
        ),
        migrations.CreateModel(
            name="Bank",
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
                (
                    "bank",
                    models.CharField(
                        choices=[
                            ("access_bank", "Access Bank"),
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
                        max_length=30,
                    ),
                ),
                (
                    "account_number",
                    models.CharField(
                        help_text="Enter your 10 digit account number",
                        max_length=10,
                        validators=[finance.validators.validate_account_number],
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bank_details",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            bases=(
                dirtyfields.dirtyfields.DirtyFieldsMixin,
                models.Model,
                dashboard.models.TimeStampMixin,
            ),
        ),
    ]