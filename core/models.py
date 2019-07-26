# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Topics(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False)

    def __unicode__(self):
        return self.name

class Department(models.Model):
    pass


class Token(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    token = models.CharField(max_length=48)

    def __unicode__(self):
        return self.token


class Course(models.Model):

    topic = models.ForeignKey(Topics)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    duration = models.DurationField(null=True, blank=True)
    level = models.CharField(max_length=30, null=True, blank=True)
    video = models.FileField(upload_to='video/', null=True)
    image = models.ImageField(upload_to='images/',null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(null=False, default='http://localhost:8000', blank=True)

    def __unicode__(self):
        return "topic {}  author {} ".format(self.topic, self.author)
