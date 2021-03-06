from __future__ import absolute_import

import threading

from django.contrib.contenttypes import fields
from django.contrib.contenttypes.models import ContentType
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models

from dashboard.models import TimeStampMixin
from finance.models import Bank, Investment, Package, Transactions
from user.models import User

CREATE = "create"
UPDATE = "update"
DELETE = "delete"
KIND_CHOICES = ((CREATE, "create"), (UPDATE, "update"), (DELETE, "delete"))

BLUE = "blue"
GREEN = "green"
PURPLE = "purple"
YELLOW = "yellow"
COLOUR_CHOICES = (
    (BLUE, "blue"),
    (GREEN, "green"),
    (PURPLE, "purple"),
    (YELLOW, "yellow"),
)


class ModelChange(models.Model):
    # This is used by auditing.middleware.GlobalRequestMiddleware to store
    # the current request object, if any, per thread.
    thread = threading.local()

    PRIMARY_MODELS = [Bank, User, Package, Investment, Transactions]

    # Create/update/delete
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    kind = models.CharField(max_length=6, choices=KIND_CHOICES)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    # What fields were changed to what values (if create or update)
    changes = models.CharField(null=True, blank=True, max_length=200)
    subject = models.CharField(null=True, blank=True, max_length=200)
    # The object whose changes we will want to query later (Building, Location)
    primary = fields.GenericForeignKey("primary_ct", "primary_id")

    primary_ct = models.ForeignKey(
        ContentType, related_name="primaries", on_delete=models.CASCADE
    )
    primary_id = models.PositiveIntegerField()
    colour_code = models.CharField(max_length=12, choices=COLOUR_CHOICES)
