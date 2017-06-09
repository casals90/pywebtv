# -*- encoding: utf-8 -*-
from django.contrib import admin
from common.models import user_model


admin.site.register(user_model.User)
