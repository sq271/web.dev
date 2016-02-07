from django.shortcuts import render

def index(request):
    return render(request,'contact/main.html',{})


