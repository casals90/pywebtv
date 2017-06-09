# -*- encoding: utf-8 -*-
from django.contrib import admin
from common.models import user_model


@admin.register(user_model.User)
class UserAdmin(admin.ModelAdmin):
    model = user_model.User
