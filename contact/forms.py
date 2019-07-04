#!/usr/bin/python
# _*_coding:utf-8_*_
# @Time     : 2019/7/4 下午2:03
# @Author   : blackysy
# @File     : forms.py
# @Software : PyCharm

from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='E-mail')
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError('Not enough words!')
        return message
