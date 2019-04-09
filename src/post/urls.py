from django.conf.urls import (include, url, )
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^create/(?P<id>\d+)/$', 'post.views.post_view', name='create'),
    url(r'^list/', 'post.views.post_list_view', name='list_detail') ,
    url(r'^detail/$', 'post.views.post_detail_view')
]
