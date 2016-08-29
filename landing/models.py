# coding: utf-8

from __future__ import unicode_literals
from django.db import models


class Event(models.Model):
    title = models.CharField('Название', max_length=100)

    def __unicode__(self):
        return 'Event %s' % self.id

class UserProfile(models.Model):
    name = models.CharField('ФИО', max_length=100, unique=False)
    email = models.EmailField('Email', unique=False)
    tel = models.CharField('Телефон', max_length=100, unique=False)
    company_title = models.CharField('Название компании', max_length=100, unique=False)
    company_edrpou = models.CharField('ЕДРПОУ', max_length=100, unique=False)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.email)
