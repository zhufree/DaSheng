#-*- coding:utf-8 -*-
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
#v0.2
# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=20,null=False,unique=True,default="")
    count=models.IntegerField(default=0)
    #ename=models.CharField(max_length=20,null=False,unique=True,default="")
    def __unicode__(self):
        return self.name

class Photo(models.Model):
    title=models.CharField(max_length=20,null=False)
    url=models.URLField()
    tags=models.ManyToManyField(Tag,related_name='has_photos',blank=True)
    add_time=models.TimeField(auto_now=True)
    is_show=models.BooleanField(default=True)
    def __unicode__(self):
        return u'%s' %(self.title)
#v0.3.5
class Message(models.Model):
    content=models.CharField(max_length=3000)
    author=models.ForeignKey(User,related_name='user_messages',default=2)
    time=models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return u'%s'%(self.content)

#v0.4.0 增加照片评论
class Comment(models.Model):
    content=models.CharField(max_length=5000)
    author=models.ForeignKey(User,related_name='user_comments')
    time=models.DateTimeField(auto_now_add=True)
    photo=models.ForeignKey(Photo,related_name='photo_comments')

admin.site.register(Photo)
admin.site.register(Tag)
admin.site.register(Message)
admin.site.register(Comment)