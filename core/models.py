# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    department = models.CharField(max_length=255, null=True)

class Movie(models.Model):

    topic = models.ForeignKey(Topic)
    author = models.ForeignKey(User)
    duration = models.DurationField(null=True)
    level = models.CharField(max_length=30, null=True, blank=False)
    file = models.FileField(upload_to='video/', null=True)
    img = models.ImageField(upload_to='images/', null=False,default='images/default.jpg')
    description = models.TextField(null=True)
    link = models.URLField(null=False, default='test')


    def __unicode__(self):
        return [self.topic,self.author,self.level,self.duration]
        #return "Course {} Author: {} Duration : {} level : {}".format(self.topic,self.author,self.duration,self.level)