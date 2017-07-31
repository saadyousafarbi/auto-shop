from __future__ import unicode_literals

from django.shortcuts import render


def welcome(request):
    return render(request, 'autoshop_welcome.html')
