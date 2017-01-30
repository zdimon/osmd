# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=250, verbose_name='Title')
    content = RichTextField()
    meta_content = models.TextField()
    meta_title =   models.TextField()
    meta_keywords = models.TextField()
    slug = models.CharField(verbose_name='slug', blank=True, max_length=250)

    def __unicode__(self):
        return self.title



class Subject(models.Model):
    title = models.CharField(max_length=250,verbose_name=_(u'заголовок'))
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = _(u'тема')
        verbose_name_plural = _(u'темы')


class Photo(models.Model):
    name = models.CharField(max_length=250,verbose_name=_(u'заголовок'), blank=True, null=True)
    image  = models.ImageField(upload_to='photo', verbose_name=u'Изображение', blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    def __unicode__(self):
        return self.image.path
