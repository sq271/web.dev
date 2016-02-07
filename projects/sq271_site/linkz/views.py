from django.shortcuts import get_object_or_404, render
from django.template import loader, Context
from django.http import HttpResponse, Http404, HttpResponseRedirect

from linkz.models import Linkz
from linkz.forms import LinkzForm


def index(request):
    if request.method == "POST":
        form = LinkzForm(request.POST)
        if form.is_valid():
            formpost = form.save()
            return HttpResponseRedirect(formpost)
        else:
            print(form.errors)
    else:
        form = LinkzForm()

    return render(request,'linkz/form.html/',{'form':form})


def detail(request, url):
    deet = get_object_or_404(Linkz, hash=url)
    return render(request,'linkz/detail.html',{'deet':deet})

