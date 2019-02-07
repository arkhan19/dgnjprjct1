# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class color(models.Model):
    name=models.CharField(max_length=10)
    type=models.CharField(default='plain', max_length=10)


class palette(models.Model):
    name=models.CharField(max_length=10)
    validity=models.PositiveIntegerField(default=28)
    type=models.ForeignKey(color)