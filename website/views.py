from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import WebsiteModel

# Create your views here.

# View
def defaultView(request):
    return render(
        request,
        "website/hello.html",
        {
            "message": "Hello Websites!",
        },
    )
def addWebsite(request):
    return

def index(request):
    return render(
        request,
        "website/website_list.html",
        {
            'website': WebsiteModel.objects.all(),
        }
    )

def store(request):
    return render(
            request,
            "website/hello.html",
            {
                "message": "Store!",
            },
        )

def edit(request, url_id=None):
    return render(
            request,
            "website/hello.html",
            {
                "message": "Edit!",
            },
        )