# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='login')
def list_channels(request):
    return render(request, 'channels.html')
