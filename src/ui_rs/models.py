# encoding:utf-8

from __future__ import unicode_literals

from django.db import models
from helpers.base.jsonfield import JsonField
# Create your models here.


class Tag(models.Model):
    zh=models.CharField('中文标签',max_length=30,unique=True)
    
    def __unicode__(self):
        return self.zh
RESOLUTION=(
    ('300x300','300x300'),
    ('600x300','600x300')
)

class UiResource(models.Model):
    title = models.CharField('标题',max_length=300)
    dsp=models.TextField(verbose_name='资源描述',blank=True)
    rs_dl_urls = JsonField(verbose_name='资源下载列表',blank=[])
    rs_show = models.CharField('资源展示图片',max_length=500,blank=True)
    resolution = models.CharField('展示分辨率',max_length=50,choices=RESOLUTION,default='300x300')
    tags=models.ManyToManyField(Tag,verbose_name='标签')
    added_time=models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    