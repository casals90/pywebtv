from django.contrib import admin
from tv.models import streaming_channel

@admin.register(streaming_channel.StreamingChannel)
class StreamingChannelAdmin(admin.ModelAdmin):
    model = streaming_channel.StreamingChannel
