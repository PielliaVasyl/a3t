# coding: utf-8

from __future__ import unicode_literals
from django.db import models


class Event(models.Model):
    title = models.CharField('Название', max_length=100)

    def __unicode__(self):
        return 'Event %s' % self.id

# class User(models.Model):
#     name = models.CharField('Имя', max_length=100)
#     email = models.EmailField('Адрес электронной почты', unique=False)
#     age = models.CharField('Возраст', max_length=1, choices=USER_AGE_CHOICES, default="2")
#     sex = models.CharField('Пол', max_length=1, choices=USER_SEX_CHOICES)
#
#     def __unicode__(self):
#         return "%s (%s)" % (self.name, self.email)
