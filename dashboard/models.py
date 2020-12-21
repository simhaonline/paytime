from __future__ import absolute_import

from django.db import models

# Create your models here.


class TimeStampMixin(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
