import datetime

from django.db import models
from django.contrib import admin


class Paste(models.Model):
    #id = models.AutoField(primary_key=True)
    hash = models.CharField(max_length=64, unique=True, primary_key=True)
    title = models.CharField(max_length=64, default='Untitled')
    owner = models.CharField(max_length=32, blank=True)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    private = models.BooleanField(default=False)
    
    
    class Meta:
        ordering = ('-time',)


    def __str__(self):
        return str(self.title)


    @models.permalink
    def get_absolute_url(self):
        return  ('pastebin.views.detail', [self.hash])



class PasteAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'time', 'hash', 'private')




admin.site.register(Paste, PasteAdmin)

