from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettex as _


def index(request):
    output = _('statusMsg')
    return render(request, 'index.html', output)
