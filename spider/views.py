#!/usr/bin/python
# _*_coding:utf-8_*_
# @Time     : 2019/6/28 下午6:23
# @Author   : blackysy
# @File     : views.py
# @Software : PyCharm

from django.template.loader import get_template
from django.template import loader, Context, RequestContext
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, render
import datetime


def hello(request):
    return HttpResponse("Hello World")


def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html', {'hour_offset': offset, 'next_time': dt})


def display_meta(request):
    values = request.META.items()
    values = sorted(values, key=lambda x: x[0])
    return render_to_response('display_meta.html', {'meta': values})


def custom_proc(request):
    """ A context processor that provides 'app', 'user' and 'ip'. """
    return {
        'app': 'My app',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR']
    }