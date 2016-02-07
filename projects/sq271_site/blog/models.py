import datetime

from django.db import models
from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField

class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug



class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return 'do shit here'


class PostAdmin(MarkdownModelAdmin):
    list_display = ('title','timestamp','publish')
    prepopulated_fields = {'slug': ('title',), }
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
