import datetime

from django.db import models
from django.contrib import admin


class Imgz(model.Models):
    hash = models.Charfield(max_length=64, unique=True, primary_key=True)
    time = models.DateTimeField(auto_now_add=True)
    img =  


class ImgzAdmin(admin.ModelAdmin):
    list_display = ('hash','time','file')


admin.site.register(Imgz, ImgzAdmin)

