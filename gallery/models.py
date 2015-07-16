#-*- coding:utf-8 -*-
from django.db import models
from django.contrib import admin

# Create your models here.
class Tag(models.Model):
	name=models.CharField(max_length=20,null=False,unique=True,default="")
	#ename=models.CharField(max_length=20,null=False,unique=True,default="")
	def __unicode__(self):
		return self.name

class Photo(models.Model):
    title=models.CharField(max_length=20,null=False)
    url=models.URLField()
    tags=models.ManyToManyField(Tag,related_name='has_photos',blank=True)
    add_time=models.TimeField(auto_now=True)
    def __unicode__(self):
        return u'%s' %(self.title)

admin.site.register(Photo)
admin.site.register(Tag)