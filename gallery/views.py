#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from gallery.models import *
from gallery.forms import *
from django.template import RequestContext 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser 
# Create your views here.

#v0.1
def index(request):
    photos=Photo.objects.all().order_by('-id')
    return render_to_response('index.html',RequestContext(request,{'photos':photos}))

#v0.2
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
                new_tag.count+=1
                new_tag.save()
                new_photo.tags.add(new_tag)#add tag to new_photo
        new_photo.save()
        return HttpResponseRedirect('/')
    else:
        tags=Tag.objects.all()
        #for tag in tags:
            #tag.count=len(tag.has_photos.all())
            #print tag.count
            #tag.save()
        return render_to_response('post.html',RequestContext(request,{'tags':tags}))

def show_by_tag(request,id):
    tag=Tag.objects.get(pk=id)

    return render_to_response('tag.html',RequestContext(request,{'tag':tag}))

def show_photo(request,id):
    photo=Photo.objects.get(pk=id)
    return render_to_response('photo.html',RequestContext(request,{'photo':photo}))

#v0.3.0
@csrf_protect
def login_(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('disabled account')
        else:
            return HttpResponse('invalid login')
    return render_to_response('registration/login.html',RequestContext(request))

def logout_(request):
    logout(request)
    return HttpResponseRedirect('/')
@csrf_protect
def register_(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            new_user=User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            new_user.save()
            new_user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
            login(request,new_user)
            return HttpResponseRedirect('/')
    else:
        form=RegistrationForm()
    variables=RequestContext(request,{'form':form})
    return render_to_response('registration/register.html',variables)

#v0.3.5
def message(request):
    if request.method=='POST':
        content=request.POST.get('content')
        try:
            new_message=Message.objects.create(
            content=content,
            author=request.user
            )
        except Exception, e:
            new_message=Message.objects.create(
            content=content
            )
            new_message.save()
            return HttpResponseRedirect('/msg/')
        else:
            new_message.save()
            return HttpResponseRedirect('/msg/')
    else:
        msgs=Message.objects.all().order_by('-time')
        return render_to_response('message.html',RequestContext(request,{'msgs':msgs}))