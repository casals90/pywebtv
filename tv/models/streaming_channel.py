# -*- encoding: utf-8 -*-
from django.db.models import CharField, ImageField, URLField, ForeignKey
from django.utils.translation import ugettext as _
from common.models.base_model import BaseModel
from common.models.user_model import User


class StreamingChannel(BaseModel):
    class Meta:
        verbose_name = _('Streaming channel')
        verbose_name_plural = _('Streaming channels')
        permissions = (
        )

    description = CharField(
        null=True,
        blank=True,
        max_length=1024,
        verbose_name=_('Description')
    )

    icon = ImageField(
        null=True,
        blank=True,
        verbose_name=_('Channel icon'),
        upload_to='images/%Y/%m/%d/channel_icons'
    )

    url = URLField(
        null=False,
        blank=False,
        verbose_name=_('URL streaming channel')
    )

    owner_user = ForeignKey(
        User,
        default=None,
        related_name='channels',
        verbose_name=_('Owner streaming channels'),
    )
