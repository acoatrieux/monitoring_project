from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import WebsiteModel
from .forms import WebsiteForm
from django.urls import reverse
from django.db.models import Q

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
            'websites': WebsiteModel.objects.all(),
        }
    )

def store(request):
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("website:index"))
    else:
        form = WebsiteForm()
    return render(
        request,
        'website/utils/form.html',
        {
            'title': "Nouveau website",
            'form': form,
        }
    )

def edit(request, website_id=None):
    current_instance = None
    if website_id:
        current_instance = WebsiteModel.objects.get(
            Q(id = website_id),
            )
    form_class = WebsiteForm
    if request.method == 'POST':
        form = form_class(request.POST, instance = current_instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("website:index"))
    else:
        form = form_class(instance = current_instance)
    return render(
        request,
        'website/utils/form.html',
        {
            'title': "Appel",
            'form':form,
        }
    )