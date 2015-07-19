#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from gallery.views import *
import settings
from django.conf.urls.static import static
urlpatterns = patterns('',
    url(r'^$',index,name='首页'),
    #v0.2
    url(r'^post/$',post,name='发布页'),
    url(r'^t/(?P<id>\d+)/$',show_by_tag,name='标签页'),
    url(r'^p/(?P<id>\d+)/$',show_photo,name='图片页'),
    #v0.3
    url(r'^accounts/register/',register_,name='注册页'),
    url(r'^accounts/login/',login_,name='登陆页'),
    url(r'^accounts/logout/',logout_,name='退出账号'),
    #v0.3.5
    url(r'^msg/',message,name='留言板页'),
    #v0.4.5
    #url(r'^t/movie/$',,name='电影海报'),
    #url(r'^t/wallpaper/$',,name='壁纸'),
    #url(r'^t/fans/$',,name='粉丝创作'),
    #url(r'^t/cp/$',,name='有关cp党的画作'),
    #url(r'^t/cp/ds_hg/$',,name='大圣和猴哥'),
    #url(r'^t/cp/ds_hd/$',,name='大圣和混沌'),
    #url(r'^t/cp/ds_ts/$',,name='大圣和江流儿'),
    #url(r'^t/comic/$',,name='四格漫画'),
    #url(r'^t/headphoto/$',,name='头像'),

    # Examples:
    # url(r'^$', 'DaSheng.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


