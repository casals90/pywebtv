# -*- encoding: utf-8 -*-
from django.conf.urls import url
from tv.views import crud

urlpatterns = [
    url(r'^channels$', crud.StreamingChannelListView.as_view(), name='channels'),
    url(r'^new_channel$', crud.StreamingChannelCreateView.as_view(), name='new_channel'),
    url(r'^update_channel/(?P<pk>[\w-]+)$', crud.StreamingChannelUpdateView.as_view(), name='update_channel'),
    url(r'^delete_channel/(?P<pk>[\w-]+)$', crud.StreamingChannelDeleteView.as_view(), name='delete_channel')
]
