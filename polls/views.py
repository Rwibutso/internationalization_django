from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _


def index(request):
    output = _('statusMsg')
    return HttpResponse(output)
