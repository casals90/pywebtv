# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _


class BaseModel(models.Model):
    class Meta:
        abstract = True

    creation_date = models.DateTimeField(
        blank=False,
        null=False,
        auto_now_add=True,
        db_index=True,
        verbose_name=_('Creation date'),
    )
    modification_date = models.DateTimeField(
        blank=False,
        null=False,
        auto_now_add=True,
        db_index=True,
        verbose_name=_('Modification date'),
    )
    delete_date = models.DateTimeField(
        blank=True,
        null=True,
        db_index=True,
        verbose_name=_('Delete date')
    )
