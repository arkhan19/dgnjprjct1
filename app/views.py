# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
# Create your views here.


def create(request):
    fobj = color.objects.create(
        name=request.POST.get('color')
    )
    fobj.save()
    object = palette.objects.create(
        name=request.POST.get('name'),
        type=fobj
    )
    object.save()


def read(request):
    data = palette.objects.filter().all()
    return render(request, 'home.html', {'data':data})

def update(request, pk):
    object = palette.objects.get(id=pk)
    object.name=request.POST.get('New Name')
    object.save()


def delete(request, pk):
    object = palette.objects.get(id=pk)
    object.delete()