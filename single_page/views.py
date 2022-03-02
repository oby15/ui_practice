from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.

def singlepage(request):
    return render(request, "single_page/singlepage.html")

def index(request):
    return render(request, "single_page/index.html")

texts = ["Text 1", "Text 2", "Text 3"]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")

def scroll(request):
    return render(request, "single_page/scroll.html")