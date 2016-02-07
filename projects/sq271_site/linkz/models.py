import datetime

from django.db import models
from django.contrib import admin


class Linkz(models.Model):
    hash = models.CharField(max_length=64, unique=True, primary_key=True)
    title = models.CharField(max_length=64, default='Untitled')
    body = models.TextField()
    owner = models.CharField(max_length=32, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    private = models.BooleanField(default=False)

    class Meta:
        ordering = ('-time',)

    def __str__(self):
        return str(self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('linkz.views.detail', [self.hash])


class LinkzAdmin(admin.ModelAdmin):
    list_display = ('title','time','hash')


admin.site.register(Linkz, LinkzAdmin)
