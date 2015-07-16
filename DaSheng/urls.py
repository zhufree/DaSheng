#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from gallery.views import *
import settings
from django.conf.urls.static import static
urlpatterns = patterns('',
    url(r'^$',index,name='index_page'),
    url(r'^post/$',post,name='post_page'),
    url(r'^t/(?P<id>\d+)/$',show_by_tag,name='tag_page'),
    url(r'^p/(?P<id>\d+)/$',show_photo,name='show_photo_page'),
    #url(r'^movie/$',,name='电影海报'),
    #url(r'^wallpaper/$',,name='壁纸'),
    #url(r'^fans/$',,name='粉丝创作'),
    #url(r'^cp/$',,name='有关cp党的画作'),
    #url(r'^cp/ds_hg/$',,name='大圣和猴哥'),
    #url(r'^cp/ds_hd/$',,name='大圣和混沌'),
    #url(r'^cp/ds_ts/$',,name='大圣和江流儿'),
    #url(r'^comic/$',,name='四格漫画'),
    #url(r'^headphoto/$',,name='头像'),
    #url(r'^photo/(?P<id>\d+)/$',,name='详细页'),
    #url(r'^post/$',,name='上传页'),
    # Examples:
    # url(r'^$', 'DaSheng.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


