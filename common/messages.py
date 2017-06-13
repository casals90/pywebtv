# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext as _
from enum import Enum


class CommonMsg(Enum):
    # Forms
    FIELD_REQUIRED = _('This field is required')
