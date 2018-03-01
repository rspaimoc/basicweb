# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

# Create your views here.

def mainpage(request):
    template  = get_template('mainpage.html')
    variables = Context({
        'titlehead': 'Sobes aPP',
        'pagetitle': 'Welcome to the Sobres aPPlication',
        'contentbody': 'Magin non legal funding since 2013'
        })
    otuput = template.render(variables)
    return HttpResponse(output)
