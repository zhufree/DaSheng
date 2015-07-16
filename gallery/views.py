#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from gallery.models import *
from django.template import RequestContext 
# Create your views here.
def index(request):
    photos=Photo.objects.all()
    return render_to_response('index.html',RequestContext(request,{'photos':photos}))

@csrf_exempt
def post(request):
    if request.method=='POST':
        title=request.POST.get('title')
        url=request.POST.get('url')
        tags=request.POST.get('tags').split()
        new_photo=Photo.objects.create(
            title=title,
            url=url
            )
        if tags:
            for tag in tags:
                new_tag,dummy=Tag.objects.get_or_create(name=tag)
                new_photo.tags.add(new_tag)#add tag to new_photo
                new_photo.save()
        return HttpResponseRedirect('/')
    else:
        tags=Tag.objects.all()
        return render_to_response('post.html',RequestContext(request,{'tags':tags}))

def show_by_tag(request,id):
    tag=Tag.objects.get(pk=id)
    return render_to_response('tag.html',RequestContext(request,{'tag':tag}))
