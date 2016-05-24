from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse, Http404, HttpResponseRedirect

from pastebin.models import Paste
from pastebin.forms import PasteForm


def list(request):
    lists = Paste.objects.all()
    plate = loader.get_template('list.html')
    text = Context({ 'list': lists })
    return HttpResponse(plate.render(text))


def detail(request, url):
    if Paste.objects.filter(hash=url).exists():
        deets = Paste.objects.filter(hash=url)
    else:
        raise Http404("Paste Does Not Exist")
    plate = loader.get_template('detail.html')
    text = Context({ 'deets': deets })
    return HttpResponse(plate.render(text))


def index(request):
    return HttpResponse("index_page")


def about(request):
    plate = loader.get_template('about.html')
    text = Context({})
    return HttpResponse(plate.render(text))


def new_paste(request):
    if request.method == "POST":
        form = PasteForm(request.POST)
        if form.is_valid():
            form.save()
            return list(request)
        else:
            print(form.errors)
    else:
        form = PasteForm()
    
    return render(request, 'add.html', {'form': form})














