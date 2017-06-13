# -*- encoding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from haystack.query import SearchQuerySet

from common.models.user_model import User
from tv.forms.streaming_channel_form import StreamingChannelForm
from tv.models.streaming_channel import StreamingChannel


def list_channels(request):
    form = StreamingChannelForm()
    return render(request, 'channels_list.html', context={'form': form})


class StreamingChannelSearch(LoginRequiredMixin, ListView):
    object = None
    model = StreamingChannel
    template_name = 'channels_list.html'

    def get_queryset(self):
        return SearchQuerySet.models(self.model).filter()


class StreamingChannelCreate(LoginRequiredMixin, CreateView):
    object = None
    model = StreamingChannel
    form_class = StreamingChannelForm
    success_url = reverse_lazy('tv:channels')
    template_name = 'edit_channel.html'
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        try:
            user = User.objects.get(username=self.request.user)
        except User.DoesNotExist:
            raise PermissionDenied

        self.object = self.model(**form.cleaned_data)
        self.object.owner_user = user
        self.object.save()

        return HttpResponseRedirect(self.success_url)
