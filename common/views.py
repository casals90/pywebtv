# -*- encoding: utf-8 -*-
from django.contrib.auth import get_user_model

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView


def index(request):
    return HttpResponse("Hello, world. You're at the web TV index.")


class ProfileView(DetailView):
    model = get_user_model()
    context_object_name = 'user_object'
    template_name = 'register/profile.html'
