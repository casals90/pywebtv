# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from common.models import user_model


class BaseModel(models.Model):
    class Meta:
        abstract = True

    # creator_by modify_by -> User
    # creator_by = models.ForeignKey(
    #     user_model.User,
    # )

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
