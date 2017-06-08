# -*- encoding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the web TV index.")