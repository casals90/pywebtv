# -*- encoding: utf-8 -*-
from django.forms import ModelForm

from tv.models.streaming_channel import StreamingChannel


class StreamingChannelForm(ModelForm):
    class Meta:
        model = StreamingChannel
        fields = [
            'name',
            'description',
            'icon',
            'url'
        ]
