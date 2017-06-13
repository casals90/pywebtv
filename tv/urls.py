# -*- encoding: utf-8 -*-
from django.conf.urls import url
from tv.views import crud

urlpatterns = [
    url(r'^channels$', crud.list_channels, name='channels'),
    url(r'^new_channel$', crud.StreamingChannelCreate.as_view(), name='new_channel')
]
