# -*- encoding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from common.models.user_model import User
from tv.forms.streaming_channel_form import StreamingChannelForm
from tv.models.streaming_channel import StreamingChannel


def list_channels(request):
    form = StreamingChannelForm()
    return render(request, 'channels_list.html', context={'form': form})


class StreamingChannelListView(LoginRequiredMixin, ListView):
    model = StreamingChannel
    template_name = 'channels_list.html'

    def get_queryset(self):
        return self.model.objects.filter(owner_user=self.request.user)


class StreamingChannelCreateView(LoginRequiredMixin, CreateView):
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


class StreamingChannelUpdateView(LoginRequiredMixin, UpdateView):
    model = StreamingChannel
    form_class = StreamingChannelForm
    success_url = reverse_lazy('tv:channels')
    template_name = 'edit_channel.html'
    login_url = reverse_lazy('login')


class StreamingChannelDeleteView(LoginRequiredMixin, DeleteView):
    model = StreamingChannel
    success_url = reverse_lazy('tv:channels')
    login_url = reverse_lazy('login')
    template_name = 'confirm_delete_channel.html'
