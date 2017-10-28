# -*- coding: utf-8 -*-

from django.shortcuts import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('hello')

