#!/usr/bin/python
# _*_coding:utf-8_*_
# @Time     : 2019/7/4 上午10:47
# @Author   : blackysy
# @File     : views.py.py
# @Software : PyCharm

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from contact.forms import ContactForm


def contact(request):
    errors = []
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'norepl@example.com'),
                ['blackysy@qq.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )
    return render_to_response('contact_form.html', {'form': form})
