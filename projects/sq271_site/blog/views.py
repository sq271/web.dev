from django.shortcuts import get_object_or_404, render
from django.template import loader, Context
from django.http import HttpResponse, Http404, HttpResponseRedirect

from blog.models import Post



def index(request):
    ls = Post.objects.order_by('-timestamp')[:20]
    return render(request,'blog/list.html',{'list':ls})


def detail(request, url):
    deets = get_object_or_404(Post, slug=url)
    return render(request,'blog/detail.html',{'deet':deets})



