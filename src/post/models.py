from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    updated = models.DateTimeField(auto_now_add=True, auto_now=False)
    timestamps = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title
