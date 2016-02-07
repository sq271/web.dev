from django.shortcuts import get_object_or_404, render
from django.template import loader, Context
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse

from paste.models import Paste
from paste.forms import PasteForm


def index(request):
    if request.method == "POST":
        form = PasteForm(request.POST)
        if form.is_valid():
            formpost = form.save()
            return HttpResponseRedirect(formpost)
        else:
            print(form.errors)
    else:
        form = PasteForm()

    return render(request,'paste/form.html/',{'form':form})


def detail(request, url):
    deet = get_object_or_404(Paste, hash=url)
    return render(request,'paste/detail.html',{'deet':deet})

