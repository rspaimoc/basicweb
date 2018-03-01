# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Sobre(models.Model):
    date = models.DateTimeField()
    amount = models.IntegerField()
    concept = models.TextField(max_length=100)
