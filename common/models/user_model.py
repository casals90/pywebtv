# -*- encoding: utf-8 -*-
from django.contrib.auth import models as auth_models
from django.db import models
from django.utils.translation import ugettext as _


class User(auth_models.AbstractUser):

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        permissions = (
        )

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

    profile_photo = models.ImageField(
        blank=True,
        null=True,
        upload_to='photos/profile/'
    )
