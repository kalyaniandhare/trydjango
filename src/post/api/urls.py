from django.conf.urls import (include, url, )
from django.contrib import admin
from post.api.views import ( PostListAPIView, )

urlpatterns = [
    url(r'^$', PostListAPIView.as_view())
]
