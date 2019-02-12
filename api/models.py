# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Person(models.Model):
    photo = models.ImageField()
    finger_right_thumb = models.ImageField(blank=True, null=True)
    finger_right_index = models.ImageField(blank=True, null=True)
    finger_right_middle = models.ImageField(blank=True, null=True)
    finger_right_ring = models.ImageField(blank=True, null=True)
    finger_right_little = models.ImageField(blank=True, null=True)
    finger_left_thumb = models.ImageField(blank=True, null=True)
    finger_left_index = models.ImageField(blank=True, null=True)
    finger_left_middle = models.ImageField(blank=True, null=True)
    finger_left_ring = models.ImageField(blank=True, null=True)
    finger_left_little = models.ImageField(blank=True, null=True)

