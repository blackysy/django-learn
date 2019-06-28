#!/usr/bin/python
# _*_coding:utf-8_*_
# @Time     : 2019/6/28 下午6:23
# @Author   : blackysy
# @File     : views.py
# @Software : PyCharm


from django.http import HttpResponse, Http404
import datetime


def hello(request):
    return HttpResponse("Hello World")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)