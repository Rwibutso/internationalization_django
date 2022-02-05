from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from django.template import loader



def index(request):
    template = loader.get_template('index.html')
    context = {
        'hello' : 'Hello'
    }
    return HttpResponse(template.render(context, request))